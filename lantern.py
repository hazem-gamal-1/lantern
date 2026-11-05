import argparse

from tasks import add_task, list_tasks
from export import export_csv

def main():
    parser = argparse.ArgumentParser(prog="lantern")
    sub = parser.add_subparsers(dest="command")

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")
    export_parser = sub.add_parser("export")

    export_parser.add_argument("--csv", action="store_true")
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--sort", action="store_true", help="sort by title")
    list_parser.add_argument("--done", action="store_true")
    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print("added:", task["title"])
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks yet.")
        for task in tasks:
            print(task["title"])
    elif args.command == "export":
        export_csv()

    else:
        parser.print_help()