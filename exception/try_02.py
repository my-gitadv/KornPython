while True: 
    try:
        a = int(input("Enter a first_number: "))
        b = int(input("Enter a second_number: "))
    except:
        print("Invalid input. Please, enter a number")
        

    else:
        try:
            answer = a/b
            print(answer)

        except:
            print("Something went wrong!")

        else:
            print("Everything is fine!")
            break