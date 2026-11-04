_tasks = []


def add_task(title):
    task = {"title": title.strip()}
    task = {"title": title,"done": False}
    _tasks.append(task)
    return task


def list_tasks():
    return _tasks

def sorted_tasks():
    return sorted(_tasks, key=lambda t: t["title"])

#a comment to show the difference