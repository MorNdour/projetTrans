# Training script
from raspberry_task.src.dataloader import load_data
from src.models.cnn import build_cnn

import tensorflow as tf

BATCH_SIZE = 32
IMAGE_SIZE = 256
CHANNELS = 3
EPOCHS = 31
N_CLASSES = 10  # Update as needed

train_dir = '../data/train'
val_dir = '../data/val'

train_dataset = load_data(train_dir, IMAGE_SIZE, BATCH_SIZE)
val_dataset = load_data(val_dir, IMAGE_SIZE, BATCH_SIZE)

input_shape = (IMAGE_SIZE, IMAGE_SIZE, CHANNELS)
model = build_cnn(input_shape, N_CLASSES)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

model.fit(train_dataset,
          validation_data=val_dataset,
          epochs=EPOCHS)

model.save('../cnn_model_save.h5')
