import torch.nn as nn
import torch.nn.functional as F


class MultiLayerPerceptron(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(MultiLayerPerceptron, self).__init__()

        # Initializing parameters
        self.input_size = input_size
        self.output_size = 5
        self.hidden_size = hidden_size

        # Activation functions and linear layers
        self.fc1 = nn.Linear(self.input_size, self.hidden_size)
        self.act1 = nn.Tanh()
        self.fc2 = nn.Linear(self.hidden_size, self.hidden_size)
        self.act2 = nn.Tanh()
        self.fc4 = nn.Linear(self.hidden_size, self.output_size)
        self.act4 = nn.LeakyReLU()

    def forward(self, features):
        x = self.fc1(features)
        x = self.act1(x)
        x = self.fc2(x)
        x = self.act2(x)
        x = self.fc4(x)
        x = self.act4(x)
        return F.softmax(x)  # Normalize to prob distribution

