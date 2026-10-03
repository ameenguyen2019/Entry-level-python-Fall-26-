"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Interest 
Date: 09/05/2026

Description:
    Write a program to calculate the future value of an account given the initial deposit, 
    annual interest rate, number of years, and the number of times per year 
    that the interest is compounded.

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
    print("Enter the following parameters.")
    P = int(input("  The initial deposit? "))
    r = float(input("  The annual interest rate in percent? "))
    n = float(input( "  The number of years the account earn interest? "))
    t = float(input( "  The number of times interest is compounded each year: ")) 
    r = r / 100
    FV = P * (1 + r / t) ** (n * t)
    print(f"The balance of this account will be ${FV:,.2f} after {n} years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
