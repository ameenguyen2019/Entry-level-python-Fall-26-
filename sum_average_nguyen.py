"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Sum Average
Date: 09/18/2026

Description:
    Write a Python program with a loop that asks the user to enter a series 
    of non-negative numbers (positive numbers or zero). The user should 
    enter a negative number to signal the end of the series. 
    After all the non-negative numbers have been entered, 
    the program should display their sum and average.
    
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


def main():
    """Write your mainline logic below this line (then delete this line)."""
    total = 0
    count = 0
    number = float(input("Enter a non-negative number (negative to quit): "))
    while number >= 0:
        total += number
        count += 1
        number = float(input("Enter a non-negative number (negative to quit): "))
    if count > 0:
        average = total/ count
        print(f"  You entered {count} numbers. ")
        print(f"  Their sum is: {total:.3f} and their average is {average:.3f}. ")
    else:
        print(" You didn't enter any numbers. ")

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
