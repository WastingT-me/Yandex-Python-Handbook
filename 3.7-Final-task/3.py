import pandas as pd

user_id, class_id = map(int, input().split())

class_user_link = pd.read_csv('class_user_link.csv')
test_class_user_link = pd.read_csv('test_class_user_link.csv')
tests = pd.read_csv('test.csv')
test_task_link = pd.read_csv('test_task_link.csv')
test_attempt = pd.read_csv('test_attempt.csv')
tasks = pd.read_csv('task.csv')
task_attempt = pd.read_csv('task_attempt.csv')

class_user_link_id = (
    class_user_link[
        (class_user_link.user_id == user_id) & 
        (class_user_link.class_id == class_id)
    ]
    .id
    .iloc[0]
)
user_tests = test_class_user_link[test_class_user_link.class_user_link_id == class_user_link_id]
test = user_tests.iloc[-1]
user_test_id = test_attempt[test_attempt.test_class_user_link_id == test.id].id.iloc[0]
tasks_ids = test_task_link[test_task_link.test_id == test.test_id].task_id
test_tasks = pd.merge(tasks_ids, tasks, left_on='task_id', right_on='id')
user_tasks = test_attempt[test_attempt.test_class_user_link_id == test.id]

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

print(f'{opened_tasks / len(test_tasks) * 100:.01f}% {solved_tasks / opened_tasks * 100:.01f}%')

for a, b, c in results:
    print(a, b, c)

h = int(time_spent // 3600)
m = int(time_spent % 3600 // 60)
s = int(time_spent % 3600 % 60)
h = str(h) if h > 9 else '0' + str(h)
m = str(m) if m > 9 else '0' + str(m)
s = str(s) if s > 9 else '0' + str(s)
print(':'.join([h, m, s]))