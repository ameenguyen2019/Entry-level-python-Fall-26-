"""
Author: Thi Mai Anh Nguyen, nguy1764@purdue.edu
Assignment: 09.2026 -  Prime List
Date: 09/24/2026

Description:
    Describe your program here.

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
    limit = int(input("Enter a positive integer: "))
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(str(number))
    print("The primes up to", limit, "are:", ", ".join(primes))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
