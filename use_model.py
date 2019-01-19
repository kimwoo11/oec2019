import torch


def use_model(feats):
    model = torch.load('neural_network/model.pt')
    feats = torch.Tensor(feats)
    model = model.float()
    predictions = model(feats)
    return int(torch.argmax(predictions)) + 1
