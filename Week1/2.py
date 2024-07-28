# Function to calculate the area of the room
def calculate_area(length, width):
    
    return length * width


length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))


area = calculate_area(length, width)


print(f"The area of the room is {area:.2f} square meters.")
