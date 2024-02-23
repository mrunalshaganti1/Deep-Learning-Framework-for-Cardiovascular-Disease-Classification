import numpy as np
import csv
import pandas as pd
df = pd.read_csv('cardioset.csv')
df["Smoker?"] = df["Smoker?"].map({'Smoker':1 ,'Non_Smoker':0})
df["Alcoholic?"] = df["Alcoholic?"].map({'Alcoholic':1 ,'Non_Alcoholic':0})
df["Diabetic?"] = df["Diabetic?"].map({'Diabetic':1 ,'Non_Diabetic':0})
df["Arrhythmiatic?"] = df["Arrhythmiatic?"].map({'Arrhythmiatic':1 ,'Non_Arrhythmiatic':0})
df["Exercise?"] = df["Exercise?"].map({'No_Exercise':1 ,'Exercise':0})
df["Stressful?"] = df["Stressful?"].map({'Stressful':1 ,'Non_Stressful':0})
df["Cholesterol"] = df["Cholesterol"].map({'Bad_Cholesterol':1 ,'Good_Cholesterol':0})
df["Sleep"] = df["Sleep"].map({'Irregular_Sleep':1 ,'Regular_Sleep':0})
df["Disease?"] = df["Disease?"].map({'CardioVascular_Disease':1 ,'No_CardioVascular_Disease':0})
heart_data = df[["Smoker?","Alcoholic?","Diabetic?","Arrhythmiatic?","Exercise?","Stressful?","Cholesterol","Sleep","Disease?"]].to_numpy()
feature_set = heart_data[:, [0,1,2,3,4,5,6,7]]
labels = heart_data[:, [8]]
np.random.seed(42)  
weights = np.random.rand(8,1)  
bias = np.random.rand(1)  
lr = 0.2
def sigmoid(x):  
    return 1/(1+np.exp(-x))
def sigmoid_der(x):  
    return sigmoid(x)*(1-sigmoid(x))
epoch = 1
x = 1
#print(weights,bias)
for epoch in range(2000):
#while (abs(x) > .001):  
    inputs = feature_set

    # feedforward step1
    XW = np.dot(feature_set, weights) + bias

    #feedforward step2
    z = sigmoid(XW)


    # backpropagation step 1
    error = z - labels
    x = error.sum()
    #print(epoch,x)

    # backpropagation step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz

    inputs = feature_set.T
    weights -= lr * np.dot(inputs, z_delta)

    for num in z_delta:
        bias -= lr * num
    #epoch = epoch + 1
print("Final adjusted weights are as follows:")
print(weights)
