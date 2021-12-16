# import train_test_split from sklearn
from sklearn.model_selection import train_test_split
import pandas as pd
import os

def train_test_split_1(random_state=0):
	"""
	Split data into train and test sets.
	"""
	df = pd.read_csv("../good2.csv", delimiter="|")
	df.head()
	df = df[df['label'].notna()]
	df = df[df['text'].notna()]
	# get train and test split of python files
	train_text, test_text, train_labels, test_labels = train_test_split(df['text'], df['label'],
                                                                    test_size=0.2,
                                                                    stratify=df['label'])
	return train_text.to_numpy(), test_text.to_numpy(), train_labels.to_numpy(), test_labels.to_numpy()