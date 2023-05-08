"""import math module"""
import math

"""Defining area function"""
def calculate_area(shape, dimensions):
    
    """conditional statements"""
    if shape == 'rectangle':
        return dimensions[0] * dimensions[1]
    elif shape == 'square':
        return dimensions[0] ** 2
    elif shape == 'circle':
        return math.pi * dimensions[0] ** 2
    elif shape == 'triangle':
        return 0.5 * dimensions[0] * dimensions[1]
    elif shape == 'rhombus':
        return math.pi*4*dimensions[0]
    else:
        return None
    
    """def perimeter fn"""

def calculate_perimeter(shape, dimensions):
    
    """conditiona statement using list"""
    if shape == 'rectangle':
        return 2 * (dimensions[0] + dimensions[1])
    elif shape == 'square':
        return 4 * dimensions[0]
    elif shape == 'circle':
        return 2 * math.pi * dimensions[0]
    elif shape == 'triangle':
        return sum(dimensions)
    elif shape == 'rhombus':
        return 4(dimensions)
    else:
        return None
    
    """main function"""

if __name__ == '__main__':
    shape = input("Enter the shape (rectangle, square, circle, triangle): ")
    dimensions = []
    
    """function calling"""

    if shape == 'rectangle':
        dimensions.append(float(input("Enter the length: ")))
        dimensions.append(float(input("Enter the width: ")))
    elif shape == 'square':
        dimensions.append(float(input("Enter the side length: ")))
    elif shape == 'circle':
        dimensions.append(float(input("Enter the radius: ")))
    elif shape == 'triangle':
        dimensions.append(float(input("Enter the first side length: ")))
        dimensions.append(float(input("Enter the second side length: ")))
        dimensions.append(float(input("Enter the third side length: ")))
    elif shape== 'rhombus':
        dimensions.append(float(input("Enter the first side length: ")))    

    area = calculate_area(shape, dimensions)
    perimeter = calculate_perimeter(shape, dimensions)

    if area is not None and perimeter is not None:
        print(f"The area of the {shape} is {area:.2f} and the perimeter is {perimeter:.2f}")
    else:
        print("Invalid shape entered")