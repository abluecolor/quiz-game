print("Welcome!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

def quiz_game():
    print("Okay! Let's play :) ")
    score = 0

    answer = input("What does the 'elif' keyword stand for? ")
    if answer.lower() == "else if":
        print("Correct!")
        score += 1
    else: 
        print("Incorrect! Correct answer: else if")

    answer = input("What is the popular snake-inspired programming language? ")
    if answer.lower() == "python":
        print("Correct!")
        score += 1
    else: 
        print("Incorrect! Correct answer: python")

    answer = input("HTML stands for? ")
    if answer.lower() == "hypertext markup language":
        print("Correct!")
        score += 1
    else: 
        print("Incorrect! Correct answer: hypertext markup language")

    answer = input("What do you call a function that calls itself? ")
    if answer.lower() == "recursive function":
        print("Correct!")
        score += 1
    else: 
        print("Incorrect! Correct answer: recursive function")

    answer = input("What does the 'DOM' stand for in JavaScript? ")
    if answer.lower() == "document object model":
        print("Correct!")
        score += 1
    else: 
        print("Incorrect! Correct answer: document object model")

    print("You got " + str(score) + " questions correct!")
    if score < 5:
        more = input("Try again? ")
        if more == "yes":
            quiz_game()
        else:
            quit()
    else:
        print("You got them all right! :)")

quiz_game()