question_1 = input("SURVEY Are you interested in computer science? (y/n): ")
question_2 = input("Do you like playing computer games? (y/n): ")
question_3 = input("Do you have an Instagram account? (y/n): ")

if(question_1 == "y"):
    answer_1 = True
else:
    answer_1 = False
if(question_2 == "y"):
    answer_2 = True
else:
    answer_2 = False
if(question_3 == "y"):
    answer_3 = True
else:
    answer_3 = False

if(answer_1):
    print("SURVEY RESULTS Interested in computer science: Yes")
else:
    print("SURVEY RESULTS Interested in computer science: No")

if(answer_2):
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if(answer_3):
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")