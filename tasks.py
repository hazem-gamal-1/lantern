_tasks = []


def add_task(title):
    task = {"title": title.strip()}
    _tasks.append(task)
    return task


def list_tasks():
    return _tasks


#a comment to show the difference