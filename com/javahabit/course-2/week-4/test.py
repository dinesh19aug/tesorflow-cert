#Testing a csv file read
import csv
import numpy as np

with open('sample.csv') as training_file:
    csvreader = csv.reader(training_file)
    next(csvreader)
    part = np.empty(0)
    values = []
    for row in csvreader:
        part=np.append(part, row[0])
        rowValues=row[1:10]
        splitRowValues= np.array_split(rowValues,3)
        list.append(values,splitRowValues)


    print(part.shape)
    values = np.array(values).astype('float')
    print(values)

# [
# [[1,2,3],[4,5,6],[7,8,9]],
# [[1,2,3],[4,5,6],[7,8,9]]
# ]
#x=[1,2,3,4,5,6,7,8,9]
#a= np.array(np.array_split(x,3))
#z=[a,a]
#np.array(z).shape