# import train_test_split from sklearn
from sklearn.model_selection import train_test_split
import os

def train_test_split_1(random_state=1):
	"""
	Split data into train and test sets.
	"""
	curr_dur = os.getcwd()
	good_python = "good_python_files"
	bad_python = "bad_python_files"
	good_python_files = os.listdir(os.path.join(curr_dur, good_python))
	bad_python_files = os.listdir(os.path.join(curr_dur, bad_python))
	# get train and test split of python files
	good_train, good_test = train_test_split(good_python_files, test_size=0.2, random_state=random_state)
	bad_train, bad_test = train_test_split(bad_python_files, test_size=0.2, random_state=random_state)
	train_label = [1] * len(good_train) + [0] * len(bad_train)
	test_label = [1] * len(good_test) + [0] * len(bad_test)
	return good_train + bad_train, good_test + bad_test, train_label, test_label