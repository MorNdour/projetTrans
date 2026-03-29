import cv2
import numpy as np
import pytest

from classification.src.preprocess import (
    TomatoDataset,
    remove_background,
    train_transform,
)


@pytest.fixture
def tmp_image(tmp_path):
    """Create a small temporary green image for testing."""
    img = np.zeros((64, 64, 3), dtype=np.uint8)
    img[:, :] = (0, 180, 0)  # BGR green
    path = str(tmp_path / "test_leaf.jpg")
    cv2.imwrite(path, img)
    return path


class TestTomatoDataset:
    def test_len(self, tmp_image):
        ds = TomatoDataset([tmp_image, tmp_image], [0, 1])
        assert len(ds) == 2

    def test_getitem_returns_image_and_label(self, tmp_image):
        ds = TomatoDataset([tmp_image], [5])
        img, label = ds[0]
        assert label == 5
        assert img.shape[0] > 0 and img.shape[1] > 0

    def test_getitem_with_transform(self, tmp_image):
        ds = TomatoDataset([tmp_image], [0], transform=train_transform)
        img, label = ds[0]
        assert img.shape[:2] == (256, 256)


class TestRemoveBackground:
    def test_returns_rgb_array(self, tmp_image):
        result = remove_background(tmp_image)
        assert isinstance(result, np.ndarray)
        assert result.ndim == 3
        assert result.shape[2] == 3

    def test_output_same_spatial_size(self, tmp_image):
        original = cv2.imread(tmp_image)
        result = remove_background(tmp_image)
        assert result.shape[:2] == original.shape[:2]

    def test_green_region_preserved(self, tmp_image):
        result = remove_background(tmp_image)
        # Green image should have non-zero pixels after masking
        assert result.sum() > 0


class TestTrainTransform:
    def test_resize_to_256(self):
        img = np.random.randint(0, 255, (100, 150, 3), dtype=np.uint8)
        out = train_transform(image=img)["image"]
        assert out.shape[:2] == (256, 256)
