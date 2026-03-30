# Training script
import tensorflow as tf

from classification.config import (
    BATCH_SIZE, IMAGE_SIZE, CHANNELS, EPOCHS, N_CLASSES,
    TRAIN_DIR, VAL_DIR, MODEL_SAVE_PATH,
)
from classification.models.cnn import build_cnn
from classification.src.dataloader import load_data


def train():
    train_dataset = load_data(TRAIN_DIR, IMAGE_SIZE, BATCH_SIZE)
    val_dataset = load_data(VAL_DIR, IMAGE_SIZE, BATCH_SIZE)

    input_shape = (IMAGE_SIZE, IMAGE_SIZE, CHANNELS)
    model = build_cnn(input_shape, N_CLASSES)

    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        metrics=['accuracy'],
    )

    model.fit(train_dataset, validation_data=val_dataset, epochs=EPOCHS)
    model.save(MODEL_SAVE_PATH)
    return model


def split_data(dataset, train_split=0.8, shuffle=True):
    dataset_size = len(dataset)

    if shuffle:
        dataset = dataset.shuffle(dataset_size, seed=12)

    train_size = int(train_split * dataset_size)

    train_dataset = dataset.take(train_size)
    val_dataset = dataset.skip(train_size)

    return train_dataset, val_dataset