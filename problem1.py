# Problem 1
names = input().strip().split()
numbers = input().strip().split()
phonebook = dict(zip(names, numbers))
add, shift = map(int, input().strip().split())

##################################
##########YOUR CODE HERE##########
##################################

p1_part1 = None 
p1_part2 = None
print(p1_part1)
print(p1_part2)

"""
# Test case with inputs:
# alex edward lily jason
# 4875740312 5749402178 2083640912 0000099999
# 2 1
assert p1_part1 == {'alex': '4609796253', 'edward': '0796162439', 'lily': '4420586213', 'jason': '1222221111'}
assert p1_part2 == {'alex': '4875740312', 'edward': '5749402178', 'lily': '2083640912', 'jason': '0000099999'}
assert p1_part2 == phonebook 
"""

