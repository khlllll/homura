import os
from datetime import datetime

# vocabularies
EPOCH = "epoch"
ITER_PER_EPOCH = "iter_per_epoch"
LOSS = "loss"
MODEL = "model"
MODE = "mode"
OPTIMIZER = "optimizer"
OUTPUT = "output"
TARGET = "target"
TEST = "test"
TRAIN = "train"
TRAINER = "trainer"
STEP = "step"
NOW = datetime.now().strftime("%b%d-%H-%M-%S")
BASIC_DIR_NAME = NOW + f"{os.getpid():0>5}"
DATA = "data"
GPU = "cuda"
CPU = "cpu"
