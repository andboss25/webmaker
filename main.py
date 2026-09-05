
import sys
import os

sys.dont_write_bytecode = True

from core.application import Application

from core.utils import error

def help():
    print("usage:")
    print("new -> makes new application")
    print("check <directory> -> checks if an application is runnable")
    print("build <directory> -> build an application")
    print("serve <directory> -> serve an application")

def make_new_application_command(argv):
    name = input("Application Name >> ")
    author = input("Application Author >> ")

    app = Application(
        name,
        author
    )

    app.store()
    app.build()

    print(f"Do ^replace here^ serve {os.path.join("build",app.sanitized_name)} to run the application")

    return

def main(argv):
    if len(argv) <= 1: help(); return;

    if argv[1] == "new":
        make_new_application_command(argv)
        return;

    if len(argv) <= 2: help(); return;

    if argv[1] == "check":
        try:
            app = Application.load(sys.argv[2])
        except FileNotFoundError:
            error("No such file or directory!")
            return;
        print(f"Loaded '{app.name}', all seems okay!")
        return;

    if argv[1] == "build":
        try:
            app = Application.load(sys.argv[2])
        except FileNotFoundError:
            error("No such file or directory!")
            return;

        app.build()
        return;

    if argv[1] == "serve":
        try:
            app = Application.load(sys.argv[2])
        except FileNotFoundError:
            error("No such file or directory!")
            return;

        os.system(f"python {os.path.join("build",app.sanitized_name,"main.py")}")
        return;

    help()
    return

if __name__ == "__main__":
    main(sys.argv)