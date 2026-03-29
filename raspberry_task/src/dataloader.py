# Data loading and preprocessing utilities

def load_data(data_dir, image_size, batch_size):
    import tensorflow as tf
    return tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        seed=123,
        shuffle=True,
        image_size=(image_size, image_size),
        batch_size=batch_size
    )
