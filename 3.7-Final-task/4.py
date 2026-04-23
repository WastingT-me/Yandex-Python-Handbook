import pandas as pd
import json

user_id, class_id = map(int, input().split())

class_user_link = pd.read_csv('class_user_link.csv')
test_class_user_link = pd.read_csv('test_class_user_link.csv')
tests = pd.read_csv('test.csv')
test_task_link = pd.read_csv('test_task_link.csv')
test_attempt = pd.read_csv('test_attempt.csv')
tasks = pd.read_csv('task.csv')
task_attempt = pd.read_csv('task_attempt.csv')
users = pd.read_csv('user.csv')

first_name = users[users.id == user_id].first_name.iloc[0]
last_name = users[users.id == user_id].last_name.iloc[0]

# User
user_info = {
    "user_id": user_id,
    "full_name": ' '.join([last_name, first_name]),
    "class_id": class_id
}

class_user_link_id = (
    class_user_link[
        (class_user_link.user_id == user_id) &
        (class_user_link.class_id == class_id)
    ]
    .id
    .iloc[0]
)
user_tests = test_class_user_link[test_class_user_link.class_user_link_id == class_user_link_id]

tests_completed = 0
tests_total = len(user_tests)
test_accuracy = []

tests_dict = []

for j, test in user_tests.iloc[::-1].iterrows():
    # Progress
    test_class_user_link_id = test.id
    attempt = test_attempt[test_attempt.test_class_user_link_id == test_class_user_link_id]
    flag = attempt.flag_is_finished.iloc[0] if not attempt.empty else False
    if flag:
        tests_completed += 1

    user_test_id = test_attempt[test_attempt.test_class_user_link_id == test.id].id.iloc[0]
    tasks_ids = test_task_link[test_task_link.test_id == test.test_id].task_id
    test_tasks = pd.merge(tasks_ids, tasks, left_on='task_id', right_on='id')
    user_tasks = test_attempt[test_attempt.test_class_user_link_id == test.id]

    datetime_started = (
        test_class_user_link[
            (test_class_user_link.test_id == test.test_id) &
            (test_class_user_link.class_user_link_id == class_user_link_id)
        ]
    )
    datetime_started = datetime_started.datetime_started.iloc[0]
    datetime_started = str(datetime_started).split()[0].split('.')
    datetime_started[2] = datetime_started[2][2:]
    datetime_started = '.'.join(datetime_started)

    opened_tasks = 0
    solved_tasks = 0
    time_spent = 0
    results = []

    for i, task in test_tasks.iterrows():
        task_id, correct_answer = task.id, task.correct_answer
        user_answer = '?'
        user_task_id = task_attempt[(task_attempt.test_attempt_id == user_test_id) & (task_attempt.task_id == task_id)]
        if not user_task_id.empty and user_task_id.time_spent.iloc[0] > 0.0:
            opened_tasks += 1
            answer = user_task_id.answer.iloc[0]
            time_spent += user_task_id.time_spent.iloc[0]
            if answer == correct_answer:
                solved_tasks += 1
                user_answer = "TRUE"
            else:
                user_answer = "FALSE"
        results.append((i + 1, user_answer, task_id))

    h = int(time_spent // 3600)
    m = int(time_spent % 3600 // 60)
    s = int(time_spent % 3600 % 60)
    h = str(h) if h > 9 else '0' + str(h)
    m = str(m) if m > 9 else '0' + str(m)
    s = str(s) if s > 9 else '0' + str(s)

    # Tests
    current_test_info = {
        "test_id": test.test_id,
        "title": tests[tests.id == test.test_id].title.iloc[0],
        "tasks": [
            {
                "order_number": a,
                "task_id": c,
                "is_correct": b
            }
            for (a, b, c) in results
        ],
        "progress_percent": round(opened_tasks / len(test_tasks) * 100, 1),
        "correct_percent": 0.0 if opened_tasks == 0 else round(solved_tasks / opened_tasks * 100, 1),
        "time": ':'.join([h, m, s]),
        "date_assigned": datetime_started
    }
    tests_dict.append(current_test_info)

    # Progress: accuracy
    if opened_tasks != 0:
        test_accuracy.append(solved_tasks / opened_tasks * 100)

# Progress
progress = {
    "tests_completed": tests_completed,
    "tests_total": tests_total,
    "accuracy_average_percent": round(sum(test_accuracy) / len(test_accuracy), 1)
}

result = {
    "user": user_info,
    "progress": progress,
    "tests": tests_dict 
}

print(json.dumps(result, ensure_ascii=False, indent=2))