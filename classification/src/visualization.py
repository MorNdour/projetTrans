# Visualization utilities

import matplotlib.pyplot as plt
import sys
from pathlib import Path
project_root = Path.cwd().parent  
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import numpy as np
from PIL import Image
import seaborn as sns



def show_samples(folder: Path, ncols=4, max_classes=12):
    if not folder.exists():
        print('Folder not found:', folder)
        return
    class_dirs = [d for d in sorted(folder.iterdir()) if d.is_dir()]
    class_dirs = class_dirs[:max_classes]
    n = len(class_dirs)
    nrows = int(np.ceil(n / ncols))
    plt.figure(figsize=(4 * ncols, 4 * nrows))
    i = 1
    for d in class_dirs:
        imgs = list(d.glob('*'))
        if not imgs:
            continue
        img_path = imgs[0]
        try:
            img = Image.open(img_path).convert('RGB')
        except Exception as e:
            print('Could not open', img_path, e)
            continue
        plt.subplot(nrows, ncols, i)
        plt.imshow(img)
        plt.title(d.name)
        plt.axis('off')
        i += 1
    plt.tight_layout()

def plot_pixel_distribution(folder: Path, n_classes=12):
    """
    Plot pixel value histograms for a sample of images per class in the given folder.
    """
    n_per_class = 10  # images per class to sample
    bins = 32
    if not folder.exists():
        print('Folder not found:', folder)
        return
    class_dirs = [d for d in sorted(folder.iterdir()) if d.is_dir()][:n_classes]
    for d in class_dirs:
        imgs = list(d.glob('*'))[:n_per_class]
        pixels = []
        for p in imgs:
            try:
                img = Image.open(p).convert('RGB')
                arr = np.asarray(img).reshape(-1, 3)  # flatten spatial dims
                pixels.append(arr)
            except Exception:
                continue
        if not pixels:
            continue
        pixels = np.concatenate(pixels, axis=0)
        plt.figure(figsize=(12,3))
        for i, color in enumerate(['R', 'G', 'B']):
            plt.subplot(1,3,i+1)
            plt.hist(pixels[:,i], bins=bins, color=color.lower(), alpha=0.7)
            plt.title(f'{d.name} - {color}')
            plt.xlim(0,255)
        plt.suptitle(f'Pixel value distribution for class: {d.name}')
        plt.tight_layout()
        plt.show()

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')
    plt.subplot(1, 2, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()


def plot_confusion_matrix(cm, class_names=None):
    """
    Plot confusion matrix with counts.

    Args:
        cm (np.ndarray): confusion matrix from compute_confusion_matrix
        class_names (list): optional list of class labels
    """
    plt.figure(figsize=(6,5))
    
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",      # required for integer counts
        cmap="Blues",
        xticklabels=class_names,
        yticklabels=class_names
    )
    
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix")
    plt.show()