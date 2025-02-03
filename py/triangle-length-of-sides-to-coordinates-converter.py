# Define a function named 'test' that takes a list 'sides' representing the side lengths of a triangle
def test(sides):
    # Sort the side lengths in ascending order and assign them to variables a, b, and c
    a, b, c = sorted(sides)
    
    # Calculate the semi-perimeter of the triangle
    s = sum(sides) / 2
    
    # Use Heron's formula to calculate the area of the triangle
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    # Calculate the height of the triangle
    y = 2 * area / a
    
    # Calculate the x-coordinate of the third vertex using the Pythagorean theorem
    x = (c ** 2 - y ** 2) ** 0.5
    
    # Return the coordinates of the vertices of the triangle as a list of lists
    return [[0.0, 0.0], [a, 0.0], [x, y]]

# Assign a specific list of side lengths 'sides' to the variable
sides = [3, 4, 5]

# Print the side lengths of the triangle
print("Sides of the triangle:", sides)

# Print a message indicating the operation to be performed
print("Coordinates of a triangle with the said side lengths:")

# Print the result of the test function applied to the 'sides' list
print(test(sides))

# Assign another specific list of side lengths 'sides' to the variable
sides = [5, 6, 7]

# Print the side lengths of the triangle
print("\nSides of the triangle:", sides)

# Print a message indicating the operation to be performed
print("Coordinates of a triangle with the said side lengths:")

# Print the result of the test function applied to the 'sides' list
print(test(sides))
