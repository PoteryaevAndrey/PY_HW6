# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Пример:
# same_by(lambda x: x % 2, [2,4,6,8])
# Ответ: True

def same_by(characteristic, objects):
    temp = type(objects)
    return temp(filter(characteristic, objects)) == objects



print(same_by(lambda x: x % 2 == 0, [2, 4, 6, 8]))
print(same_by(lambda x: x % 2, [2, 4, 6, 8]))
print(same_by(lambda x: x % 2 == 0, {2, 4, 7, 8}))
print(same_by(lambda x: x > 2, [2, 4, 7, 8]))
print(same_by(lambda x: x > 2, (3, 4, 7, 8)))
print(same_by(lambda x: x < 9, {3, 4, 7, 8}))
print(same_by(lambda x: x < 9, {}))
print(same_by(lambda x: x < 9, (3, 4, 7, 9)))