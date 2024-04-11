#!/usr/bin/env python
import math
from models import Task, TaskDependency
from interact_excel import excel_to_dict, write_to_excel
from schedule import topological_sort, assign_dates

def main():
    # path to your excel file
    excel_file: str = "cult_project.xlsx"

    # stores the excel data in a dictionary
    data: dict = excel_to_dict(excel_file)

    tasks = {}
    dependencies = []

    for item in data:
        task = Task(
            task_id = item['task_id'],
            description = item['description'],
            work = item['work'],
            max_workers = item['workers'],
            units_of_work_per_manday = item['units_of_work_per_manday']
        )

        if isinstance(item['rules'], str):
            task.rules = item['rules']

        task.calculate_duration()

        tasks[task.task_id] = task

    for item in data:
        if isinstance(item['dependencies'], str):
            dependent_task = tasks[item['task_id']]

            for depends_on_id in item['dependencies'].split(','):
                depends_on_id = depends_on_id.strip()
                dependency_type = item['dependency type']
                depends_on = tasks[depends_on_id]

                dependency = TaskDependency(
                    depends_on = depends_on,
                    dependend_task = dependent_task,
                    dependency_type = dependency_type
                )

                dependencies.append(dependency)

    sorted_tasks = topological_sort(tasks, dependencies)
    assign_dates(sorted_tasks, tasks)

    # for task_id, task in tasks.items():
    #     print(task_id, task.start_date, task.end_date)

    write_to_excel(excel_file, tasks)

if __name__ == '__main__':
    main()
