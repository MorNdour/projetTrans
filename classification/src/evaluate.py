"""Evaluation helpers for model predictions."""

from sklearn.metrics import confusion_matrix, classification_report
import numpy as np


def compute_confusion_matrix(y_true, y_pred):
	"""
	Compute a confusion matrix from true and predicted labels.

	Accepts labels as integer class indices or one-hot encoded arrays.

	Returns:
		numpy.ndarray: square confusion matrix (counts).
	"""
	y_true_arr = np.asarray(y_true)
	y_pred_arr = np.asarray(y_pred)
	# Convert one-hot to class indices if needed
	if y_true_arr.ndim > 1:
		y_true_arr = np.argmax(y_true_arr, axis=1)
	if y_pred_arr.ndim > 1:
		y_pred_arr = np.argmax(y_pred_arr, axis=1)
	return confusion_matrix(y_true_arr, y_pred_arr)


def print_classification_report(y_true, y_pred, target_names=None):
	"""Prints sklearn classification report for given true/pred labels.

	target_names: optional list of class names (length must match number of classes).
	"""
	y_true_arr = np.asarray(y_true)
	y_pred_arr = np.asarray(y_pred)
	if y_true_arr.ndim > 1:
		y_true_arr = np.argmax(y_true_arr, axis=1)
	if y_pred_arr.ndim > 1:
		y_pred_arr = np.argmax(y_pred_arr, axis=1)
	print(classification_report(y_true_arr, y_pred_arr, target_names=target_names))