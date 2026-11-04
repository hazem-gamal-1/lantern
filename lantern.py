import argparse

from tasks import add_task, list_tasks


def main():
    parser = argparse.ArgumentParser(prog="lantern")
    sub = parser.add_subparsers(dest="command")

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    list_parser = sub.add_parser("list")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print("added:", task["title"])
    elif args.command == "list":
        for task in list_tasks():
            print(task["title"])
    else:
        parser.print_help()
