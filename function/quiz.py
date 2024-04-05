def quiz():
    questions = [
        {"question": "What is the method used to read a content in the URL?", "answer":"get"},
        {"question": "Which of the following data types is mutable in Python?", "answer": "list"},
        {"question": "What is the correct way to write a Python list", "answer": "[1, 2, 3]"},
        {"question": "Which data type is used to store a sequence of characters in Python?", "answer": "string"},
        {"question": "What is the index value of 6 in given series 1234567?", "answer": '5'}
    ]
    
    score = 0
    
    for question in questions:
        print(question["question"])
        answer = input("Your answer: ")
        question_answer = question["answer"]
        if answer == question_answer:
            print("HURRAY!!Correct!")
            score += 1
        else:
            print("OPS!!Wrong!")
    
    print(f"Quiz complete! You scored {score} out of {len(questions)}")

quiz()
