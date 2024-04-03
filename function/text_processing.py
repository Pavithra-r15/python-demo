import analyzer as a

def text_processing():
    while  True:
        user_input = input("Enter your text:")

        print("\nchoose an option : ")
        print('1. calculate the no.of.words in the user_input')
        print('2. calculate the no.of.character in the user_input')
        print('3. Rreverse the text in the user_input')
        print('4. Capitalize the text in the user_input')
        print('5. Exit the program')
        
        choose = input("enter the  number of option you want to perform:")

        if(choose == '1'):
            word_count = a.word_count(user_input)
            print("The word count of give text:  ",word_count)

        elif(choose == '2'):
            char_count = a.char_count(user_input)
            print("The char_count of given text:",char_count)
            
        elif(choose=='3'):
            capitalize = a.capital_text(user_input)
            print(f"The capitalized text  is : ",capitalize)

        elif(choose == '4'):
            reversed = a.reverse_text(user_input)
            print("The resversed text is:", reversed)

        elif(choose == '5'):
            print("exit the program")
        
        #if user enter any other than valid choice then it will show error message and ask for valid choice again.
        
        else:
            print("Enter a valid choice")
            break
        

text_processing()
                  

