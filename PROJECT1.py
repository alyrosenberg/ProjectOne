import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	readfile = open(file, 'r')
	content = readfile.readlines()
	firstline = content.pop(0)
	keys = firstline.strip().split(",")

	outputlist = []

	for line in content:
		currentline = line.strip().split(",")
		tempdic = {}
		for i, word in enumerate(currentline):
			tempdic[keys[i]] = word
		outputlist.append(tempdic)

	return outputlist

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sortedlist = sorted(data, key=lambda k: k[col])
	outputstring = "" + sortedlist[0]["First"] + " " + sortedlist[0]["Last"]
	return outputstring

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	classtallies = {"Freshman":0, "Sophomore":0, "Junior":0, "Senior":0}
	for student in data:
		classtallies[student["Class"]] += 1

	unsortedtuplist = [(k, v) for k, v in classtallies.items()]
	sortedtuplist = sorted(unsortedtuplist, key = lambda x: x[1], reverse=True)
	return sortedtuplist
	
# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	countdic = {}
	for student in a[1:]:
		month, dayofmonth, year = student["DOB"].split('/')
		dayofmonth = int(dayofmonth)
		if dayofmonth not in countdic:
			countdic[dayofmonth] = 1
		else:
			countdic[dayofmonth] += 1

	return max(countdic, key=lambda x: countdic[x])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	countdic = {num:0 for num in range(-100,100)}
	for student in a:
		datestring = student["DOB"]
		splitlist = datestring.split("/")
		age = int(2017) - int(splitlist[2])
		countdic[age] += 1
	total = 0
	count = 0
	for key in countdic.keys():
		count += countdic[key]
		total += key*countdic[key]
	return int(total/count)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	csv_file = open(fileName,'w')
	sortedlist = sorted(a, key=lambda k: k[col])
	#headers = list(a[0].keys())
	#csv_file.write(','.join(headers)+'\n')
	for student in sortedlist:
		vals = list(student.values())[:3]
		csv_file.write(','.join(vals)+ ',' +'\n')

	csv_file.close()

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()