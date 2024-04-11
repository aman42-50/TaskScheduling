from datetime import date
import math
from typing import List, Optional, Tuple, Literal

class Task:
    def __init__(self, task_id: str, description: str, work: float, max_workers: int, units_of_work_per_manday: float, rules: Optional[str] = None):
        self.task_id: str = task_id
        self.description: str = description
        self.work: float = work
        self.max_workers: int = max_workers
        self.units_of_work_per_manday: float = units_of_work_per_manday
        self.rules: Optional[str] = rules
        self.duration : Optional[int] = None
        self.start_date: Optional[date] = None
        self.end_date: Optional[date] = None

    def calculate_duration(self) -> None:

        # calculate the units of work max_workers can do in a day
        units_of_work_in_a_day = self.units_of_work_per_manday * self.max_workers

        # duration = total amount of work / units of work max_workers can do in a day
        self.duration = int(math.ceil(self.work / units_of_work_in_a_day))


class TaskDependency:
    def __init__(self, depends_on: Task, dependend_task: Task, dependency_type: Literal['fs', 'ff', 'ss', 'sf']):
        self.depends_on: Task = depends_on
        self.dependent_task: Task = dependend_task
        self.dependency_type: Literal['fs', 'ff', 'ss', 'sf'] = dependency_type
