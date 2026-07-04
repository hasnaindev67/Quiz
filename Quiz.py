import random

print("===== WELCOME TO QUIZ =====")

print("\n")

#Creating Questions

question1 = {
    "question": "What is the capital of Pakistan?",
    "options": ["A. Karachi", "B. Islamabad", "C. Lahore"],
    "answer": "B"
}

question2 = {
    "question": "Which function is used to take user input?",
    "options": ["A. def", "B. str", "C. input"],
    "answer": "C"
}

question3 = {
    "question": "What is 5 + 7?",
    "options": ["A. 10", "B. 12", "C. 13"],
    "answer": "B"
}

question4 = {
    "question": "What is HTML used for?",
    "options": ["A. Designing games", "B. Creating web pages", "C. App development"],
    "answer": "B"
}

question5 = {
    "question": "When was Python first released?",
    "options": ["A. 1974", "B. 1985", "C. 1991"],
    "answer": "C"
}

question6 = {
    "question": "Which keyword is used to define a function?",
    "options": ["A. function", "B. def", "C. fun"],
    "answer": "B"
}

question7 = {
    "question": "Which symbol is used for comments in Python?",
    "options": ["A. //", "B. #", "C. /*"],
    "answer": "B"
}

question8 = {
    "question": "Which data type stores whole numbers?",
    "options": ["A. int", "B. float", "C. str"],
    "answer": "A"
}

question9 = {
    "question": "What is 10 × 5?",
    "options": ["A. 50", "B. 40", "C. 60"],
    "answer": "A"
}

question10 = {
    "question": "Which loop repeats while a condition is true?",
    "options": ["A. for", "B. while", "C. if"],
    "answer": "B"
}

question11 = {
    "question": "Which keyword is used for conditions?",
    "options": ["A. if", "B. for", "C. while"],
    "answer": "A"
}

question12 = {
    "question": "What is the extension of Python files?",
    "options": ["A. .py", "B. .java", "C. .html"],
    "answer": "A"
}

question13 = {
    "question": "Which operator is used for addition?",
    "options": ["A. +", "B. *", "C. /"],
    "answer": "A"
}

question14 = {
    "question": "What is 20 - 8?",
    "options": ["A. 10", "B. 12", "C. 14"],
    "answer": "B"
}

question15 = {
    "question": "Which keyword creates a class?",
    "options": ["A. object", "B. class", "C. define"],
    "answer": "B"
}

question16 = {
    "question": "Which function displays output?",
    "options": ["A. show()", "B. print()", "C. display()"],
    "answer": "B"
}

question17 = {
    "question": "What is 9 × 9?",
    "options": ["A. 81", "B. 72", "C. 99"],
    "answer": "A"
}

question18 = {
    "question": "Which collection uses square brackets []?",
    "options": ["A. Tuple", "B. List", "C. Dictionary"],
    "answer": "B"
}

question19 = {
    "question": "Which collection uses curly braces {} with key-value pairs?",
    "options": ["A. Dictionary", "B. List", "C. Tuple"],
    "answer": "A"
}

question20 = {
    "question": "Which keyword exits a loop?",
    "options": ["A. stop", "B. break", "C. continue"],
    "answer": "B"
}

question21 = {
    "question": "What is 100 ÷ 10?",
    "options": ["A. 20", "B. 5", "C. 10"],
    "answer": "C"
}

question22 = {
    "question": "Which function finds the length of a list?",
    "options": ["A. count()", "B. len()", "C. size()"],
    "answer": "B"
}

question23 = {
    "question": "Which keyword is used to import a module?",
    "options": ["A. include", "B. import", "C. using"],
    "answer": "B"
}

question24 = {
    "question": "What is CSS used for?",
    "options": ["A. Styling web pages", "B. Database", "C. Programming"],
    "answer": "A"
}

question25 = {
    "question": "Which language is used to make web pages interactive?",
    "options": ["A. HTML", "B. CSS", "C. JavaScript"],
    "answer": "C"
}

question26 = {
    "question": "What is 15 + 15?",
    "options": ["A. 20", "B. 30", "C. 35"],
    "answer": "B"
}

question27 = {
    "question": "Which symbol is used for multiplication?",
    "options": ["A. x", "B. *", "C. #"],
    "answer": "B"
}

question28 = {
    "question": "Which function converts text to integer?",
    "options": ["A. str()", "B. float()", "C. int()"],
    "answer": "C"
}

question29 = {
    "question": "Which loop is commonly used to iterate over a list?",
    "options": ["A. for", "B. if", "C. else"],
    "answer": "A"
}

question30 = {
    "question": "What is 49 ÷ 7?",
    "options": ["A. 8", "B. 7", "C. 9"],
    "answer": "B"
}

question31 = {
    "question": "Which keyword is used to create an object?",
    "options": ["A. new", "B. class", "C. No keyword"],
    "answer": "C"
}

question32 = {
    "question": "Which operator checks equality?",
    "options": ["A. =", "B. ==", "C. !="],
    "answer": "B"
}

question33 = {
    "question": "What is 14 + 6?",
    "options": ["A. 18", "B. 20", "C. 22"],
    "answer": "B"
}

question34 = {
    "question": "Which function converts text to lowercase?",
    "options": ["A. lower()", "B. small()", "C. down()"],
    "answer": "A"
}

question35 = {
    "question": "Which keyword defines inheritance?",
    "options": ["A. extends", "B. class", "C. Parent class in brackets"],
    "answer": "C"
}

question36 = {
    "question": "Which data type stores decimal numbers?",
    "options": ["A. int", "B. float", "C. bool"],
    "answer": "B"
}

question37 = {
    "question": "What is 18 × 2?",
    "options": ["A. 36", "B. 32", "C. 40"],
    "answer": "A"
}

question38 = {
    "question": "Which keyword skips the current loop iteration?",
    "options": ["A. continue", "B. break", "C. stop"],
    "answer": "A"
}

question39 = {
    "question": "Which keyword defines a constructor?",
    "options": ["A. init()", "B. __init__", "C. constructor"],
    "answer": "B"
}

question40 = {
    "question": "What is 81 ÷ 9?",
    "options": ["A. 8", "B. 9", "C. 10"],
    "answer": "B"
}

question41 = {
    "question": "Which function converts text to uppercase?",
    "options": ["A. upper()", "B. capital()", "C. big()"],
    "answer": "A"
}

question42 = {
    "question": "Which value represents False?",
    "options": ["A. 1", "B. 0", "C. True"],
    "answer": "B"
}

question43 = {
    "question": "What is 11 + 22?",
    "options": ["A. 33", "B. 32", "C. 34"],
    "answer": "A"
}

question44 = {
    "question": "Which operator means 'not equal'?",
    "options": ["A. !=", "B. ==", "C. ="],
    "answer": "A"
}

question45 = {
    "question": "Which keyword returns a value from a function?",
    "options": ["A. print", "B. return", "C. break"],
    "answer": "B"
}

question46 = {
    "question": "What is 64 ÷ 8?",
    "options": ["A. 6", "B. 8", "C. 10"],
    "answer": "B"
}

question47 = {
    "question": "Which keyword is used to handle exceptions?",
    "options": ["A. catch", "B. try", "C. error"],
    "answer": "B"
}

question48 = {
    "question": "Which keyword handles an exception?",
    "options": ["A. except", "B. catch", "C. finally"],
    "answer": "A"
}

question49 = {
    "question": "What is 7 × 8?",
    "options": ["A. 54", "B. 56", "C. 58"],
    "answer": "B"
}

question50 = {
    "question": "Python is a ______ language.",
    "options": ["A. Programming", "B. Markup", "C. Database"],
    "answer": "A"
}

#Storing questins in list

quiz = [
    question1, question2, question3, question4, question5,
    question6, question7, question8, question9, question10,
    question11, question12, question13, question14, question15,
    question16, question17, question18, question19, question20,
    question21, question22, question23, question24, question25,
    question26, question27, question28, question29, question30,
    question31, question32, question33, question34, question35,
    question36, question37, question38, question39, question40,
    question41, question42, question43, question44, question45,
    question46, question47, question48, question49, question50
]

quiz = random.sample(quiz, 5)        #list me se koi bhi 5 random questions deta he

score = 0

for question in quiz:
    print("\n" + question["question"])          #question print krta he list me se

    for option in question["options"]:          #question k options print krta he
        print(option)

    user_answer = input("Enter your answer: ").upper()   #user se answer k liye input leta he ager answer B he or user small b likhe to automatically capital ho jaye ga

    if user_answer == question["answer"]:          #ager user ka answer coreect ho to score + hoty han or ager correct naho to +nai hota
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer is:", question["answer"])    #ager user ghalat answer dy to nicy correct answer print ho jata he

print("\nTotal score:", score)     #last me total score print ho jaty han k 5 questions me se user ne kitny correct kiye

while True:                #yahan loop is liye use hoi he k ager user chahe to quiz again bhi khel sakta he jab tak condition true ho tab tak chalti rahy
    choice = input("Would you like to play again? (Y/N): ").lower()
    if choice == "y":                    #choice y hoi to again start ho jaye gi quiz
        continue
    elif choice == "n":                  #choice n hoi to break ho jaye gi loop
        print("Thank you for playing!")
        break
    else:             #y ya n k ilawa koi choice dy to invalid choice aye
        print("Invalid  Choice")

