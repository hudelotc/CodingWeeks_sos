from utils_cv.loading import *
from pytest import *

def test_load():
    assert type(load("../Data/tetris_blocks.png")) == np.ndarray

