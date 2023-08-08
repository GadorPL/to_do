todos = []

while True:
    user_action = input("Type add or show, or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:
            print("You entered an unknown command. Try again.")

print("Bye")
