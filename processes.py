"""программа для работы с процессами"""

import os
import time


def show_message(text=""):
    print("-" * 45)
    if text:
        print(text)
    else:
        print("Готово!")
    print("-" * 45)


def main():
    print("Starting...")
    print(f"pid : {os.getpid()}")
    print(f"ppid : {os.getppid()}")
    time.sleep(5)
    welcome()


def welcome():
    print("Welcome!")
    print(f"pid : {os.getpid()}")
    time.sleep(5)
    work()


def work():
    print("Working...")
    print(f"pid : {os.getpid()}")
    time.sleep(5)


def finish():
    print("Finished!")
    print(f"pid : {os.getpid()}")
    time.sleep(5)


if __name__ == '__main__':
    main()
