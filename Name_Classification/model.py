import torch
import torch.nn as nn

class RNN (nn.RNN):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2o = nn.Linear(hidden_size+input_size, output_size)
        self.i2h = nn.Linear(hidden_size+input_size, hidden_size)
        self.softmax = nn.LogSoftmax(dim=1)
          
    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        out = self.i2o(combined)
        next_hidden = self.i2h(combined)
        out = self.softmax(out)

        return out, next_hidden

    def init_hidden(self):
        return torch.zeros(1, self.hidden_size)