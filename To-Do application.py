import datetime

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description, due_date=None, priority=None):
        task_id = len(self.tasks) + 1
        task_details = {
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'completed': False
        }
        self.tasks[task_id] = task_details
        print(f'Task {task_id} added successfully.')

    def display_tasks(self):
        print("\nTo-Do List:")
        for task_id, details in self.tasks.items():
            status = "Completed" if details['completed'] else "Pending"
            print(f"{task_id}. {details['description']} - Due: {details['due_date']} - Priority: {details['priority']} - Status: {status}")

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f'Task {task_id} marked as completed.')
        else:
            print('Invalid task ID.')

    def update_task(self, task_id, description=None, due_date=None, priority=None):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task['description'] = description if description else task['description']
            task['due_date'] = due_date if due_date else task['due_date']
            task['priority'] = priority if priority else task['priority']
            print(f'Task {task_id} updated successfully.')
        else:
            print('Invalid task ID.')

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f'Task {task_id} removed successfully.')
        else:
            print('Invalid task ID.')

# Example usage:
if __name__ == "__main__":
    todo_list = ToDoList()

    todo_list.add_task("Finish project", due_date="2023-11-15", priority="High")
    todo_list.add_task("Go to the gym", priority="Medium")
    todo_list.add_task("Read a book", due_date="2023-11-12")

    todo_list.display_tasks()

    todo_list.mark_completed(1)
    todo_list.update_task(2, description="Go to the gym - Updated", due_date="2023-11-18")
    todo_list.remove_task(3)

    todo_list.display_tasks()
