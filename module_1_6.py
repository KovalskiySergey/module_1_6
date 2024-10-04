my_dict = {'Sergey':1994,'Anna':1997}
print(my_dict)
print(my_dict.get('Sergey'), my_dict.get('Maxim'))
my_dict.update({'Alina': 1987, 'Artem': 1999})
a = my_dict.pop('Anna')
print(a)
print(my_dict)
my_set = {(1,2,3), True, 1,1,2,1,3, (1,2,3), (4,5,6)}
print(my_set)
my_set.update({6, False, 'Word'})
my_set.discard(True)
print(my_set)
