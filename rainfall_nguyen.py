"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Rainfall 
Date: 09/18/2026

Description:
    Write a Python program that uses nested loops to collect data and 
    calculate the average rainfall over a period of years. The program 
    should first ask for the number of years. The outer loop will iterate 
    once for each year. The inner loop will iterate twelve times, once for 
    each month. Each iteration of the inner loop will ask the user for the 
    inches of rainfall for that month. After all iterations, the program should 
    display the number of months, the total inches of rainfall, and the average 
    rainfall per month for the entire period. Format the precision of total and 
    average rainfall to 2.

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
    years = int(input("Enter the number of years: "))
    if years < 1:
        print(f"Invalid input; years must be greater than {years}. ")
    else: 
        total_rainfall = 0
        months = 0
        month_names = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", 
                       "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
        for year in range(years):
            print(f" For year No. {years} ")

            for month in range(12):
                rainfall = float(input(f"   Enter the rainfall for {month_names[month]}: "))

                while rainfall < 0:
                    print("   Invalid input; rainfall cannot be negative. ")
                    rainfall = float(input(f"   Enter the rainfall for month {month_names[month]}: "))

                total_rainfall += rainfall
                months += 1

            average_rainfall = total_rainfall / months
            print(f" There are {months} months. ")
            print(f" The total rainfall was {total_rainfall:.2f} inches. ")
            print(f" The monthly average rainfall was {average_rainfall:.2f} inches. ")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
