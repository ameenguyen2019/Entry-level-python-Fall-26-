"""
Author: Thi Mai Anh Nguyen, nguy1764@purdue.edu
Assignment: 09.2026 -  Average Grade Assignment
Date: 09/24/2026

Description:
    Write a program that asks the user to enter a valid score five times. 
    The program should display a letter grade after each score is entered. 
    After all the scores are entered, it should display the average of the scores 
    and the letter grade corresponding to that average. Complete your program by 
    writing the following three functions and calling them from within your main function.


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


def get_valid_score():
    score = float(input("Enter a score: "))
    while score < 0 or score > 100:
        print("  Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    return score #after the loop

def calc_average(scores):
    return sum(scores) / len(scores)

def determine_grade(score):
    if score >= 92:
        return "A"
    elif score >= 82:
        return "B"
    elif score >= 73:
        return "C"
    elif score >= 64:
        return "D"
    else:
        return "F"

def main():
    scores = []

    for i in range(5):
        score = get_valid_score()
        scores.append(score)
        grade = determine_grade(score)
        print(f"  The letter grade for {score:.1f} is {grade}.")
    average = calc_average(scores)
    average_grade = determine_grade(average)

    print()
    print(f"Results:")
    print(f"  The average score is {average:.2f}.")
    print(f"  The letter grade for {average:.2f} is {average_grade}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
