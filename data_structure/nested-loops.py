nested_lists = [
    [1,2,3], # 0
    [2,3,4], # 1
    [5,6,7], # 2
    [8,9,10] # 3
]

for index, items in enumerate(nested_lists):
    for childitem in items:
        print(f"Parent Index [{index}], child Item [{childitem}]")

