print("----------------------")
print("# Summation Pogram")
print("# Type 'exit' to end the pogram")
print("----------------------")


# ตัวแปรไว้เก็บผลรวม
sumdata = 0
count = 1

while True:
    data = input(f"Enter number {count}: ")
    # รวจว่าผู้ใช้ป้อน 'exit'
    if data == 'exit':
        break
    # การหาผลรวม
    sumdata += int(data)
    count = count+1

print(f"Sum value is {sumdata}")
