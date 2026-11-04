_tasks = []


def add_task(title):
    task = {"title": title,"done": False}
    _tasks.append(task)
    return task


def list_tasks():
    return _tasks


#a comment to show the difference