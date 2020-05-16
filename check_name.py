from knn import *
import math
import csv

def readCsv():
	file = open('data.csv')
	data = csv.reader(file)
	next(data, None)
	return [[float(x), float(y)] for x, y in data]

def toNumber(string):
	number = [ord(x) for x in string.lower()]
	number = [x * (math.sqrt(i) + math.pi) for i, x in enumerate(number)]
	return sum(number) / len(number)

if __name__ == "__main__":
	dataset = readCsv()
	while True:
		name = input("Name: ")
		prediction = predict_classification(dataset, [toNumber(name),None], 3)
		print("Prediction: " + ("Valid" if prediction == 1 and name.isalpha() else "Not Valid") + "\n")