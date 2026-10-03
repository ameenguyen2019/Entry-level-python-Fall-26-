"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Time Calculator
Date: 09/12/2026

Description:
    Write a program that asks the user to enter a number of seconds, 
    and then displays the total time entered in days, hours, minutes and seconds. 
    Only non-zero units should be displayed, and all units should be 
    separated by proper punctuation.

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
    input_seconds = int(input("Please enter a time in seconds: "))
    if input_seconds < 0:
        print("  Invalid Input!")
        exit()
    else:
        days = input_seconds // 86400
        hours = (input_seconds % 86400) // 3600
        minutes = (input_seconds % 3600) // 60
        seconds = input_seconds % 60
        time_units = []
        if input_seconds < 60:
            print(f"  {input_seconds} seconds is less than one minute.")
        elif input_seconds == 60:
            print(f"  {input_seconds} seconds equals 1 minute(s).")
        elif 60 < input_seconds < 240:
            print(f"  {input_seconds} seconds equals {minutes} minute(s) and {seconds} second(s).")
        elif 240 < input_seconds < 36000:
            print(f"  {input_seconds:,} seconds equals {hours} hour(s) and {seconds} second(s).")
        elif 36000 < input_seconds <= 86400:
            print(f"  {input_seconds:,} seconds equals {days} day(s). ")
        elif 86401 < input_seconds < 864000:
            print(f"  {input_seconds:,} seconds equals {days} day(s), {hours} hour(s), {minutes} minute(s) and {seconds} second(s). ")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
