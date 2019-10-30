'''
Task scheduler (counting slots required)

We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time,
but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.

Exapmle:
tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)

Solution translated from Java to Python from:
https://sugarac.gitbooks.io/facebook-interview-handbook/task-scheduler.html
'''
from collections import defaultdict
def task_schedule(tasks, cooldown):
    if tasks == None or len(tasks) == 0:
        return 0
    my_map = defaultdict(int)
    slots = 0
    for task in tasks:
        if task in my_map and my_map[task] > slots:
            slots = my_map[task]
        my_map[task] = slots + cooldown + 1
        slots += 1
    return slots

# Test
tasks = [1, 1, 2, 1]
tasks2 = [1, 1, 1, 2, 2, 2]
cooldown = 2
print task_schedule(tasks, cooldown)
