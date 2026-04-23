import pandas as pd

lens = []
paths = [
    'user.csv',
    'class.csv',
    'class_user_link.csv',
    'task.csv',
    'test.csv',
    'test_task_link.csv',
    'test_class_user_link.csv',
    'test_attempt.csv',
    'task_attempt.csv'
]

for path in paths:
    df = pd.read_csv(path)
    lens.append(str(len(df)))

print(' '.join(lens))