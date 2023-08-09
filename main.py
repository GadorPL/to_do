todos = []

while True:
    user_action = input("Type add or show, edit or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}={item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to mark complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("You entered an unknown command. Try again.")

print("Bye")
