import argparse
import pandas as pd
from neural_network.utils import *

seed = 0
torch.manual_seed(seed)
np.random.seed(seed)


def train():
    # Setting hyper-parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=5)
    parser.add_argument('--lr', type=float, default=10)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--eval_every', type=int, default=1)
    parser.add_argument('--hidden_size', type=int, default=11)
    parser.add_argument('--input_size', type=int, default=11)

    args = parser.parse_args()

    data = pd.read_csv("data.csv")

    train_loader, val_loader = load_data(args.batch_size, data)
    model, loss_fnc, optimizer = load_model(lr=args.lr, input_size=args.input_size, hidden_size=args.hidden_size)
    model = model.double()  # Switch the model to double precision for greater accuracy

    batch_num = 0

    for epoch in range(args.epochs):
        # initialize to zero for every new epoch
        accum_loss = 0
        tot_corr = 0
        tot_attempts = 0

        for idx, batch in enumerate(train_loader, 0):  # enumerate s.t. idx=0 initially
            # gets one "batch" of data
            feats, labels = batch

            # set all gradients to zero
            optimizer.zero_grad()

            # run neural network model on the batch
            predictions = model(feats)

            # compute loss function using correct answer for the entire batch
            normal_labels = torch.argmax(labels, dim=1)

            batch_loss = loss_fnc(input=predictions, target=normal_labels.long())
            accum_loss += batch_loss

            # compute gradient of loss with respect to the parameters
            # use back-propagation
            batch_loss.backward()

            # change the parameters in the model by one 'step' guided by
            # the learning rate. Parameters are the weights and bias
            optimizer.step()

            # calculate number of correct predictions
            corr = torch.argmax(predictions, dim=1) == torch.argmax(labels, dim=1)
            tot_corr += int(corr.sum())
            tot_attempts += args.batch_size

            # evaluate the model on the validation set every eval_every steps
            if idx % args.eval_every == 0:
                valid_acc = evaluate(model, val_loader)
                train_acc = float(tot_corr) / float(tot_attempts)
                print("Epoch: %d | Step: %d | Loss: %0.3f | Correct: %d | Training Accuracy: %0.3f | Valid Acc.: %0.3f"
                      % (epoch + 1, idx + 1, accum_loss / args.eval_every, tot_corr, train_acc, valid_acc))

                accum_loss = 0
                tot_corr = 0
                tot_attempts = 0

            batch_num += 1
            torch.save(model, "model.pt".format(idx))


if __name__ == "__main__":
    train()
