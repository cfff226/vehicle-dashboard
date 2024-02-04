# Vehicle dashboard program

from tabulate import tabulate

LI = 0
speed = 0
car_range = 0
RI = 0


title = "\n\t\t+++++++++ VEHICLE DASHBOARD +++++++++\n"
table = [["LI", "Speed", "Range", "RI"], [LI, speed, car_range, RI]]

print(f"{title}\n")
print(tabulate(table, headers="firstrow", tablefmt="pretty"))


# Display the menu.
menu = True

while True:
    user_choice = int(
        input(
            """\nWould you like to:\n
    1. View engine details
    2. View music selection
    3. View car analytics
    4. Quit application

    Enter selection: """
        )
    )
    # if user_choice == 1:

    # elif user_choice == 2:

    # elif user_choice == 3:

    # elif user_choice == 4:
