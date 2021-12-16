from sklearn.metrics import accuracy_score
from utils import train_test_split_1
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

def extract_tfidf(train, test):
	tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0)
	train = tf.fit_transform(train)
	test = tf.transform(test)
	return train, test


def main():
	# get train and test split of python files
	train, test, train_label, test_label = train_test_split_1()
	# tfidf features
	train, test = extract_tfidf(train, test)
	models = [LogisticRegression(), Perceptron(penalty = "l2"), RandomForestClassifier(), AdaBoostClassifier(), KNeighborsClassifier()]
	for model in models:
		# fit model
		model.fit(train, train_label)
		# predict labels
		predictions = model.predict(test)
		# print accuracy
		print(f"Accuracy for {model}: ", accuracy_score(test_label, predictions))



if __name__ == "__main__":
	main()