# # Task One: Create functions for each arithmetic operation.

def addition(*args):
    return sum(args)

sum = addition(90, 1000, 57, 80, 65)
print(f"Sum = {sum}")
print()

def subtract(*args):
    if not args:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        return subtract(args[0] - args[1], *args[2:])
diff = subtract(1,2,3,4,5)
print(f"Difference = {diff}")
print()

def multiplication(*args):
    if not args:
        return 0
    else:
        result = 1
        for arg in args:
            result *= arg
        return result
multi = multiplication(1,2,3,4,5)
print(f"Multiplication = {multi}")
print()

# # Task Two: Implement user input to receive numbers and an operation choice.

def user_addition1():
    total = 0
    a = 0
    while not a == -99:
        a = int(input("Enter a number or quit by entering -99: "))
        if a == -99: 
            continue
        else:
            total += a
    return total

result = user_addition1()
print(f"Sum = {result}")
print()

def multiplication1():
    total = 1
    a = 0
    while not a == -99:
        a = int(input("Enter a number or enter -99 to quit: "))
        if a == -99:
            continue
        else:
            total *= a
    return total

result = multiplication1()
print(f"Multiple = {result}")
print()
# # Task 3: Ensure your program can handle division by zero and other potential errors.
def division1():  
    a = 0
    total = int(input("Enter a number or enter -99 to quit: "))
    while total == 0:
        total = int(input("Enter a non-zero number or enter -99 to quit: "))
    
    while not a == -99: 
        a = int(input("Enter a number or enter -99 to quit: "))
        while a == 0:
            a = int(input("Enter a non-zero number or enter -99 to quit: "))
        if a == -99:
            continue
        else:
            total /= a
    return total

result = division1()
print(f"Division = {result:.2f}".format(result = result))
print()

# The Shopping List Maker
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

def shoppingList():
    addItemsList = []
    while addItemsList == [] or len(addItemsList) < 5:
        item = input("Enter item: ")
        addItemsList.append(item)
    return addItemsList
listOfItems = shoppingList()
print()

def removeItem():
    print(listOfItems)
    for item in listOfItems.copy():
        removeItem = input(f"Remove item from list or input 'exit': ")
        if removeItem == "exit" or len(listOfItems) == 0:
            break
        else:
            listOfItems.remove(removeItem)
    return listOfItems
print(f"List After Removal: {removeItem()}")
print()

def formatSL():
    newList = []
    newList = [item.title() for item in listOfItems]
    return newList
print(f"Formatted List: {formatSL()}")
print()

# The Grade Analyzer
# Task 1: Code a function to calculate the average grade
# Task 2: Implement a function to find the highest and lowest grade
# Task 3: Create a feature that catgeorizes grades into letter grades (A,B,C, etc.)

def calculateGrade():
    total = 0.0
    counter = 0.0
    average = 0.0
    grade = 0.0
    gradeList = []
    while gradeList == [] or not grade == -99:
        if grade == -99:
            break
        else:
            counter = counter + 1
            total += grade
            average = total / counter
            grade = float(input("Enter grade as decimal or -99 to quit: "))
            if not grade == -99:
                gradeList.append(grade)
            average = "{:.2f}".format(average)
    print("Average Grade:", average)
    return gradeList

listOfGrades = calculateGrade()

def findGrade():
    listOfGrades.sort()
    lowest = listOfGrades[0]
    greatest = listOfGrades[-1]
    print(f"Highest Grade: {greatest}")
    print(f"Lowest Grade: {lowest}")

findGrade()

def categorizeGrades():
    newGradeList = []
    for grade in listOfGrades:
        if grade >= 90:
            gradeL = 'A'
        elif grade < 90 and grade >= 80:
            gradeL = 'B'
        elif grade < 80 and grade >= 70:
            gradeL = 'C'
        elif grade < 70 and grade >= 60:
            gradeL = 'D'   
        else: 
            gradeL = 'F'
        newGradeList.append(gradeL)
    print("Original Grades: ", listOfGrades)
    return newGradeList
print("Letter Grades: ", categorizeGrades())

# The Quiz Game
# Task 1: Develop a list of questions and answers
# Task 2: Write a function that quizzes the user and takes their answers
# Task 3: Score the quiz and give the user feeback on their performance

questions = ["True or False: There are 5 continents.", "How many (interger) countries are there in Africa?",
"True or False: Flying is more dangerous than driving.", 
"True or False: The University of Chicago is #10 in the nation."]
answers = ["False", "54", "False", "False"]
def quizGame():
    ansList = []
    for i in range(len(questions)):
        userAns = input(f"{questions[i]} ").title()
        ansList.append(userAns)
        correct = 0
    for i in range(len(answers)):
        if answers[i] == ansList[i]:
            correct = correct + 1
            feedback = correct/len(answers) * 100
    print(f"User received: {feedback}%")
    print(f"Correct Answers: {answers}")
    
quizGame()
    
# The Fitness Tracker
# Task 1: Develop a function to log different fitness activities and their duration
# For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15]
# where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and 
# Biking corresponds to 15 minutes.
# Task 2: Write a simple function that estimates calories burned based on the activity and 
# duration. For instance, Total calories burned = Duration in minutes *3.5
# Task 3: Create a summary function that provides a report of all 
# activities and total calories burned for the day.

def activityLog():
    activity = []
    while activity == [] or len(activity) < 5:
        sport = input("Today's activity or exit: ")
        if sport == "exit":
            break
        else:
            activity.append(sport)
    print(f"Activities: {activity}")
    return activity
activityItems = activityLog()
print()

def durationLog():
    duration = []
    while duration == [] or len(duration) <= len(activityItems):
        time = float(input("Time Elapsed (in minutes): "))    
        duration.append(float(time))
    print(f"Duration: {duration}")
    return duration
durationItems = durationLog()
print()

def calBurned():
    calBurned = []
    for i in range(len(durationItems)):
        calBurned.append(durationItems[i] * 3.5)
    return calBurned
print("Calories Burned: ", calBurned())
print()

def summaryFit():
    title = "USER SUMMARY".center(60)
    print(title)
    print("User's activities: ", activityItems)
    print("User's Time Spent Per Activity: ", durationItems)
    print("Calories Burned: ", calBurned())

summaryFit()
print()






 








