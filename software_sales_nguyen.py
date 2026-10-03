"""
Author: Thi Mai Anh Nguyen , maianh.nguyen@purdue.edu
Assignment: 09.2026 - Software Sales
Date: 09/12/2026

Description:
    A software company sells a package that retails for $880. 
    Quantity discounts are given. Write a Python program that asks 
    the user to enter the number of packages purchased. 
    The program should then display the amount of the discount 
    (if any) and the total amount of the purchase after the discount.

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
    #Constants:
    PACKAGE_PRICE = 880
    DISCOUNT_10 = 0.1
    DISCOUNT_15 = 0.15
    DISCOUNT_30 = 0.3
    DISCOUNT_42 = 0.42
    input_packages = int(input("How many packages will be purchased: "))
    if input_packages < 0:
        print("  Invalid input!")
        exit()
    else:
        if 4 <= input_packages < 39:
            discount = DISCOUNT_10
            print("  10% discount applied.")
        elif 40 <= input_packages < 199:
            discount = DISCOUNT_15
            print("  15% discount applied.")
        elif 200 <= input_packages < 999:
            discount = DISCOUNT_30
            print("  30% discount applied.")
        elif input_packages > 1000:
            discount = DISCOUNT_42
            print("  42% discount applied.")
        else:
            discount = 0
            print("  No discount applied.")
    total_price = input_packages * PACKAGE_PRICE * (1- discount)
    print(f"  The total price to purchase {input_packages} packages is ${total_price:,.2f}.")
    




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
