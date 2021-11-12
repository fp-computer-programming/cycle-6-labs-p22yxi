#  Author Yongdong XI (Nov 12 2021)

my_row = ["Satou", "Larry"]
my_row[2:] = ["Yongdong"]
print(my_row)

my_row2 = my_row

del my_row[1]

print(my_row)
print(my_row2)
