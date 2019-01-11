from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from random import randint
import numpy as np


def build_model(num_layers):
    assert(num_layers > 0)
    model = Sequential()

    if (num_layers == 1):
        model.add(Dense(1, input_shape=(10,), activation='relu'))
        model.add(Dense(2, activation='softmax'))
    else:
        model.add(Dense(1024, input_shape=(10,), activation='relu'))
    
        for _ in range(num_layers - 2):
            model.add(Dense(1024, activation='relu'))

        model.add(Dense(2, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def get_data(num_samples):
    x, y = np.zeros(shape=(num_samples, 10), dtype=np.int), np.zeros(shape=(num_samples, 2), dtype=np.int)

    for i in range(num_samples):
        num = randint(0, 9)
        x[i, num] = 1
        y0 = 0, 1
        if num < 5:
            y0 = 0
        y[i, y0] = 1

    return x, y


def main():
    model = build_model(num_layers=1)
    x, y = get_data(num_samples=10000)
    model.fit(x, y, epochs=150, batch_size=128, verbose=2)


if __name__ == "__main__":
    main()