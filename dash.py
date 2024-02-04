# Vehicle dashboard program

# Display the menu.
menu = True

while True:
    user_choice = int(
        input(
            """\nWould you like to:\n
    1. View engine details
    2. View music selection
    3. View car analytics
    3. Quit application

    Enter selection: """
        )
    )