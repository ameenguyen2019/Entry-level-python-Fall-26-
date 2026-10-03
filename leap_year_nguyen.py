"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Leap Year
Date: 09/11/2026

Description:
    This program displays the number of days in February that year. 
    Use the following criteria to identify leap years:
    Determine whether the year is divisible by 100. 
    If it is then it is a leap year if and only if it is also divisible by 400.
    If the year is not divisible by 100, 
    then it is a leap year if and only if it is divisible by 4.

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
    year = int(input('Enter a year: '))

    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The year {year} is a leap year.')
            print(f'February of {year} has 29 days.')
        else:
            print(f'The year {year} is not a leap year.')
            print(f'February of {year} has 28 days.')
    else:
        if year % 4 == 0:
            print(f'The year {year} is a leap year.')
            print(f'February of {year} has 29 days.')
        else:
            print(f'The year {year} is not a leap year.')
            print(f'February of {year} has 28 days.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
