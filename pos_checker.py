def positive(lst):
    numbers = [num for num in lst if num > 0]
    return numbers

list1 = [12, -7, 5, 64, -14]
scene1 = positive(list1)
print(f"Input: list1 = {list1} Output: {scene1}")

list2 = [12, 14, -95, 3]
scene2 = positive(list2)
print(f"Input: list2 = {list2} Output: {scene2}")

