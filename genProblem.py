#!/Users/ajeetganga/.pyenv/shims/python3

"""  Readme
You can configure following parameters. Given values are default.
author: ajeet.ganga.cs@gmail.com

problemsCount = 80
MinAbsNumber = -500
MaxAbsNumber = 500
# AllowedOperations = ['add', 'substract', 'multiply', 'divide']
operations = ['add', 'substract']
fractionInput = False
printTwoColumns = True

Requires numpy library installation.

Sample usage

""" 

import random
from numpy import arange

AllowedOperations = ['add', 'substract', 'multiply', 'divide']
ColWidth = 50
MaxWidth = 120

def getSymbolForOperation(operation):
	if operation == 'add':
		return ' + '
	if operation == 'substract':
		return ' - '
	if operation == 'multiply':
		return ' x '
	if operation == 'divide':
		return ' / '

def getQStringFromProblem(problem):
	if problem[3] < 0:
		y = "(" + str(problem[3]) + ")"
	else:
		y = str(problem[3])
	operation = getSymbolForOperation(problem[1])
	if isinstance(problem[2], int):
		operand1 = str(problem[2])
		if problem[3] < 0:
			operand2 = '(' + str(problem[3]) + ')'
		else:
			operand2 = str(problem[3])
	else:
		operand1 = '{0:.2f}'.format(problem[2])
		if problem[3] < 0:
			operand2 = '(' + '{0:.2f}'.format(problem[3]) + ')'
		else:
			operand2 = '{0:.2f}'.format(problem[3])
	
	s = " " + str(problem[0]) +  "] " + operand1 + operation + operand2 + " = "
	return 	s

def getAnswerString(problem):
	return str(problem[0]) + "] Answer is " + str(problem[4])

def printQuestions(problems, printTwoColumns):  
	problemsCount = len(problems)

	if printTwoColumns:
		for i in range(0, problemsCount, 2): 
			chArr = []
			for j in range(MaxWidth):
				chArr.append(" ")
			if i + 1 == problemsCount:
				s1 = getQStringFromProblem(problems[i])
				s2 = ""
			else:
				s1 = getQStringFromProblem(problems[i])
				s2 = getQStringFromProblem(problems[i+1])
			if(len(s1) > ColWidth):
				print("Column width exceeded error.")
				exit(1)
			for i in range(len(s1)):
				chArr[i] = s1[i]
			for i in range(len(s2)):
				chArr[i+ColWidth] = s2[i]
			print(''.join(chArr))
	else:
		for problem in problems:
			s = getQStringFromProblem(problem)
			print(s)

def printAnswers(problems, printTwoColumns): 
	problemsCount = len(problems)
	if printTwoColumns:
		for i in range(0, problemsCount, 2): 
			chArr = []
			for j in range(MaxWidth):
				chArr.append(" ")
			if i + 1 == problemsCount:
				s1 = getAnswerString(problems[i])
				s2 = ""
			else:
				s1 = getAnswerString(problems[i])
				s2 = getAnswerString(problems[i+1])
			if(len(s1) > ColWidth):
				print("Column width exceeded error.")
				exit(1)
			for i in range(len(s1)):
				chArr[i] = s1[i]
			for i in range(len(s2)):
				chArr[i+ColWidth] = s2[i]
			print(''.join(chArr))
	else:
		for problem in problems:
			s = getAnswerString(problem)
			print(s)

def main(operations, problemsCount, MinAbsNumber, MaxAbsNumber, fractionInput, printTwoColumns):
	problems = []
	inputRange = []
	if fractionInput: 
		inputRange = [i for i in arange(MinAbsNumber, MaxAbsNumber, 0.1)]
	else:
		inputRange =  [i for i in range(MinAbsNumber, MaxAbsNumber)]

	for i in range(problemsCount):

		operation = random.choice(operations) #todo getOperation() 
		x = random.choice(inputRange) 
		y = random.choice(inputRange) 

		if operation == 'add':
			z = x+y
			if not fractionInput:
				answer = str(z)
			else:
				answer = '{0:.2f}'.format(z)
		if operation == 'substract':
			z = x-y
			if not fractionInput:
				answer = str(z)
			else:
				answer = '{0:.2f}'.format(z)
		if operation == 'multiply':
			z = x*y
			if not fractionInput:
				answer = str(z)
			else:
				answer = '{0:.2f}'.format(z)
		if operation == 'divide':
			if (y == 0):
				z = 'undefined'
				answer = '{0:.2f}'.format(z)
			else:
				z = x/y 
				answer = '{0:.2f}'.format(z) 

		# 0  Problem number
		# 1  Operation
		# 2  First Operand
		# 3  Second Operand
		# 4  Answer
		problems.append([i+1, operation, x, y, answer])

	print(' Question sheet')
	printQuestions(problems, printTwoColumns)
	print("\n Answer sheet")
	printAnswers(problems, printTwoColumns)

# 96 for one page text
# 82 for one google doc page
problemsCount = 394 # fits on one page in google doc
MinAbsNumber = -20
MaxAbsNumber = +20
# operations = ['add', 'substract', 'multiply', 'divide']
operations = ['add', 'substract']
fractionInput = False
printTwoColumns = True
main(operations, problemsCount, MinAbsNumber, MaxAbsNumber, fractionInput, printTwoColumns)
