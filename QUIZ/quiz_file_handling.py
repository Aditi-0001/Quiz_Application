import os

def register():
    try:
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        
        with open("users.txt", "a") as f:
            f.write(f"{username}-{password}\n")
        print("Registration successful!")
    except Exception as e:
        print("An error occurred during registration:", e)

def login():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("users.txt", "r") as f:
            for user in f:
                # Check that the line has the expected format with "-"
                if "-" in user:
                    name, pwd = user.strip().split("-", 1)  # Split only once in case of extra "-"
                    if name == username and pwd == password:
                        print("Login successful!")
                        return username  # Return the username if login is successful
            print("Invalid username or password.")
            return None
    except Exception as e:
        print("An error occurred during login:", e)
        return None 

def load_questions(subject):
    filename = f"{subject}.txt"
    questions = []
    
    try:
        with open(filename, "r") as f:
            content = f.read().split("\n\n")
            for block in content:
                if block.strip():
                    lines = block.split("\n")
                    
                    # Check if there are enough lines for the question, options, and answer
                    if len(lines) >= 6:
                        question = lines[0]
                        options = lines[1:5]
                        # Ensure there is an answer line and it's properly formatted
                        answer_line = lines[5].strip()
                        if answer_line.startswith("Answer:"):
                            answer = answer_line.split(":")[1].strip()
                        else:
                            print(f"Warning: Invalid answer format for question '{question}'. Skipping this question.")
                            continue
                        questions.append((question, options, answer))
                    else:
                        print(f"Warning: Insufficient data for question block. Skipping.")
        return questions
    except FileNotFoundError:
        print(f"No questions found for {subject}. Please create the file '{filename}' with questions.")
        return []

def attempt_quiz(username):
    print("Choose a subject:\n1. DBMS\n2. DSA\n3. Python")
    choice = input("Enter the subject number (1-3): ")
    subject_map = {"1": "DBMS", "2": "DSA", "3": "PYTHON"}
    
    subject = subject_map.get(choice)
    if not subject:
        print("Invalid choice.")
        return

    questions = load_questions(subject)
    if not questions:
        return
    
    score = 0
    for question, options, correct_answer in questions:
        print("\n" + question)
        for option in options:
            print(option)
        answer = input("Your answer: ").strip().upper()
        if answer == correct_answer:
            score += 1

    print(f"Your score for {subject} quiz: {score}/{len(questions)}")
    update_result(username, score)

def update_result(username, score):
    results = {}
    
    try:
        if os.path.exists("results.txt"):
            with open("results.txt", "r") as f:
                data = f.read().splitlines()
                for line in data:
                    # Ensure the line has exactly one hyphen
                    if "-" in line:
                        try:
                            user, user_score = line.split("-", 1)
                            results[user] = int(user_score)
                        except ValueError:
                            print(f"Warning: Skipping malformed line: {line}")
        
        results[username] = max(score, results.get(username, 0))

        with open("results.txt", "w") as f:
            for user, user_score in results.items():
                f.write(f"{user}-{user_score}\n")
        print("Result saved successfully!")
    except Exception as e:
        print("An error occurred while saving the result:", e)

def show_result(username):
    try:
        with open("results.txt", "r") as f:
            results = f.read().splitlines()
            for result in results:
                # Ensure the line has exactly one hyphen
                if "-" in result:
                    try:
                        user, score = result.split("-", 1)
                        if user == username:
                            print(f"{username}'s highest score: {score}")
                            return
                    except ValueError:
                        print(f"Warning: Skipping malformed line: {result}")
        print(f"No result found for {username}.")
    except Exception as e:
        print("An error occurred while retrieving the result:", e)


if __name__ == "__main__":
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()  # Capture the returned username
            if username:  # Only proceed if login was successful
                while True:
                    print("\n1. Attempt Quiz")
                    print("2. Show Result")
                    print("3. Logout")
                    action = input("Choose an action (1-3): ")
                    if action == "1":
                        attempt_quiz(username)
                    elif action == "2":
                        show_result(username)
                    elif action == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
