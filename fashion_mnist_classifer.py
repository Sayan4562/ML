# -*- coding: utf-8 -*-
"""Fashion_mnist_classifer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IsqBXN2oDM8V1Hv-3LEVHH8gR6lmme6F
"""

import tensorflow as tf
from tensorflow import keras
fashion_mnist=keras.datasets.fashion_mnist
(train_image,train_labels),(test_image,test_labels)=fashion_mnist.load_data()

import matplotlib.pyplot as plt
plt.imshow(train_image[0])

train_image=train_image/255.0
test_image=test_image/255.0

from keras.api._v2.keras import activations
model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation=tf.nn.relu),
    tf.keras.layers.Dense(10,activation=tf.nn.softmax)
])


model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])


model.fit(train_image,train_labels,epochs=70)

model.evaluate(test_image,test_labels)

# how save a model

import pickle
pickle.dump(model, open('model.pkl', 'wb'))

# how lode a sve model

import pickle
pickel_model=pickle.load(open("model.pkl","rb"))
pickel_model.predict(test_image)

