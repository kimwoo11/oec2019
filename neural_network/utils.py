import torch
import numpy as np

from neural_network.dataset import Dataset
from torch.utils.data import DataLoader
from neural_network.models import MultiLayerPerceptron
from sklearn.model_selection import train_test_split

seed = 0
torch.manual_seed(seed)
np.random.seed(seed)


def evaluate(model, val_loader):
    total_corr = 0

    for i, vbatch in enumerate(val_loader):
        feats, label = vbatch
        prediction = model(feats)
        corr = torch.argmax(prediction, dim=1) == torch.argmax(label, dim=1)
        total_corr += int(corr.sum())

    return float(total_corr) / len(val_loader.dataset)


def feats_data(data):
    continuous_feats = ['age', 'sex', 'preg', 'pulse', 'br', 'temp', 'siast', 'diast', 'oxysat', 'pain', 'glasgow']
    data_continuous = np.zeros((data.shape[0], 11))
    for i, feat in enumerate(continuous_feats):
        column = data[feat]
        data_continuous[:, i] = column
    return data_continuous


def load_data(batch_size, data):
    data_processed = feats_data(data)
    label = data['level']

    l_dict = {1: [1, 0, 0, 0, 0],
              2: [0, 1, 0, 0, 0],
              3: [0, 0, 1, 0, 0],
              4: [0, 0, 0, 1, 0],
              5: [0, 0, 0, 0, 1]}

    labels = np.zeros((len(label), 5))
    for i in range(len(label)):
        if label[i] == 1:
            labels[i] = (l_dict[1])
        elif label[i] == 2:
            labels[i] = (l_dict[2])
        elif label[i] == 3:
            labels[i] = (l_dict[3])
        elif label[i] == 4:
            labels[i] = (l_dict[4])
        else:
            labels[i] = (l_dict[5])

    feat_train, feat_val, label_train, label_val = train_test_split(data_processed,
                                                                    labels,
                                                                    test_size=0.2,
                                                                    random_state=seed)
    train_dataset = Dataset(feat_train, label_train)
    val_dataset = Dataset(feat_val, label_val)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)

    return train_loader, val_loader


def load_model(lr, input_size, hidden_size):
    model = MultiLayerPerceptron(input_size, hidden_size)
    loss_fnc = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)

    return model, loss_fnc, optimizer
