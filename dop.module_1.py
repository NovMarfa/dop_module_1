grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list (students)
students.sort()  # изменяет список на месте
print(students)

gr0 = [5, 3, 3, 5, 4]
mid0 = sum(gr0) / len(gr0)   # вычисление ср. ариф. sum - сумма всех эл-тов; len - кол-во эл-тов в списке
print(mid0)
gr1 = [2, 2, 2, 3]
mid1 = sum(gr1) / len(gr1)
print(mid1)
gr2 = [4, 5, 5, 2]
gr3 = [4, 4, 3]
gr4 = [5, 5, 5, 4, 5]
mid2 = sum(gr2) / len(gr2)
mid3 = sum(gr3) / len(gr3)
mid4 = sum(gr4) / len(gr4)
print(mid2)
print(mid3)
print(mid4)
mid = [mid0, mid1, mid2, mid3, mid4]
# zip - поэлементно (по столбцам) проходит по каждому списку
# dict - преобразование в словарь
journal = dict(zip(students, mid))
print(journal)