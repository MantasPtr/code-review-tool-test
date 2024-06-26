PI = 3.141592653589793

def calculate_area(radius):
    # Calculates the area of a circle
    area = PI * radius**2
    return area

def calculate_volume(radius, height):
    # Calculates the volume of a cylinder
    base_area = PI * radius**2
    if base_area < 0:
        return -1
    volume = base_area * height
    return volume

def calculate_circumference(radius):
    # Calculates the circumference of a circle
    circumference = 2 * PI * radius
    return circumference

def main():
    radius = 5
    height = 10

    circle_area = calculate_area(radius)
    print("Area of the circle:", circle_area)

    cylinder_volume = calculate_volume(radius, height)
    print("Volume of the cylinder:", cylinder_volume)

    circle_circumference = calculate_circumference(radius)
    print("Circumference of the circle:", circle_circumference)

if __name__ == "__main__":
    main()
