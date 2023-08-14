# list of questions
quizQuestions= [{'Question':'The series Friends is set in which city?','Choices':['A. Los Angeles', 'B. New York City', 'C. Miami', 'D. Seattle'], 'Answer': 'B'}, {'Question':'What was the name of the monkey that Ross owned?','Choices':['A. Keith', 'B. Lancelot', 'C. Marcel', 'D. Alistair'], 'Answer': 'C'}, {'Question':'What’s the name of Joey’s penguin?','Choices':['A. Snowflake', 'B. Waddle', 'C. Huggsy', 'D. Bobber'], 'Answer': 'C'}, {'Question':'What is Chandler’s middle name?','Choices':['A. Muriel', 'B. Kim', 'C. Jason', 'D. Zachary'], 'Answer': 'A'}, {'Question':'Who was Chandler’s TV magazine always addressed to?','Choices':['A. Chanandler Bong', 'B. Chanandler Bang', 'C. Chanandler Bing', 'D. Chanandler Beng'], 'Answer': 'A'}]
# class quiz implementation
class TriviaGame:
    def __init__(self, allQuestions):
        self.allQuestions= allQuestions
        self.userScore= 0
        self.currentIndex= 0
    def Display(self): # display function for welcome message
        print("WELCOME TO THE FRIENDS TRIVIA!\n")
        print("You will be given 5 multiple-choice questions to test your knowledge about FRIENDS")
    def loadQuestions(self): # function to sequentially load questions
        while self.currentIndex < len(self.allQuestions):
            question= self.allQuestions[self.currentIndex]
            print(f"{self.currentIndex + 1}: {question['Question']}")
            for choice in question['Choices']:
                print(choice)
            inputAnswer = input("Your answer: ")
            self.EvaluateAnswer(question, inputAnswer)
            self.currentIndex+= 1
    def EvaluateAnswer(self, question, inputAnswer): # function to check answers of user
        if inputAnswer.lower() == question['Answer'].lower(): # consider answer if input is in lowercase
            self.userScore+= 1
            print("Correct!\n--------")
        else:
            print(f"Incorrect. The correct answer is: {question['Answer']}\n-----------------------------------")
    def displayResult(self): # final result display function
        print("QUIZ OVER!\n---------")
        print("RESULT:")
        print(f"Your final score: {self.userScore}/{len(self.allQuestions)}")
        userPercentage= (self.userScore / len(self.allQuestions) * 100) 
        print(f"Your Percentage: {userPercentage:.2f}%")
        print("Goodbye :)")
# call functions to start quiz for user
trivia= TriviaGame(quizQuestions)
trivia.Display()
trivia.loadQuestions()
trivia.displayResult()