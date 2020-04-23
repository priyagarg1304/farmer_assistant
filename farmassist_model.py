import pandas
import numpy as np

data = pandas.read_csv('crop_production.csv')
data = data.drop('Crop_Year', 1)
from sklearn.preprocessing import LabelEncoder



# encoding the strings to labels like 0,1,2...
le = LabelEncoder()

data['Crop'] = le.fit_transform(data['Crop'])
data['State_Name'] = le.fit_transform(data['State_Name'])
data['District_Name'] = le.fit_transform(data['District_Name'])
data['Season'] = le.fit_transform(data['Season'])
print(data)

import pandas
import numpy as np

data = pandas.read_csv('crop_production.csv')
data = data.drop('Crop_Year', 1)
from sklearn.preprocessing import LabelEncoder

crops = np.unique(data['Crop'])
states = np.unique(data['State_Name'])
districts = np.unique(data['District_Name'])

# encoding the strings to labels like 0,1,2...
le = LabelEncoder()

data['Crop'] = le.fit_transform(data['Crop'])
data['State_Name'] = le.fit_transform(data['State_Name'])
data['District_Name'] = le.fit_transform(data['District_Name'])
data['Season'] = le.fit_transform(data['Season'])
print(data)

import numpy as np

dat = np.array(data)
X = dat[:, 0:4]
X = np.array(X)

Y = dat[:, 5]
Y = np.array(Y)

# saving the changed output
Y1 = np.array(Y)

from sklearn import preprocessing

for i in range(Y.size):
    if Y[i] > 200000:
        Y1[i] = 4
    elif Y[i] > 100000 and Y[i] < 200000:
        Y1[i] = 3
    elif Y[i] > 10000:
        Y1[i] = 2
    else:
        Y1[i] = 1

print(Y1)

from sklearn.model_selection import train_test_split
#test and train data splitting
X_train, X_test, y_train, y_test = train_test_split( X, Y1, test_size=0.2, random_state=42)
print(len(X_train))

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
#model
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
filepath="C:\\Users\\sun\\Desktop\\proj1.h5"
checkpoint1= ModelCheckpoint(filepath,monitor='val_acc',verbose=1,save_best_only=True,mode='max')
callbacks_list=[checkpoint1]

model.fit(X_train, y_train, epochs=20, batch_size=100)
model.save("C:\\Users\\sun\\Desktop\\proj1.h5")
_, accuracy = model.evaluate(X_test, y_test)
print('Accuracy: %.2f' % (accuracy*100))
'''
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
'''