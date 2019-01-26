import keras.models
import numpy

model = keras.models.load_model("model")
for i in range(100):
    test = numpy.array([numpy.random.randint(0,20,size=2)])
    numbers = test[0][0]
    print(test)
    print(round(model.predict(test)[0][0]))