from collections import defaultdict, deque
from datetime import datetime, timedelta


def topological_sort(tasks, dependencies):

    graph = defaultdict(list)
    indegree = defaultdict(int)

    for dependency in dependencies:
        graph[dependency.depends_on.task_id].append((dependency.dependent_task.task_id, dependency.dependency_type))
        indegree[dependency.dependent_task] += 1

    tasks_starting_idx = defaultdict(int)

    que = deque()
    for task in tasks:
        if indegree[task] == 0:
            que.append((task, 0))
            tasks_starting_idx[task] = 0


    if not que:
        return False

    while que:
        task, idx = que.popleft()
        for child, dependency_type in graph[task]:
            indegree[child] -= 1
            if dependency_type == "fs":
                idx = idx + tasks[task].duration
            elif dependency_type == "ff":
                idx = idx + tasks[task].duration - tasks[child].duration
            tasks_starting_idx[child] = max(tasks_starting_idx[child], idx)
            if indegree[child] == 0:
                que.append((child, idx))

    if len(tasks_starting_idx) != len(tasks):
        return False

    return tasks_starting_idx


def add_days(date_str, days):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = date + timedelta(days=days)
    new_date_str = new_date.strftime('%Y-%m-%d')

    return new_date_str

def assign_dates(sorted_tasks, tasks) -> None:

    project_start_date = '2024-04-12'

    for task, idx in sorted_tasks.items():
        start_date = add_days(project_start_date, idx)
        end_date = add_days(project_start_date, idx + tasks[task].duration)
        tasks[task].start_date = start_date
        tasks[task].end_date = end_date
