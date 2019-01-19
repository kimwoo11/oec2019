import torch.utils.data as data


class Dataset(data.Dataset):
    def __init__(self, feat, label):
        self.feat = feat
        self.label = label

    def __len__(self):
        return len(self.feat)

    def __getitem__(self, index):
        feat = self.feat[index]
        label = self.label[index]
        return feat, label