# Section A: Code Review
Review of Option 2: java task 
Aim of the task: 
- In a file called recursion.java, create:
    1. recursive function that reverses a string
    2. a recursive function that, given a number n, prints out the first n Fibonacci numbers (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8...)

### Correctness
- First function: a recursive function that reverses a string
- - you were correct in intitally checking if the string was empty in line 27 and print out a message prompting the user that the input string to be reverse is empty in line 28
- - You did not declare another function reverseString that was called in line 33 
- - The fundamental idea of this reverseString function is to traverse the length of the input string, extract each character using the buildt in charAt function and append this to the  begining of a new empty string.

- Second function: a recursive function that, given a number n, prints out the first n Fibonacci numbers 
- -  

### Efficiency

### Style

### Documentation