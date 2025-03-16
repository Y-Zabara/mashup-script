#!/usr/bin/env python3
import argparse
import commands
import re

def check(args):
    print(int(commands.check_tasks() * 1000))

def show(args):
    tasks = commands.show_tasks()
    print(f"{'-'*35}")
    for task in tasks:
        print(f"Command: {task['command']}")
        print(f"Hash: {task['calculated_hash']}")
        print(f"Mode: {task['invert_mode']}")
        print(f"Status: {task['status']}")
        print(f"{'-'*35}")

def delete(args):
    if commands.delete_task(args.id):
        print(f"Task with ID {args.id} successfully deleted.")
    else:
        print(f"Task with ID {args.id} not found.")

def add(args):
    if not re.fullmatch(r"[a-fA-F0-9]{32}", args.hash):
        print(f"Invalid hash: {args.hash}. Hash must be a valid MD5 hash (32 hexadecimal characters).")
        return

    if commands.add_task(args.command, args.hash):
        print(f"Task added successfully: Command='{args.command}', Hash='{args.hash}'")
    else:
        print("Failed to add the task. Please check the inputs.")

def main():
    parser = argparse.ArgumentParser(description="Програма з командами check, show, delete і add.")

    subparsers = parser.add_subparsers(help="Доступні команди")

    # Команда 'check'
    check_parser = subparsers.add_parser('check', help="Перевірка задач")
    check_parser.set_defaults(func=check)

    # Команда 'show'
    show_parser = subparsers.add_parser('show', help="Показати інформацію")
    show_parser.set_defaults(func=show)

    # Команда 'delete'
    delete_parser = subparsers.add_parser('delete', help="Видалити задачу за ID")
    delete_parser.add_argument('id', type=int, help="ID задачі для видалення")
    delete_parser.set_defaults(func=delete)

    # Команда 'add'
    add_parser = subparsers.add_parser('add', help="Додати нову задачу")
    add_parser.add_argument('command', type=str, help="Bash команда для виконання")
    add_parser.add_argument('hash', type=str, help="MD5 хеш команди")
    add_parser.set_defaults(func=add)

    args = parser.parse_args()

    # Перевірка, чи була передана команда
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

