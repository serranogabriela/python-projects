#  start by creating a variable and assigning it a randomly generated integer
#  between and inclusive of both 1 and 10.
#
# Then, using your knowledge of if, elif, and else statements, create a program which
# prints the roman numeral equivalent of the randomly generated number.
#
# For example, if the randomly generated integer was 9, then the program would say that
# the roman numeral equivalent of 9 is IX in the output.

import random
random_int = random.randint(1,10)
if random_int == 10:
    print(random_int, "the number ten in Roman numeral is X")
elif random_int == 9:
    print(random_int, "the number nine in Roman numeral is IX")
elif random_int == 8:
    print(random_int, "the number eight in Roman numeral is VIII")
elif random_int == 7:
    print(random_int, "the number seven in Roman numeral is VII")
elif random_int == 6:
    print(random_int, "the number six in Roman numeral is VI")
elif random_int == 5:
    print(random_int, "the number five in Roman numeral is V")
elif random_int == 4:
    print(random_int, "the number four in Roman numeral is IV")
elif random_int == 3:
    print(random_int, "the number three in Roman numeral is III")
elif random_int == 2:
    print(random_int, "the number two in Roman numeral is II")
else:
    print(random_int, "the number one in Roman numeral is I")
