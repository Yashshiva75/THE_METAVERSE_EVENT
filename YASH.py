import math

# Function to calculate the volume of a regular octangonal prism
def octagonal_prism_volume(side_length, height):
    # Calculate the area of the octagonal faces
    face_area = 2 * side_length**2 *(1 + math.sqrt(2))

    # Calculate the volume of the prism by multiplying the face area by the height
    volume = face_area * height
    
    return volume
# Input the side length and height from the user
side_length = float(input("Enter the side lenght of the octagon: "))
height = float(input("Enter the height of the prism: "))

# Calculate and print the volume
volume = octagonal_prism_volume(side_length, height)
print(f"The volume of the regular octagonal prism is {volume:.2f} cubic units")