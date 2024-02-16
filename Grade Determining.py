# write a program which will determine the grades of the class's students.
# Her grading scale is as follows:
#     A score of 90 or above is an A
#     A score of 80 or above is a B
#     A score of 70 or above is a C
#     A score of 60 or above is a D
#     A score any lower is an F
#
# For this exercise, start by creating a variable and assigning that variable a student's
# score as an integer using input().
# Then, using nested if and else statements and the following set of rules, determine
# and then display the student's grade along with their score using print().
#
# Make sure to run your program multiple times and test it with values for each 5 of
# the different grades to make sure that the correct output is displayed for any value
# entered as a student's score.

GPA = int(input("What's the student grade point?"))

if GPA >= 90:
    print("the student got an A")
else:
    if GPA >= 80:
        print("the student got an B")
    else:
        if GPA >= 70:
            print("the student got an C")
        else:
            if GPA >= 60:
                print("the student got an D")
            else:
                print("the student got an F")
