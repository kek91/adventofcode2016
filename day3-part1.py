# adventofcode.com
# Day 3 - Part 1
# github.com/kek91

triangles = tuple(open("day3-input.txt", "r"))
triangles_amount = 0

for t in triangles:
    t = t.split(' ')
    t_1 = int(t[0])
    t_2 = int(t[1])
    t_3 = int(t[2])

    if (t_1 + t_2) > t_3:
        if (t_2 + t_3) > t_1:
            if (t_3 + t_1) > t_2:
                triangles_amount += 1

print(str(triangles_amount))
