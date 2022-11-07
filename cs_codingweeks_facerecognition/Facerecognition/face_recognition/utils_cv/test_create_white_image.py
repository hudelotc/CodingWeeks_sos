from create_white_image import create_white_image
from pytest import *
import numpy as np


def test_create_white_image():
    assert np.array_equal(create_white_image(),np.array([[[255], [255], [255], [255]], [[255], [255], [255], [255]], [[255], [255], [255], [255]], [[255], [255], [255], [255]]], dtype=np.uint8)) == True


test_create_white_image()