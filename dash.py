# Vehicle dashboard program

from tabulate import tabulate

LI = 0
speed = 0
car_range = 0
RI = 0
# seatbelt_sensor = False


title = "\n\n\t\t+++++++++ VEHICLE DASHBOARD +++++++++\n"
table = [["LI", "Speed", "Range", "RI"], [LI, speed, car_range, RI]]


# Function to display a warning
def seatbelt_warning(seatbelt_sensor):
    if not seatbelt_sensor:
        print("\n\n\t\tDriver is not wearing a seatbelt\n")


# Display the menu.
menu = True

print(f"{title}\n")
print(tabulate(table, headers="firstrow", tablefmt="pretty"))

while True:
    seatbelt_warning(seatbelt_sensor=False)
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
    #     engine_details()

    # elif user_choice == 2:
    # music_selection()

    # elif user_choice == 3:
    # car_analytics()

    # elif user_choice == 4:
    # quit()
