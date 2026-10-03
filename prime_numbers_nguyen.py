"""
Author: Thi Mai Anh Nguyen, nguy1764@purdue.edu
Assignment: 09.2026 -   Prime Numbers
Date: 09/24/2026

Description:
    A prime number is a number (not including 1) that is only evenly divisible by two numbers: 
    itself and 1. For example, the number 5 is prime because it can only be evenly divided by 1
    and 5. The number 6, however, is not prime because it can be divided evenly by 1,2,3,6.
    Write a Boolean function named is_prime which takes an integer as an argument and returns 
    True if the argument is a prime number, or False otherwise. Then, in the main function, 
    prompt the user to enter a number. If the user enters -1, end the program. Otherwise, 
    display a message indicating whether the number is prime, using your is_prime function to 
    decide which message to display.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) +1):
        if number % i == 0:
            return False
    return True
        
def main(): 
    number = int(input("Enter a positive integer (-1 to quit): "))
    while number != -1:
        if is_prime(number):
            print("  " + str(number) + " is prime!")
        else:
            print("  " +  str(number) + " is not prime.")
        number = int(input("Enter a positive integer (-1 to quit): "))
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
