print(" 1. Registration \n 2. Login \n 3.Attempt quiz \n 4.Show score \n 5.Exit " )

users=[]
pwd={}
scores = {}
quizzes = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": 2},
        {"question": "Which data structure is LIFO?", "options": ["Queue", "Stack", "Deque", "Graph"], "answer": 2},
    ],
    "DBMS": [
        {"question": "Which SQL keyword is used to retrieve data?", "options": ["SELECT", "UPDATE", "DELETE", "INSERT"], "answer": 1},
        {"question": "What does ACID stand for in databases?", "options": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Clarity, Integration, Dependability", "Automated, Consistent, Independent, Distributed", "None of the above"], "answer": 1},
    ],
    "Python": [
        {"question": "Which of these is not a keyword in Python?", "options": ["pass", "eval", "assert", "function"], "answer": 4},
        {"question": "What does PEP stand for in Python?", "options": ["Python Enhancement Proposal", "Python Effective Program", "Program Efficiency Proposal", "Programming Enhancement Python"], "answer": 1},
    ],
}

def register():
    u=input("Enter username :").strip()
    passwd=input("Enter password :")
    users.append(u)
    pwd[u]=passwd
    scores[u] = {}  # Initialize scores dictionary for the user
    print("Registered successfully.")

def login():
    u=input("Enter username :").strip()
    if u in users:
        passwd=input("Enter password :")
        if passwd==pwd[u]:
            print("Logged in successfully .")
        else :
            print("Wrong password.")
    else:
        print ("Wrong username.")

def attempt_quiz():
    username = input("Enter your username: ").strip()
    if username not in users:
        print("Please register or login first.")
        return
    print("Available subjects:")
    for i, subject in enumerate(quizzes.keys(), start=1):
        print(f"{i}. {subject}")
    try:
        subject_choice = int(input("Select a subject: "))
        subject = list(quizzes.keys())[subject_choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    print(f"\nStarting quiz on {subject}...")
    score = 0
    for i, q in enumerate(quizzes[subject], start=1):
        print(f"\nQ{i}. {q['question']}")
        for opt_i, option in enumerate(q['options'], start=1):
            print(f"{opt_i}. {option}")
        try:
            answer = int(input("Enter your answer (1/2/3/4): "))
            if answer == q['answer']:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        except ValueError:
            print("Invalid input. Moving to the next question.")
    if subject not in scores[username]:
        scores[username][subject] = score
    else:
        scores[username][subject] += score
    print(f"Quiz completed! You scored {score}.")

def show_score():
    print("\n=== Results ===")
    username = input("Enter your username: ")
    if username not in scores:
        print("No records found for this user.")
        return
    print(f"\nScores for {username}:")
    for subject, score in scores[username].items():
        print(f"{subject}: {score}")

while True:
    choice=int(input("Enter your choice : "))
    if choice== 1:
        register()
    elif choice== 2:
        login()
    elif choice == 3:
        attempt_quiz()
    elif choice ==4:
        show_score()
    elif choice == 5:
        exit()
    else :
        print("Enter a valid choice.")


