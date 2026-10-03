"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Road trip
Date: 09/03/2026

Description:
    Write a program that estimates the round trip fuel cost for my trip. My program asks user to enter: the distance traveled, in miles, the average price of fuel in dollars per gallon, the fuel efficiency of your vehicle in miles per gallon

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
    print("Road trip fuel cost estimator:")
    distance = int(input("  How far away is your destination (miles)? "))
    price = float(input("  What is the average price of gas (dollars per gallon)? "))
    mpg = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))
    cost = 2 * (distance / mpg) * price
    print()
    print(f"The fuel cost for this trip is approximately ${int(cost)}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
