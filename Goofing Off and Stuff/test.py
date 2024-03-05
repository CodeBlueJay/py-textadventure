exercise_data = []
dates = []
exercises = []
durations = []

def add_exercise(date, exercise, duration):
    exercise_data.append({'date': date, 'exercise': exercise, 'duration': duration})
    for entry in exercise_data:
        dates.append(entry['date'])
        exercises.append(entry['exercise'])
        durations.append(entry['duration'])

def weekly_summary(exercise):
    weekly_sum = 0
    for entry in exercise_data:
        if entry['exercise'] == exercise:
            weekly_sum += entry['duration']
    print(weekly_sum)

def display_data():
    for entry in exercise_data:
        print(f"{entry['date']} | {entry['exercise']} | {entry['duration']}")

add_exercise('2022-01-01', 'Running', 30)
add_exercise('2022-01-02', 'Swimming', 45)
display_data()
weekly_summary('Running')