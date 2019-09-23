import argparse

def get_train_args():
    "Get args needed while training"

    parser = argparse.ArgumentParser('Train a model for Name Classification')

    parser.add_argument('--hidden_dim',
                        type=int,
                        default=128,
                        help='Hidden state dimension of RNN')

    args = parser.parse_args()
    return args