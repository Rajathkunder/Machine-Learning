
def calculate_area_in_acres(length, width):
    
    area_in_square_feet = length * width
    area_in_acres = area_in_square_feet / 43560
    return area_in_acres


length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))


area_in_acres = calculate_area_in_acres(length, width)


print(f"The area of the field is {area_in_acres:.2f} acres.")
