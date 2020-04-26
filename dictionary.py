scores = {
    'John': 1200,
    'Bobby': 2000,
    'Janny': 4200
}

print(scores)
print(scores['Bobby'])

# เพิ่มสาชิกใหม่เข้า Dictionary
scores['roger'] = 3200

print(scores)

# การสร้าง Dictionary ว่าง
points = {}

# เพิ่มค่าเข้า Dictionary ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

# การ Loop อ่านสมาชิกของ Dicionary ออกมา
for k, v in scores.items():
    print(k, v)
