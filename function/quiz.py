def quiz():
    questions = [
        {"question": "What is the method used to read a content in the URL?\n a)get\n b)post \n c)update\n d)delete\n" , "answer":"a"},
        {"question": "Which of the following data types is mutable in Python?\n a)set\n b)list\n c)tuple\n d)dict\n", "answer": "b"},
        {"question": "What is the correct way to write a Python list? \n a)[]\n b)()\n c){} \n d) none\n", "answer": "a"},
        {"question": "Which data type is used to store a sequence of characters in Python? \n a)int\n b)string\n c)char \n d)float\n", "answer": "b"},
        {"question": "What is the index value of 6 in given series 1234567?\n a)6 \n b)5\n c)0\n d)1\n" , "answer": 'b'}
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
