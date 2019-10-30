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
