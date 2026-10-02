def calculator():

    total = 0
    history = []
    redo_history = []

    # operations in a while loop
    while True:
        user_input = input("> ").strip()
        parts = user_input.split()
        # print(parts)

        if not parts:
            print("Invalid Input")
            continue
        
        operator = parts[0]


        if operator == "exit":
            if len(parts) != 1:
                print("Invalid Input")
                continue

            print("Goodbye")
            break
        
        # operations
        match operator:
            case "undo":
                if len(parts) != 1:
                    print("Invalid Input")
                    continue

                if history:
                    redo_history.append(total)
                    total = history.pop()
                    print("Result: ", total)
                else:
                    print("Nothing to undo")
                continue

            case "redo":
                if len(parts) != 1:
                    print("Invalid Input")
                    continue

                if redo_history:
                    history.append(total)
                    total = redo_history.pop()
                    print("Result: ", total)
                else:
                    print("Nothing to redo")
                continue


        
    
        if len(parts) != 2:
            print("Invalid Input")
            continue

        if operator not in ["+", "-", "*", "/"]:
            print("Invalid Operator")
            continue

        try:
            num = float(parts[1])
        except ValueError:
            print("Invalid number")
            continue


        
        match operator:
            case "+":
                history.append(total)
                total += num
                redo_history.clear()
                print("Total: ", total)
            case "-":
                history.append(total)
                total -= num
                redo_history.clear()
                print("Total: ", total)
            case "*":
                history.append(total)
                total *= num
                redo_history.clear()
                print("Total: ", total)
            case "/":
                if num == 0:
                    print("Cannot Divide by zero")
                else:
                    history.append(total)
                    total /= num
                    redo_history.clear()
                    print("Total: ", total)

calculator()