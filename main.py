#SIMPLE CODE EXCERPT FROM LEX FRIDMAN

import tensorflow as tf
from tensorflow import keras

(train_images, train_labels), (test_images, test_labels) * \
keras.datasets.mnist.load_data()

model = keras.Sequential ([
	keras.layers.Flatten(input_shape=(28, 28)),
	keras.layers.Dense(128, activation=tf.nn.relu),
	keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
	Loss='sparse_cartegorical_corssentropy',
	metrics=['accauracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test accuracy:', test_acc)

predictions = model.predict(test_images)