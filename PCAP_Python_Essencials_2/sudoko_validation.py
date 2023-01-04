"""NEED TO BE TESTED"""
rows = []
for row in range(9):
    rows.append(input())

desired_pattern = [x for x in range(1, 10)]
check = False
for row in rows:
    if sorted(row) == desired_pattern:
        check = True
    else:
        check = False
if check:
    print("Yes")
else:
    print("False")
