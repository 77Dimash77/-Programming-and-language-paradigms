from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, sum_list, element, add')

(sum_list[X] == 0) <= (element[X] == False)

(sum_list[X] == Y) <= (element[X] == True, add(X, Z, Y), element[Z] == True)

(add(X, Y, Z)) <= (Z == X + Y)

my_list = [1, 2, 3, 4, 5]

for index, value in enumerate(my_list):
    element[index + 1] = True


print(sum_list[X] == Y)
