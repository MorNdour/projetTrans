import sys
from unittest.mock import MagicMock

import numpy as np

# Mock tflite_runtime before importing prediction module
sys.modules.setdefault("tflite_runtime", MagicMock())
sys.modules.setdefault("tflite_runtime.interpreter", MagicMock())

from classification.config import CLASS_NAMES
from classification.src.prediction import classify_image


def _make_mock_interpreter(predicted_index):
    """Create a mock TFLite interpreter that returns a fixed prediction."""
    scores = np.zeros(len(CLASS_NAMES), dtype=np.float32)
    scores[predicted_index] = 1.0

    interpreter = MagicMock()
    interpreter.get_output_details.return_value = [{"index": 0}]
    interpreter.get_tensor.return_value = np.array([scores])
    return interpreter


def test_classify_returns_string():
    interp = _make_mock_interpreter(0)
    result = classify_image(interp, None)
    assert isinstance(result, str)


def test_classify_returns_correct_class():
    for i, expected_name in enumerate(CLASS_NAMES):
        interp = _make_mock_interpreter(i)
        assert classify_image(interp, None) == expected_name


def test_classify_calls_invoke():
    interp = _make_mock_interpreter(0)
    classify_image(interp, None)
    interp.invoke.assert_called_once()
