# การสร้างฟังก์ชั่นแบบ no return value
def hello(name):
    print(f"Hello {name}")


# สร้างฟังก์ชันแบบมีการ return value
def area(width, height):
    total = width*height
    return total


 # เรียกใช้งานฟังกชั่น hello()
hello("Narumon")

# เรียกใช้งานฟังกชั่น area()
print(area(5, 8))
print("พื้นที่ทั้งหมด", area(15, 7.5))
print()


# ฟังก์ชั่นแบบมีค่าเริ่มค้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Laguage: {lang}")


# เรียกใช้งานฟังก์ชั่น show_info()
show_info()
print()
show_info('Narumon', 12000, 'PHP')
