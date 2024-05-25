from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"Task {i}:")
                print(task)
                print()

    def edit_task(self, title, new_title=None, new_description=None, new_due_date=None, new_priority=None):
        for task in self.tasks:
            if task.title == title:
                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description
                if new_due_date:
                    task.due_date = new_due_date
                if new_priority:
                    task.priority = new_priority
                return True
        return False

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                return True
        return False
