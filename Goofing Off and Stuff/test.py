import time

exercise_data = [
    {"date": "2022-01-01", "exercise": "Running", "duration": 30}
]
all_exercises = []

def add_exercise():
    while True:
        new_date = input("Enter Date (YYYY-MM-DD): ")
        new_exercise = input("Enter exercise: ")
        new_duration = input("Enter duration (in minutes): ")
        date_str = '| 1. Date: ' + new_date
        spaces = ''
        for i in range(29-len(date_str)):
            spaces += ' '
        print(" ____________________________ ")
        print("|    Is the data correct?    |")
        print("|----------------------------|")
        print(date_str + spaces + '|')
        exercise_str = '| 2. Exercise: ' + new_exercise
        spaces = ''
        for i in range(29-len(exercise_str)):
            spaces += ' '
        print(exercise_str + spaces + '|')
        duration_str = '| 3. Duration: ' + new_duration
        spaces = ''
        for i in range(29-len(duration_str)):
            spaces += ' '
        print(duration_str + spaces + '|')
        print("|----------------------------|")
        print("|  If the data is correct,   |")
        print("|   type 'yes' to confirm.   |")
        print("|    Otherwise, type 'no'    |")
        print("|____________________________|")
        confirmation = input(">>> ")
        if confirmation == 'yes':
            break
        elif confirmation == 'no':
            add_exercise()
        else:
            print("Invalid Command")
            

    new_exercise_data = {"date": new_date, "exercise": new_exercise, "duration": new_duration}
    exercise_data.append(new_exercise_data)
    print(f"Exercise {new_exercise} added successfully!\n")


def weekly_summary():
    global exercise
    print("\n--- Weekly Summary ---")
    weekly_sum = 0
    while not exercise in all_exercises:
        exercise = input("Enter exercise to view weekly summary on: ")
    for data in exercise_data:
        if data['exercise'] == exercise:
            weekly_sum += int(data['duration'])
    print("Weekly sum for " + exercise + ": " + str(weekly_sum))

def display_data():
    print("\n--- Exercise Data ---")
    for data in exercise_data:
        print("Date: " + data["date"] + " | Exercise: " + data["exercise"] + " | Duration (in minutes): " + str(data["duration"]))

for i in exercise_data:
    for exercise in exercise_data:
        all_exercises.append(exercise["exercise"])

print(" _____________________________ ")
print("| Welcome to Fitness Tracker! |")
print("| --------------------------- |")
print("| 1. Add an Exercise          |")
print("| 2. Display Exercise Data    |")
print("| 3. View Weekly Summmary for |")
print("|    an Exercise.             |")
print("|_____________________________|")
while True:
    command = input("> ")
    if command == "1":
        print("\n--- Add an Exercise ---")
        add_exercise()
    elif command == "2":
        display_data()
    elif command == "3":
        weekly_summary()
    else:
        print("Invalid Command")