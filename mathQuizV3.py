#Random math quiz (timed) +,-,*,/ Version 3
# By Casey Latimere Kreicar
#Import Random function
import random
import time
#start timer
startTimer = time.time()
#Set counter for percentage/total calculation of correct answers at the end of quiz
sum = 0
#Set counter for number of correct answers
numberOfCorrectAnswers = 0
#_____________________________________________________________________________________
#
#                                                               ADDITION for loop SECTION
#_____________________________________________________________________________________
#Create a variable for the loop
i = 0
#Initial for loop to set parameters so that the loop will run 5 times
for i in range (5):
    #Generate two single digit integers
    numberOne = random.randint(0,50)
    numberTwo = random.randint(0,50)
    #Variable i will cumulatively add 1 once each turn/iteration of the loop is executed
    i += 1
    #If the numberOne < numberTwo, swap them
    if numberOne < numberTwo:
        numberOne, numberTwo = numberTwo, numberOne
    #Print out of prompt for user to follow
    print("\n_________________________________\nSolve the following math problem: \n\n")
    #Equation for the user to solve
    answerToProblem = eval(input("What is "+ str(numberOne) + " + " + str(numberTwo) + " ? \n"))
#Check answerOne and display the result
    if numberOne + numberTwo == answerToProblem:
        print("\nYour answer is correct, please continue.")
        sum = sum + 1
        numberOfCorrectAnswers = numberOfCorrectAnswers  + 1
    else:
        print("\nYour answer is incorrect,  ", numberOne, ' + ', numberTwo, "=", numberOne + numberTwo , " please continue.")
#_____________________________________________________________________________________
#
#                                                             SUBTRACTION for loop SECTION
#_____________________________________________________________________________________
#Set counter for percentage/total calculation of correct answers at the end of quiz
sum = sum
#Set counter for number of correct answers
numberOfCorrectAnswers = numberOfCorrectAnswers 
#Create a variable for the loop
i = 0
#Initial for loop to set parameters so that the loop will run 5 times
for i in range (5):
    #Generate two single digit integers
    numberOne = random.randint(0,50)
    numberTwo = random.randint(0,50)
    #Variable i will cumulatively add 1 once each turn/iteration of the loop is executed
    i += 1
    #If the numberOne < numberTwo, swap them
    if numberOne < numberTwo:
        numberOne, numberTwo = numberTwo, numberOne
    #Print out of prompt for user to follow
    print("\n_________________________________\nSolve the following math problem: \n\n")
    #Equation for the user to solve
    answerToProblem = eval(input("What is "+ str(numberOne) + " - " + str(numberTwo) + " ? \n"))
#Check answerOne and display the result
    if numberOne - numberTwo == answerToProblem:
        print("\nYour answer is correct, please continue.")
        sum = sum + 1
        numberOfCorrectAnswers = numberOfCorrectAnswers  + 1
    else:
        print("\nYour answer is incorrect,  ", numberOne, ' - ', numberTwo, "=", numberOne - numberTwo , " please continue.")
#_____________________________________________________________________________________
#
#                                                             MULTIPLICATION for loop SECTION
#_____________________________________________________________________________________
#Set counter for percentage/total calculation of correct answers at the end of quiz
sum = sum
#Set counter for number of correct answers
numberOfCorrectAnswers = numberOfCorrectAnswers 
#Create a variable for the loop
i = 0
#Initial for loop to set parameters so that the loop will run 5 times
for i in range (5):
    #Generate two single digit integers
    numberOne = random.randint(0,12)
    numberTwo = random.randint(0,12)
    #Variable i will cumulatively add 1 once each turn/iteration of the loop is executed
    i += 1
    #If the numberOne < numberTwo, swap them
    if numberOne < numberTwo:
        numberOne, numberTwo = numberTwo, numberOne
    #Print out of prompt for user to follow
    print("\n_________________________________\nSolve the following math problem: \n\n")
    #Equation for the user to solve
    answerToProblem = eval(input("What is "+ str(numberOne) + " x " + str(numberTwo) + " ? \n"))
#Check answerOne and display the result
    if numberOne * numberTwo == answerToProblem:
        print("\nYour answer is correct, please continue.")
        sum = sum + 1
        numberOfCorrectAnswers = numberOfCorrectAnswers  + 1
    else:
        print("\nYour answer is incorrect,  ", numberOne, ' x ', numberTwo, "=", numberOne * numberTwo , " please continue.")
#_____________________________________________________________________________________
#
#                                                             DIVISION for loop SECTION
#_____________________________________________________________________________________
#Set counter for percentage/total calculation of correct answers at the end of quiz
sum = sum
#Set counter for number of correct answers
numberOfCorrectAnswers = numberOfCorrectAnswers 
#Create a variable for the loop
i = 0
#Initial for loop to set parameters so that the loop will run 5 times
for i in range (5):
    #Generate two single digit integers
    numberOne = random.randint(1,12)
    numberTwo = random.randint(0,144)
    #Variable i will cumulatively add 1 once each turn/iteration of the loop is executed
    i += 1
    #If the numberOne < numberTwo, swap them
    if numberOne < numberTwo:
        numberOne, numberTwo = numberTwo, numberOne
    #Print out of prompt for user to follow
    print("\n_________________________________\nSolve the following math problem (enter decimal point if necessary): \n\n")
    #Equation for the user to solve
    answerToProblem = eval(input("What is "+ str(numberOne) + " / " + str(numberTwo) + " ? \n"))
#Check answerOne and display the result
    if numberOne / numberTwo == answerToProblem:
        print("\nYour answer is correct, please continue.")
        sum = sum + 1
        numberOfCorrectAnswers = numberOfCorrectAnswers  + 1
    else:
        print("\nYour answer is incorrect,  ", numberOne, ' / ', numberTwo, "=", numberOne / numberTwo , " please continue.")
#_____________________________________________________________________________________
#
#                                                             Final score calculation
#_____________________________________________________________________________________
#end timer
endTimer = time.time()
#timer calculation
elapsedTime = (endTimer - startTimer)
#cleaner time output
cleanerElapsedTime = "{:.2f}" .format(elapsedTime)
#Set counter for percentage/total calculation of correct answers at the end of quiz
sum = sum
#Set counter for number of correct answers
numberOfCorrectAnswers = numberOfCorrectAnswers 
totalOfScore = sum / 20
finalScore = totalOfScore * 100
finalScoreFormatted = "{:.2f}" .format(finalScore) 
print("\n_________________________________\nYour score is ", finalScoreFormatted , "% out of 100 %")
if finalScore >= 90.0:
    grade = "A"
elif finalScore >= 80.0:
        grade = "B"
elif finalScore >= 70.0:
        grade = "C"
elif finalScore >= 60.0:
        grade = "D"
else:
    finalScore < 60.0
    grade = "F"
print("Grade: ", grade , "\nYou answered " , numberOfCorrectAnswers , " out of " , 20 , " questions correctly")
print("Elapsed Time (in seconds):", cleanerElapsedTime)
