def calculator():

    total = 0
    history = []

    # operations in a while loop
    while True:
        user_input = input("> ").strip()
        parts = user_input.split()

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
                    total = history.pop()
                    print("Result: ", total)
                else:
                    print("Nothing to undo")
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
                print("Total: ", total)
            case "-":
                history.append(total)
                total -= num
                print("Total: ", total)
            case "*":
                history.append(total)
                total *= num
                print("Total: ", total)
            case "/":
                if num == 0:
                    print("Cannot Divide by zero")
                else:
                    history.append(total)
                    total /= num
                    print("Total: ", total)

calculator()