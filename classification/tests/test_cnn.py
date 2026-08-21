import pytest
from tensorflow.keras import models

from classification.models.cnn import build_cnn


def test_build_cnn_returns_model():
    model = build_cnn((256, 256, 3), 10)
    assert model is not None


def test_output_shape():
    model = build_cnn((256, 256, 3), 10)
    output_shape = model.output_shape
    assert output_shape[-1] == 10


def test_different_n_classes():
    for n in [2, 5, 15]:
        model = build_cnn((128, 128, 3), n)
        assert model.output_shape[-1] == n


def test_model_is_sequential():
    model = build_cnn((256, 256, 3), 10)
    assert isinstance(model, models.Sequential)


def test_model_has_layers():
    model = build_cnn((256, 256, 3), 10)
    assert len(model.layers) > 0
