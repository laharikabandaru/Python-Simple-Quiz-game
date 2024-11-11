print("Welcome to Simple Quiz Game")
def quiz():
    """
    Conducts a quiz with multiple-choice questions.

    Returns:
        int: The final score of the user.
    """
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What is the largest country in the world by land area?",
            "options": ["Russia", "Canada", "China", "United States"],
            "answer": "Russia"
        }
    ]

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")

        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        while user_answer not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number between 1 and 4.")
            user_answer = input("Enter your answer (1, 2, 3, or 4): ")

        user_answer = int(user_answer) - 1
        if question["options"][user_answer] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])

    print("\nYour final score is:", score, "/", len(questions))
    return score

if __name__ == "__main__":
    quiz()