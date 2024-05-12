# class User:
#     def __init__(self,user_id,username):
        
#         self.id= user_id
#         self.username= username
#         self.followers=0
#         self.following=0
        
#     def follow(self,user):
#         user.followers+=1
#         self.following+=1
        
        
# user_1= User("002", "Ana")
# user_2= User("004","nicolas")

# print(user_1.username)
# print(user_2.id)
# user_1.username="naol"
# print(user_1.username)

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# user_2.follow(user_1)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# QUIZ PROJECT


# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# class Questions:
#     def __init__(self,q_text,q_answer):
#         self.text= q_text
#         self.answer= q_answer
        
# class Quizbrain:
#     def __init__(self, q_list):
#         self.q_numbers= 0
#         self.score=0
#         self.questions_list= q_list
        
#     def any_questions_left(self):
#         return self.q_numbers< len(self.questions_list)
    
#     def next_question(self):
#         current_question= self.questions_list[self.q_numbers]
#         self.q_numbers+=1
#         user_an= input(f"Q.{self.q_numbers}) {current_question.text} (True/False?) : ")
#         self.check_answer(user_an, current_question.answer)
    
#     def check_answer(self,user_answer, correct_answer):
#         if user_answer.lower()== correct_answer.lower():
#             self.score+=1
#             print("You got it right")
#         else:
#             print("That's wrong!")
        
#         print(f"The correct answer was {correct_answer}")
#         print(f"Your score is {self.score}/{self.q_numbers}")
#         print("\n")

# q_bank=[]   
# for questions in question_data:
#     question_text= questions["text"]
#     question_answer= questions["answer"]
#     new_questions= Questions(question_text,question_answer)
#     q_bank.append(new_questions)
    
# quiz= Quizbrain(q_bank)
# while quiz.any_questions_left():
#     quiz.next_question()

# print("You have completed the quiz!")
# print(f"Your final score was: {quiz.score}/{quiz.q_numbers}")
    
    
             
        
            
        
        



