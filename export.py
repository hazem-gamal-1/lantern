import csv
import sys

from tasks import list_tasks


def export_csv(out=sys.stdout):
    writer = csv.writer(out)
    writer.writerow(["title", "done"])
    for task in list_tasks():
        writer.writerow([task["title"], task.get("done", False)])