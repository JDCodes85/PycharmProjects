# Main program loop, accept commands from the user using full word or shortcut text in ()
while True:
    userAction = input("Type (a)dd, (s)how, (e)dit, (c)omplete, or e(x)it: ")
    userAction = userAction.strip()

# Perform action based on user input
    match userAction:
        case 'add' | 'a':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 's':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        case 'edit' | 'e':
            number = int(input("Which task do you want to edit? "))
            number = number - 1

            with open('todos.txt','r') as file:
                todos = file.readlines()

            newTodo = input("Enter new todo: ")
            todos[number] = newTodo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete' | 'c':
            number = int(input("Enter number of completed task: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            toDoToRemove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {toDoToRemove} has been removed."
            print(message)

        case 'exit' | 'x':
            break
        case _:
            print("You entered an incorrect command. Try again.")

# Print confirmation that the program closed successfully.
print("Goodbye!")