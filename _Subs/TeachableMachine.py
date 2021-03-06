import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

import time

global model
    
def initMachine():
    global model
    model = tensorflow.keras.models.load_model(r'/Users/brianabouchard/Downloads/converted_keras (3)/keras_model.h5')
    return 1

def askMachine(path):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    result = prediction.tolist()
    return result
