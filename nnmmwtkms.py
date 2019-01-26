from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy

numpy.random.seed(69) # set seed for reproducibility

train_x = []

for i in range(100000):
    train_x.append(numpy.random.randint(0,20,size=2)) # append lists of two random numbers to the values for train_x

train_y = []

for i in train_x:
    train_y.append(i[0] + i[1]) # append sums to train_y

train_y = numpy.array(train_y) # convert to array (I'm not sure why I need this but program broke when I removed it)
train_x = numpy.array(train_x) # ^^^

model = Sequential()
model.add(Dense(4, input_dim=2)) # input and first hidden layer
model.add(Activation('linear')) # linear activation because "infinite" range of answers
model.add(Dense(1)) # output layer with one answer neuron
model.add(Activation('linear'))
model.compile(optimizer='adam',loss='mse') # optimizer and loss
model.fit(train_x, train_y, validation_split=0.01, epochs=6) # train the model

model.save("model") # save it to a file called "model"