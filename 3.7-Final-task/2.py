import pandas as pd

user_id, class_id = map(int, input().split())

result = []

class_user_link = pd.read_csv('class_user_link.csv')
test_class_user_link = pd.read_csv('test_class_user_link.csv')
tests = pd.read_csv('test.csv')
test_task_link = pd.read_csv('test_task_link.csv')
test_attempt = pd.read_csv('test_attempt.csv')

class_user_link_id = (
    class_user_link[
        (class_user_link.user_id == user_id) & 
        (class_user_link.class_id == class_id)
    ]
    .id
    .iloc[0]
)
user_tests = test_class_user_link[test_class_user_link.class_user_link_id == class_user_link_id]

for _, test in user_tests.iterrows():
    title = tests[tests.id == test.test_id].title.iloc[0]

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
    
    test_class_user_link_id = test.id
    attempt = test_attempt[test_attempt.test_class_user_link_id == test_class_user_link_id]
    flag = attempt.flag_is_finished.iloc[0] if not attempt.empty else False

    result.append((title, datetime_started, flag))

result = sorted(result, key=lambda x: (pd.to_datetime(x[1]), x[0]), reverse=True)
print(f'{sum(map(lambda x:x[2], result))}/{len(result)}')
for a, b, c in result:
    print(a, b, "TRUE" if c else "FALSE")