import pandas as pd
import math

class KNNClassifier:
    
  train_data = [] # array of triplets <a, b, actual value>

  def input_train_data(self, train_a, train_b, train_y):
    for i in range(len(train_a)):
        self.train_data.append((train_a[i], train_b[i], train_y[i]))

  def calc_distance(self, test_a, test_b):
    ret = [] # array of pairs <distances, actual value>

    # complete code
    # for i in range(self.train_data)
    for train_a, train_b, train_y in self.train_data:
      distance = math.sqrt(math.pow(train_a - test_a, 2) +
        math.pow(train_b - test_b, 2))
      ret.append((distance, train_y))

    return ret

  def classify(self, all_distances, K):
    all_distances.sort()

    # complete code
    results = {}
    for i in range(K):
      desc = all_distances[i]
      if not desc[1] in results:
        results[desc[1]] = 0
      results[desc[1]] = results[desc[1]] + 1

    # x flower : 5
    maxNumber = -100
    maxName = ""

    for name, num in results.items():
      if num > maxNumber:
        maxName = name
        maxNumber = num

    return maxName

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

test_a = 2.5
test_b = 0.75
all_distance = knn.calc_distance(test_a, test_b)

pred = knn.classify(all_distance, 3)
print(pred)