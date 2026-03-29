
import cv2
import numpy as np
import albumentations as A

from torch.utils.data import Dataset

class TomatoDataset(Dataset):

    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):

        img = cv2.imread(self.image_paths[idx])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.transform:
            augmented = self.transform(image=img)
            img = augmented["image"]

        label = self.labels[idx]

        return img, label

def remove_background(image_path):
    """Removes background from an image using HSV color space 
    to isolate green areas."""
    
    image = cv2.imread(image_path)

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green range
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply mask
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Convert BGR → RGB for plotting
    # original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    return result_rgb


train_transform = A.Compose([
    A.Resize(256,256),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.Rotate(limit=40, p=0.7),
    A.RandomBrightnessContrast(p=0.5),
    A.GaussianBlur(p=0.2),
    # A.CoarseDropout(max_holes=8, max_height=20, max_width=20, p=0.3)
], seed=137)