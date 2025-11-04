while True:
    user_input = input("Enter something (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the loop. Goodbye!")
        break
    
    print(f"You entered: {user_input}")
