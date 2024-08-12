#I have performed 4 set operations avaliable here, considering 
#their exclusivness :D

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

union_set = s1.union(s2)
print("Union:",union_set)

intersection = s1.intersection(s2)
print("Intersection",intersection)

difference_set1 = s1.difference(s2)
print("Difference (s1 - s2):", difference_set1)

symmetric_difference_set = s1.symmetric_difference(s2)
print("Symmetric Difference:", symmetric_difference_set)
