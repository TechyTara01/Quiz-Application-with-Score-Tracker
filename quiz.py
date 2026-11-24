import os


print("=== Subject Quiz ===")


# Get student details first
name = input("Enter your name: ")
enrollment = input("Enter your enrollment number: ")
branch = input("Enter your branch: ")
department = input("Enter your department: ")


subjects = [
    "Python",
    "Linear Algebra",
    "Software Engineering and Development",
    "Digital Logic Design",
    "AI Landscape and Tool"
]


file_names = [
    "python_notes.txt",
    "linear_algebra_notes.txt",
    "software_engineering_notes.txt",
    "digital_logic_notes.txt",
    "ai_notes.txt"
]


# Correct choices for questions 1 through 10 in each subject
answer_keys = [
    ["C", "B", "D", "B", "C", "B", "C", "C", "A", "C"],
    ["B", "B", "C", "A", "B", "A", "B", "B", "C", "C"],
    ["B", "C", "A", "C", "B", "B", "B", "B", "B", "B"],
    ["A", "C", "B", "C", "C", "C", "B", "B", "C", "C"],
    ["B", "B", "A", "B", "B", "B", "A", "A", "A", "C"]
]


print("\nChoose a subject:")
for i in range(len(subjects)):
    print(str(i + 1) + ". " + subjects[i])


subject_choice = input("Enter a subject number (1-5): ")


while subject_choice not in ["1", "2", "3", "4", "5"]:
    subject_choice = input("Please enter a number from 1 to 5: ")


subject_index = int(subject_choice) - 1
selected_subject = subjects[subject_index]


# Use the folder containing this Python file for the question and result files
folder = os.path.dirname(os.path.abspath(__file__))
selected_file = os.path.join(folder, file_names[subject_index])


questions = []
options = []
current_options = []


try:
    with open(selected_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()


            if line.startswith("Q") and "." in line:
                questions.append(line.split(".", 1)[1].strip())


            elif line.startswith(("A)", "B)", "C)", "D)")):
                current_options.append(line[3:].strip())


                if line.startswith("D)"):
                    options.append(current_options)
                    current_options = []


except FileNotFoundError:
    print("\nQuestion file not found:", file_names[subject_index])
    print("Make sure it is in the same folder as this Python program.")


else:
    valid_file = len(questions) == 10 and len(options) == 10


    for question_options in options:
        if len(question_options) != 4:
            valid_file = False


    if not valid_file:
        print("\nThe selected file must contain 10 questions with four options each.")
    else:
        score = 0


        print("\nSubject:", selected_subject)
        print("Correct answer: +1 mark | Wrong answer: 0 marks")
        print("Enter A, B, C, or D.\n")


        for i in range(10):
            print("Question", i + 1, ":", questions[i])


            for j in range(4):
                print(chr(65 + j) + ") " + options[i][j])


            answer = input("Your answer: ").strip().upper()


            while answer not in ["A", "B", "C", "D"]:
                answer = input("Please enter A, B, C, or D: ").strip().upper()


            if answer == answer_keys[subject_index][i]:
                print("Correct! +1 mark\n")
                score = score + 1
            else:
                print("Wrong answer. 0 marks\n")


        print("=== Quiz Result ===")
        print("Name:", name)
        print("Enrollment:", enrollment)
        print("Branch:", branch)
        print("Department:", department)
        print("Subject:", selected_subject)
        print("Score:", score, "out of 10")
        print("Percentage:", score * 10, "%")


        results_file = os.path.join(folder, "quiz_results.txt")


        with open(results_file, "a", encoding="utf-8") as file:
            file.write("Name: " + name + "\n")
            file.write("Enrollment: " + enrollment + "\n")
            file.write("Branch: " + branch + "\n")
            file.write("Department: " + department + "\n")
            file.write("Subject: " + selected_subject + "\n")
            file.write("Score: " + str(score) + " out of 10\n")
            file.write("------------------------------\n")


        print("\nResult saved in quiz_results.txt")





THIS IS PYTHON TAB AND FOLLOWING IS THE WRITTEN CODE WHICH YOU CAN COPY ON YOUR SYSTEM AND PASTE IN FOLLOWING COMPILER 




CODE

import os


print("=== Subject Quiz ===")


# Get student details first
name = input("Enter your name: ")
enrollment = input("Enter your enrollment number: ")
branch = input("Enter your branch: ")
department = input("Enter your department: ")


subjects = [
    "Python",
    "Linear Algebra",
    "Software Engineering and Development",
    "Digital Logic Design",
    "AI Landscape and Tool"
]


file_names = [
    "python_notes.txt",
    "linear_algebra_notes.txt",
    "software_engineering_notes.txt",
    "digital_logic_notes.txt",
    "ai_notes.txt"
]


# Correct choices for questions 1 through 10 in each subject
answer_keys = [
    ["C", "B", "D", "B", "C", "B", "C", "C", "A", "C"],
    ["B", "B", "C", "A", "B", "A", "B", "B", "C", "C"],
    ["B", "C", "A", "C", "B", "B", "B", "B", "B", "B"],
    ["A", "C", "B", "C", "C", "C", "B", "B", "C", "C"],
    ["B", "B", "A", "B", "B", "B", "A", "A", "A", "C"]
]


print("\nChoose a subject:")
for i in range(len(subjects)):
    print(str(i + 1) + ". " + subjects[i])


subject_choice = input("Enter a subject number (1-5): ")


while subject_choice not in ["1", "2", "3", "4", "5"]:
    subject_choice = input("Please enter a number from 1 to 5: ")


subject_index = int(subject_choice) - 1
selected_subject = subjects[subject_index]


# Use the folder containing this Python file for the question and result files
folder = os.path.dirname(os.path.abspath(__file__))
selected_file = os.path.join(folder, file_names[subject_index])


questions = []
options = []
current_options = []


try:
    with open(selected_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()


            if line.startswith("Q") and "." in line:
                questions.append(line.split(".", 1)[1].strip())


            elif line.startswith(("A)", "B)", "C)", "D)")):
                current_options.append(line[3:].strip())


                if line.startswith("D)"):
                    options.append(current_options)
                    current_options = []


except FileNotFoundError:
    print("\nQuestion file not found:", file_names[subject_index])
    print("Make sure it is in the same folder as this Python program.")


else:
    valid_file = len(questions) == 10 and len(options) == 10


    for question_options in options:
        if len(question_options) != 4:
            valid_file = False


    if not valid_file:
        print("\nThe selected file must contain 10 questions with four options each.")
    else:
        score = 0


        print("\nSubject:", selected_subject)
        print("Correct answer: +1 mark | Wrong answer: 0 marks")
        print("Enter A, B, C, or D.\n")


        for i in range(10):
            print("Question", i + 1, ":", questions[i])


            for j in range(4):
                print(chr(65 + j) + ") " + options[i][j])


            answer = input("Your answer: ").strip().upper()


            while answer not in ["A", "B", "C", "D"]:
                answer = input("Please enter A, B, C, or D: ").strip().upper()


            if answer == answer_keys[subject_index][i]:
                print("Correct! +1 mark\n")
                score = score + 1
            else:
                print("Wrong answer. 0 marks\n")


        print("=== Quiz Result ===")
        print("Name:", name)
        print("Enrollment:", enrollment)
        print("Branch:", branch)
        print("Department:", department)
        print("Subject:", selected_subject)
        print("Score:", score, "out of 10")
        print("Percentage:", score * 10, "%")


        results_file = os.path.join(folder, "quiz_results.txt")


        with open(results_file, "a", encoding="utf-8") as file:
            file.write("Name: " + name + "\n")
            file.write("Enrollment: " + enrollment + "\n")
            file.write("Branch: " + branch + "\n")
            file.write("Department: " + department + "\n")
            file.write("Subject: " + selected_subject + "\n")
            file.write("Score: " + str(score) + " out of 10\n")
            file.write("------------------------------\n")


        print("\nResult saved in quiz_results.txt")



