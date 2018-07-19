# 29. Write a Python program to print out a set containing
# all the colors from color_list_1 which are not present in color_list_2.


def get_colors(set1, set2):
    return set([color for color in set1 if color not in set2])


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
unique_colors = get_colors(color_list_1, color_list_2)
print(unique_colors)
