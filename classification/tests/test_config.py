import os

from classification.config import (
    BATCH_SIZE, IMAGE_SIZE, CHANNELS, EPOCHS, N_CLASSES,
    CLASS_NAMES, BASE_DIR, FIREBASE_CONFIG,
)


def test_hyperparameters_are_positive():
    assert BATCH_SIZE > 0
    assert IMAGE_SIZE > 0
    assert CHANNELS > 0
    assert EPOCHS > 0


def test_class_names_length_matches_n_classes():
    assert len(CLASS_NAMES) == N_CLASSES


def test_class_names_are_strings():
    for name in CLASS_NAMES:
        assert isinstance(name, str)
        assert len(name) > 0


def test_base_dir_exists():
    assert os.path.isdir(BASE_DIR)


def test_firebase_config_has_required_keys():
    required = [
        "apiKey", "authDomain", "databaseURL",
        "projectId", "storageBucket",
    ]
    for key in required:
        assert key in FIREBASE_CONFIG
