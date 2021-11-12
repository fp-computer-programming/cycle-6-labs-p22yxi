#  Author Yongdong XI (Nov 12 2021)

colors = ['yellow', 'blue', 'red', 'green']
colors.extend(['yellow', 'pink', 'white'])
print(colors)

print(colors.count('yellow'))

colors.insert(3, "black")
print(colors)

colors.clear()
print(colors)

print(colors.count('red'))
