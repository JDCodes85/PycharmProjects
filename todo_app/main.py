# Create an empty list of todos
todos = []

# Main program loop, accept commands from the user using full word or shortcut text in ()
while True:
    userAction = input("Type (a)dd, (s)how, (e)dit, (c)omplete, or e(x)it: ")
    userAction = userAction.strip()

# Perform action based on user input
    match userAction:
        case 'add' | 'a':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 's':
            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit' | 'e':
            number = int(input("Which task do you want to edit? "))
            number = number - 1
            newTodo = input("Enter new todo: ")
            todos[number] = newTodo
        case 'complete' | 'c':
            number = int(input("Enter number of completed task: "))
            todos.pop(number - 1)
        case 'exit' | 'x':
            break
        case _:
            print("You entered an incorrect command. Try again.")

# Print confirmation that the program closed successfully.
print("Goodbye!")