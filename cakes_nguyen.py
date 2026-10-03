"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Cakes
Date: 09/18/2026

Description:
    Write a Python program that asks the user to enter a number of layers, 
    and then uses nested loops to draw the ASCII art cake pattern 
    shown in the sample terminal below.

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
    value = int(input("Enter the number of layers: "))

    for i in range(1, value + 1):
        for j in range(value - i):
            print(" ", end="")

        print("[", end="")

        for j in range(2 * i - 1):
            print("*", end="")

        print("]")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
