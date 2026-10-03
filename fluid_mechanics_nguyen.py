"""
Author: Thi Mai Anh Nguyen, maianh.nguyen@purdue.edu
Assignment: 09.2026 - Fluid Mechanics 
Date: 09/13/2026

Description:
    The Reynolds number is a key parameter used to determine whether fluid flow will be laminar or turbulent. 
    For fluid flow through a pipe, the Reynolds number is given by where is the Reynolds number (a dimensionless value), 
    is the velocity or of the fluid, is the diameter of the pipe, or, and is the kinematic viscosity of the fluid or. 
    The kinematic viscosity, v, is a measure of the fluid’s resistance to flow and stress.
    Except when at extremely high pressures, a liquid fluid’s kinematic viscosity is dependent on temperature 
    and is independent of pressure. The following chart lists the kinematic viscosity of water at three different temperatures:

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
    input_temperature = int(input("  Enter the temperature in °C as 5, 20, or 50: "))
    V = float(input("  Enter the velocity of water in the pipe (m/s): "))
    d = float(input("  Enter the pipe's diameter (m): "))
    if input_temperature == 5:
        v = 1.519e-6
    elif input_temperature == 20:
        v = 1.004e-6
    elif input_temperature == 50:
        v = 0.553e-6
    R = (V * d) / v
    print(f"  At {input_temperature:.1f}°C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {R:.2e}.")







"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
