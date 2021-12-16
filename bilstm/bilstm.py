import numpy as np
from keras.preprocessing import sequence
from keras.layers import Dense, LSTM, Bidirectional
from keras.models import Sequential
from gensim.models import Word2Vec
from tensorflow.keras.utils import to_categorical
import os
from utils_334 import train_test_split_1
import tensorflow as tf
from tensorflow.python.keras import backend as K
import tensorflow as tf
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)
K.set_session(sess)


def word_embeddings(train, test, train_label, test_label):
	train_embed = []
	test_embed = []
	for x in train:
		to_add = []
		for line in x.split("\n"):
			if line == "":
				continue
			to_add += line.strip().split(" ")
		train_embed.append(to_add)
	for x in test:
		to_add = []
		for line in x.split("\n"):
			if line == "":
				continue
			to_add += line.strip().split(" ")
		test_embed.append(to_add)
	
	# Read train and test files and return word embeddings
	model = Word2Vec((train_embed + test_embed)[500], vector_size = 50, window = 3, min_count = 1, workers = 3, sg  = 1)
	for i in [train_embed, test_embed]:
		for l in i:
			for k in range(len(l)):
				try:
					l[k] = model.wv[l[k]]
				except:
					l[k] = [0.0 for x in range(50)]
	return train_embed, test_embed, train_label, test_label


def main():

	os.environ["CUDA_VISIBLE_DEVICES"]="3"
	#gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
	#tf.config.experimental.set_visible_devices(devices=gpus[0], device_type='GPU')
	#tf.config.experimental.set_memory_growth(device=gpus[0], enable=True)
	# get train and test split of python files
	train, test, train_label, test_label = train_test_split_1()
	# word embedding features
	train, test, train_label, test_label = word_embeddings(train, test, train_label, test_label)
	train_label = np.array(to_categorical(train_label, 2))
	test_label = np.array(to_categorical(test_label, 2))
	train = sequence.pad_sequences(train, maxlen = 100)
	test = sequence.pad_sequences(test, maxlen = 100)
	train = np.array(train)
	test = np.array(test)
	model = Sequential()
	model.add(Bidirectional(LSTM(2, return_sequences=False, stateful=True), batch_input_shape=(1, train.shape[1], train.shape[2])))
	model.add(Dense(2, activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
	model.fit(train, train_label, batch_size=1, epochs=15, verbose=1)
	print(model.summary())
	score = model.evaluate(test, test_label, batch_size=1, verbose=1)
	pred = model.predict(test, batch_size=1, verbose=1)
	b = np.argmax(pred, axis=1)
	accuracy = np.mean(b == np.argmax(test_label, axis=1))
	print(pred)
	print(accuracy)
	print("Accuracy: ", score[1])

if __name__ == '__main__':
	main()