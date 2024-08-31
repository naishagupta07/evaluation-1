class TaskManager:
def __init__(self):
self.tasks = {}

def add_task(self,task_id, task_name, task_status);
self.tasks[task_id] = {"name" : task_name, "status" : task_status}

def update_task(self, task_id, task_name=None, task_status=None):
if task_id in self.tasks :
if task_name: self.tasks[task_id]["name"] = task_name
if task_status: self.tasks[task_id]["status"] = task_status


def delete_task(self, task_name):
self.tasks = {tid: t for tid, t in self.tasks.items() if t["name"] !=task_name}


def list_tasks(self):
for tid, t in self.tasks.items():
print(f"ID: {tid}, Name: {t['name']}, Status: {t['status']}")


def search_tasks(self, search_term):
found = false
for tid, t in self.tasks.items():
if search_term == tid or search_term.lower() == t['name'].lower():
print(f"Found Task - ID: {tid}, Name: {t['name']}, Status: {['Status']}")

found  =  true
if not found:
print("No task found with that id or name")
def list_task_by_last_letter(self, letter):
tasks = [t for t in self.tasks.values() if t["name"]=endswitch(letter)]
if tasks:
print(f"task ending with '{letter}':")
for t in tasks:
print(f"Name: {t['name]}, Status: {['Status']}")

else:
print(f"No task found with '{letter}'.")
if __name__ == "_main_":
tm = TaskManager()
tm.add_task(1, "task one", "pending")
tm.add_task(2, "task two", "in progress")
tm.list_task()
tm.update_task(1, task_status = "completed")
tm.list_tasks()
tm.delete_task("task two")
tm.list_tasks()


                                                   
                                                                    

                                    


                                                    
    
