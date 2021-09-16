myInt = 0 #Our counter variable to loop through the integers.
mySum = 0 #Variable to hold the sum of the numbers we want. We start at 0 since we haven't added anything yet.

while myInt <= 1000000: #We only want integers up to 1 million. 
    if (myInt%3 != 0) and (myInt%7 != 0): #Checks that the number isn't divisible by 3 and isn't divisible by 7.
        mySum += myInt #Only ads to mySum if the value isn't divisible by 3 and isn't divisible by 7.
    myInt += 1 #Adds one to our counter to let us loop through the integers.

print(mySum) #Prints the final sum once the while loop is finished.