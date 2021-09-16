counter = 2 #Starting at 2 since every number is evenly divisible by 1.
prime = True #A flag (bool) to let us tell the program if a number is prime.
#Initially we will assume the number is prime until we find a factor that shows it is composite.

userInput = int(input("Enter a number between 50 and 500: ")) #Makes our user input an integer.

while counter <= 10: #We only want factors up to 10.
    if userInput%counter == 0: #If the input mod counter is 0, then the input is evenly divisible by the counter.
        print(str(userInput) + " is divisible by " + str(counter))
        prime = False #If a factor is found, the number is not prime.
    counter += 1

if prime: #This is another way to write "if prime is True:" or "if prime == True".
    print("Your value is prime")

'''
Note that the computer has no idea what "prime" means as a variable name. To it, it's just a random assortment of 
characters. The same is true for the variable name "counter". Python doesn't know you mean to use it as a counter.
The same is true yet again for the user input prompt. Python doesn't automatically know you want a number between
50 and 500 or even that you want a number. All Python knows is that you want the user to input something. You have 
to be literal with what you want your code to do. Do not make the assumption that Python knows anything
about anything.
'''