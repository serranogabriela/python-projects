# For this programming challenge, you will be creating a function that calculates the volume
# of a rectangular prism in cubic feet. The formula to find the volume of a rectangular prism is
# V = l * w * h where l, w, and h are length, width, and height, respectively.

# First, create three variables representing length, width, and height.
# Assign each of them an integer as user input using the input() function and int().

# Next, create a function to calculate the volume of the rectangular prism.
# It should have 3 parameters representing length, width, and height and return the volume
# of a rectangular prism calculated using those 3 parameters.

# Finally, use print() to display
# "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.
# You will have to use str() on the function call to be able to concatenate
# it with strings since it returns an integer.

length = int(input("what is the length?"))
width = int(input("what is the width?"))
height = int(input("what is the height?"))


def prism_calculator(p1, p2, p3):
    return length * width * height


print("The volume of the rectangular prism is " + str(prism_calculator(length, width, height)) + " cubic feet.")


