# Section A: Code Review
Review of Option 2: java task 
Aim of the task: 
- In a file called recursion.java, create:
    1. recursive function that reverses a string
    2. a recursive function that, given a number n, prints out the first n Fibonacci numbers (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8...)

### Correctness
- First function: a recursive function that reverses a string
    - You were correct in intitally checking if the string was empty in line 20 and print out a message prompting the user that the input string to be reverse is empty in line 21
    - You did not declare another function reverseString that was called in line 26
    - The fundamental idea of this reverseString function is to traverse the length of the input string, extract each character using the buildt in charAt function and append this to the  begining of a new empty string.

- Second function: a recursive function that, given a number n, prints out the first n Fibonacci numbers 
    - Incorrect function declaration on line 28, there was no need to use a genric function can just use a public static void function as your function does not return a value. 
    - The declared function (line 28) was never called in the main function
    - You duplicated the maxNumber variable, line 30, it would be better to utilise a default value for maxNumber if one was not provided on the function call instead of redeclaring the variable. 
    - Your for loop (line 36) needed to be indented to form part of the function. 
    - The rest of the function to print out the first n Fibonacci numbers will work correctly, well done!

### Efficiency
- The reverseString loop, called on line 26, could have been written in the reverse_string function after the empty string check there was no need to call on an additional function. 
- As mentioned in the correctness section you could just use a void function for the Fibonacci sequence with a default parameter (line 28) for maxNumber if one is not given when calling the function.  

### Style
- Class names should begin with a capital letter i.e Recursion class in line 1 
- Correct Naming conventions utilised for variables 
- For loop on line 36 shoudl be indented

### Documentation
Good use of documentation overall a  few poitners though:
    - comment on line 5 is unnecessary, the varibale name tells the user that it is the input string
    - comment on line 9 is vague what mehtod is being created and what parameter is being passed?  
    - no comment explaining the responsibility of the function on line 28
    - good comment explain the for loop on lines 38-40, you can also utilsie a multi-lien comment using /* **insert comment here** */ 

## Overall comment
This is a good attempt and solving the two functions required with a few improvements mentioned above. Please feel free to ask if you need any clarity. 