from quiz_questions import *
from random import *
class quiz:
    def __init__(self):
       
        self.show_question()
        self.check_que()
    
    def show_question(self):
        self.random_num = randint(0,200)
        print(quiz_questions[self.random_num]["question"])
        
        
    def check_que(self):
        
        ans = input("Write true or false : ")
        
        if ans == (quiz_questions[self.random_num]["answer"]).lower():
            print("Hey You got if Right!!!")
            self.play_again()
        else : 
            print("You got it wrong")
            self.play_again()
    
    def play_again(self):
        choice = input("if you want to stop type exit :  ").lower()
        if choice == "exit":
            pass
            
        else: 
            self.show_question()
            self.check_que()
                
a = quiz()
