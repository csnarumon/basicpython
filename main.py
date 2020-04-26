# import ทั้งหมดทุกฟังก์ชั่น Module
#import numbers

#import มาบางฟังก์ชั้น
#from numbers import factorial, fibonacci
#import ทุกฟังก์ชั่น
#from numbers import *

# import และเปลี่ยนชื่อฟังก์ชั่น (alias)
from numbers import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

# print(factorial(5))
# print(fibonacci(100))

print(fa(5))
print(fi(100))
