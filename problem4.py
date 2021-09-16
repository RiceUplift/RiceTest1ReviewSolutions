#Same code as problem 3, but with an additional while loop to verify the user input. See problem 3 for more comments.
counter = 2
prime = True
userInput = int(input("Enter a number between 50 and 500: "))

while counter <= 10:
    while (userInput<50) or (userInput>500): #Checks that the user input is between 50 and 500.
        userInput = int(input("Invalid number. Enter a number between 50 and 500: ")) #Asks for another value.
        #This while loop will continue until the user enters an integer between 50 and 500.
    if userInput%counter == 0:
        print(str(userInput) + " is divisible by " + str(counter))
        prime = False
    counter += 1

if prime:
    print("Your value is prime")