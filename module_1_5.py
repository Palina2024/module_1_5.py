immutable_var = [2, 4], 1, 3, 5.5, 'file', False
print(immutable_var)
immutable_var[0][0] = 1.5         # изменить элемент в кортеже можно, если этот элемент принадлежит изменяемому типу данных
print(immutable_var)
# immutable_var[2] = 4
# print(immutable_var)              # остальные элементы не поддаются изменению, так как tuple-это неизменяемый тип данных
mutable_list = [1, (3, 5.5), 'file', False]
print(mutable_list)
mutable_list[1] = 'string'
mutable_list.remove(1)
mutable_list.extend(['hello'])
print(mutable_list)


