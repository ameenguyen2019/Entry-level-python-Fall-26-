"""
Author: Thi Mai Anh Nguyen, nguy1764@purdue.edu
Assignment: 09.2026 - Lucky Sum
Date: 09/24/2026

Description:
    Write a function named lucky_sum that accepts two integer values as arguments. 
    The function should calculate and return the sum of the lucky numbers which are 
    all the numbers from the smallest argument to the largest argument that are divisible by 7.
 
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

def lucky_sum(first, second):
    total = 0
    start = min(first, second)
    end = max(first, second)

    for number in range(start, end + 1):
        if number % 7 == 0:
            total += number
    return total

def main():
    first = int(input('Enter the first integer: '))
    second = int(input('Enter the second integer: '))  
    result = lucky_sum(first, second)
    print(f"The sum of the lucky numbers is {result:,}.")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
