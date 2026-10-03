"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Organism 
Date: 09/18/2026

Description:
    Write a Python program that predicts the approximate size of a population 
    of organisms. The application should allow the user to enter the starting 
    number of organisms, the average daily population increase (as a percentage), 
    and the number of days the organisms will be left to multiply.

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
    start_population = float(input("Starting population, in thousands: "))
    increase = float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))
    population = start_population
    print("Day   Approx.Pop")

    for day in range(days + 1):
        print(f"{day:3d}{population:15,.3f}")
        population = population * (1 + increase / 100)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
