def get_todos(filepath="todos.txt"):
    """ read a text file and return the list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath ="todos.txt"):
    """ Write the to-do items lsit in the text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__name__":
    print("hello")
    print(get_todos())


