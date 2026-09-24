def quiz():
    score = 0

    print("===== PAKISTAN GENERAL KNOWLEDGE QUIZ =====")

    # Question 1
    answer = input("1. What is the national flower of Pakistan? ")
    if answer.lower().strip() == "jasmine":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Jasmine.")

    # Question 2
    answer = input("2. Which is the highest peak in Pakistan? ")
    if answer.lower().strip() in ["k2", "k-2", "godwin austen"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is K2.")

    # Question 3
    answer = input("3. What is the capital city of Pakistan? ")
    if answer.lower().strip() == "islamabad":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Islamabad.")

    # Question 4
    answer = input("4. Which is the longest river in Pakistan? ")
    if answer.lower().strip() in ["indus river", "indus"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Indus River.")

    # Question 5
    answer = input("5. Who is the national poet of Pakistan? ")
    if "iqbal" in answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Allama Iqbal.")

    # Question 6
    answer = input("6. Who was the founder of Pakistan? ")
    if "jinnah" in answer.lower() or "quaid" in answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Quaid-e-Azam Muhammad Ali Jinnah.")

    # Question 7
    answer = input("7. What is the national sport of Pakistan? ")
    if answer.lower().strip() == "field hockey" or answer.lower().strip() == "hockey":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Hockey.")

    print(f"\nYour final score is: {score} / 7")


quiz()