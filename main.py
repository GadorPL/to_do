while True:
    user_action = input("Type add or show, edit or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', '2') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}={item}"
            print(row)
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')

        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye")
