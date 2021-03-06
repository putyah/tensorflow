# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1.0, 2.0, 3.0, 5.0, 7.0], dtype=float)
ys = np.array([1.0, 1.5, 2.0, 3.0, 4.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([9.0]))
