# Problem 2
letters = input().strip().split()
accepted_words = {"node":3,"sun":2, "gone":4, "fondue":6, "hit":1,"car":2, "god":3, "put":1,"fee":4,"due":3,"end":2, "go":1, "done":4, "odeon":5, "bb":1}

##################################
##########YOUR CODE HERE##########
##################################

p2_part1 = None
p2_part2 = None
p2_part3 = None
print(p2_part2)
print(p2_part3)

# Below are 2 test cases.
# Uncomment one of the blocks to check your implementation. 

# Test 1
"""
# when the input is: a b c
assert set(p2_part1) == set(["a","b","c","aa","ab","ac","ba","bb","bc","ca","cb","cc","aaa","aab","aac","aba","abb","abc","aca","acb","acc","baa","bab","bac","bba","bbb","bbc","bca","bcb","bcc", "caa","cab","cac","cba","cbb","cbc","cca","ccb","ccc"])
assert p2_part2 == 1
assert p2_part3 == 1
assert p2_part2 == p2_part3
"""

# Test 2
"""
# when the input is: d e f o g n u
assert p2_part2 == 35 
assert p2_part3 == 35 
assert p2_part2 == p2_part3
"""