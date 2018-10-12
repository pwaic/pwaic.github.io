import pandas as pd
import math

class KNNClassifier:
    
    train_data = [] # array of triplets <a, b, actual value>

    def input_train_data(self, train_a, train_b, train_y):
        for i in range(len(train_a)):
            self.train_data.append((train_a[i], train_b[i], train_y[i]))

    def calc_distance(self, a, b):
        ret = [] # array of pairs <distances, actual value>

        # complete code
        

    def classify(self, test_a, test_b):
        distances = self.calc_distance(test_a, test_b).sort()

        # complete code
    
        

if __name__ == '__main__':

    # load data
    all_data = pd.read_csv('Iris_Data.csv')
    petal_length = all_data['petal_length'].values.tolist()
    petal_width = all_data['petal_width'].values.tolist()
    labels = all_data['species'].values.tolist()

    # check on the data (make sure it's correct)
    print(petal_length)
    print(petal_width)
    print(labels)

    # instantiate KNN classifier
    knn = KNNClassifier()
    knn.input_train_data(petal_length, petal_width, labels)
    print(knn.train_data)