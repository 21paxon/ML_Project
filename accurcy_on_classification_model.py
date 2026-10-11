from sklearn.metrics import  accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
actual =[0,0,1,1,1]
predicted =[0,0,1,0,1]

accuracy_score=accuracy_score(actual,predicted)
print("Accuracy of the classification model is:", accuracy_score)


#confusion matrix

actual = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
predicted = [0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
print("The confusion matrix is:")
print(confusion_matrix(actual, predicted))



actual =    [0, 0, 0, 0, 1, 1, 1, 1]
predicted = [0, 0, 0, 1, 1, 1, 0, 1]
print("The classification report is:")
print(classification_report(actual, predicted))