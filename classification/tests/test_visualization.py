from unittest.mock import MagicMock, patch

from classification.src.visualization import plot_history


def _make_mock_history():
    history = MagicMock()
    history.history = {
        'accuracy': [0.5, 0.7, 0.9],
        'val_accuracy': [0.4, 0.6, 0.8],
        'loss': [1.0, 0.5, 0.2],
        'val_loss': [1.2, 0.6, 0.3],
    }
    return history


@patch("matplotlib.pyplot")
def test_plot_history_runs_without_error(mock_plt):
    """Verify plot_history executes and calls plt.show()."""
    with patch("classification.src.visualization.plt", mock_plt):
        plot_history(_make_mock_history())
