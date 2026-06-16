def generate_sandglass(n):
    for i in range(n):
        # Calculate the number of stars: 2 * (n - i) - 1
        stars = '*' * (2 * (n - i) - 1)
        # Calculate the number of leading spaces to center the stars
        spaces = ' ' * i
        # Add the centered row to the list
        sandglass.append(spaces + stars + spaces)
    
    # Create the lower half of the sandglass (excluding the narrowest row)
    for i in range(n - 1):
        # Calculate the number of stars: 2 * (i + 1) + 1
        stars = '*' * (2 * (i + 1) + 1)
        # Calculate the number of leading spaces for the lower half
        spaces = ' ' * (n - i - 2)
        # Add the centered row to the list, ensuring proper spacing
        sandglass.append(spaces + stars + spaces)
    return sandglass
