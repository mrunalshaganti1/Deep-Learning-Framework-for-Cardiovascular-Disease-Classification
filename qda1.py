from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import numpy as np
import pandas as pd
from sklearn import *
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.metrics import accuracy_score
df = pd.read_csv('cardioset3.csv')
df["Smoker?"] = df["Smoker?"].map({'ChainSmoker':5 ,'MoreThanThreeTimesDaily':4,'ThreeTimesDaily':3 ,'LessThanThreeTimesDaily':2,'DoesNotSmoke':1})
df["Alcoholic?"] = df["Alcoholic?"].map({'DrinksDaily':5 ,'MoreThanThriceAwek':4,'ThriceAwek':3 ,'LessThanThriceAwek':2,'DoesNotDrink':1})
df["Diabetic?"] = df["Diabetic?"].map({'SevereType1Diabetis':5 ,'Type1Diabetis':4,'SevereType2Diabetis':3 ,'Type2Diabetis':2,'NoDiabetis':1})
df["Arrhythmiatic?"] = df["Arrhythmiatic?"].map({'StronglyIrregularBeat':5 ,'HighlyIrregularBeat':4,'MediumIrregularBeat':3 ,'LowIrregularBeat':2,'RegularHeartBeat':1})
df["Exercise?"] = df["Exercise?"].map({'NoExercise':5 ,'Around1hrPerWeek':4,'Around3hrsPerWeek':3 ,'Around5hrsPerWeek':2,'Around7hrsPerWeek':1})
df["Stressful?"] = df["Stressful?"].map({'SevereStressfulLifestyle':5 ,'HighlyStressfulLifestyle':4,'MildlyStressfulLifestyle':3 ,'LessRelaxedLifestyle':2,'RelaxedLifestyle':1})
df["Cholesterol"] = df["Cholesterol"].map({'Morethan240':5 ,'Around240':4,'InBetween200to239':3 ,'Around200':2,'LessThan200':1})
df["Sleep"] = df["Sleep"].map({'Lessthan4hours':5 ,'MoreThan9hours':4,'Around9hours':3 ,'Around8hours':2,'Around7hours':1})
data = df[["Smoker?","Alcoholic?","Diabetic?","Arrhythmiatic?","Exercise?","Stressful?","Cholesterol","Sleep","Percentage"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = QuadraticDiscriminantAnalysis()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of QDA Classifier on testing data is: " + str(accuracy))
testSet = [[3,4,2,3,3,5,3,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDA percentage prediction on the first test set is:',predictions)
testSet = [[4,3,3,4,5,2,5,5]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDA percentage prediction on the second test set is:',predictions)
testSet = [[1,3,5,4,2,1,3,2]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDA percentage prediction on the third test set is:',predictions)
