grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = list(students)
a.sort()
print(a)
dlina1 = len(grades[0])
dlina2 = len(grades[1])
dlina3 = len(grades[2])
dlina4 = len(grades[3])
dlina5 = len(grades[4])

ocenka1 = sum(grades[0])/dlina1
ocenka2 = sum(grades[1])/dlina2
ocenka3 = sum(grades[2])/dlina3
ocenka4 = sum(grades[3])/dlina4
ocenka5 = sum(grades[4])/dlina5

#a.insert(1, ocenka1)
#a.insert(3, ocenka2)
#a.insert(5, ocenka3)
#a.insert(7, ocenka4)
#a.insert(9, ocenka5)
print(ocenka1, ocenka2, ocenka3, ocenka4, ocenka5)
# Последовательность копирую из консоли не нашел способа выводит в терминал собранный список переменных
b = {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
print(b)


result = {}
for i in range(len(a)):
    result[a[i]]=sum(grades[i])/len(grades[i])
print(result)

