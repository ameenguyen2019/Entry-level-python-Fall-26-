"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Roulette Color 
Date: 09/12/2026

Description:
    On a roulette wheel, the pockets are numbered from 
 to {math} 36. The colors of the pockets are as follows:
 Pocket 0 is green. For pockets 1 thorugh 10, the odd-numbered pockets are red 
 and the even-numbered pockets are black. For pockets 11 through 18, 
 the odd-numbered pockets are black and even-numbered pockets are red.
 For pockets 19 through 28, the odd-numbered pockets are red and 
 the even-numbered pockets are black. For pockets 29 through 36,
 the odd-numbered pockets are black and the even-numbered pockets are red.
 Write a Python program that asks the user to choose a pocket number, and 
 then displays the color of that pocket (either green, red, or black). 
 The program should display an error message if the user enters a number 
 that is outside the range of 0 through 36.

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
    input_pocket = int(input("Please choose a pocket number: "))
    if input_pocket < 0 or input_pocket > 36:
        print("  Invalid Input!")
        exit()
    else:
        if input_pocket == 0:
            print("  Pocket number 0 is green.")
        elif 1 <= input_pocket <= 10:
            if input_pocket % 2 == 0:
                print(f"  Pocket number {input_pocket} is black.")
            else:
                print(f"  Pocket number {input_pocket} is red.")
        elif 11 <= input_pocket <= 18:
            if input_pocket % 2 == 0:
                print(f"  Pocket number {input_pocket} is red.")
            else:
                print(f"  Pocket number {input_pocket} is black.")
        elif 19 <= input_pocket <= 28:
            if input_pocket % 2 == 0:
                print(f"  Pocket number {input_pocket} is black.")
            else:
                print(f"  Pocket number {input_pocket} is red.")
        elif 29 <= input_pocket <= 36:
            if input_pocket % 2 == 0:
                print(f"  Pocket number {input_pocket} is red.")
            else:
                print(f"  Pocket number {input_pocket} is black.")
        



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
