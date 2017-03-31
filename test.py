import pandas as pd
import re

#Convert the array to a string and then use a find in python
def checkArrayElem(arr):
	df = pd.DataFrame(arr)
	x = df.to_string(header=False, index=False, index_names=False).split('\n')
	x = ''.join(x)
	if(x.find('134') >= 0):
		return True
	else:
        	return False 
#	vals = [','.join(ele.split()) for ele in x]
#	print(vals)

#Testing it 
assert checkArrayElem([1,2,3,4,1,4]) == False

assert checkArrayElem([1,2,1,3,4,1,4]) == True

