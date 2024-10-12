my_dict = {'Madina': 1994, 'Dilya': 1993}
print(my_dict)
print(my_dict['Madina'])
my_dict['Julia'] = 1997
print(my_dict)
my_dict.update({'Nastya': 2002,
                'Anya' : 1999})
print(my_dict)
#del my_dict ['Nastya']
a=my_dict.pop('Nastya')
print(a)
print(my_dict)
my_set = {'Dina', 0/4, 0, 3, 1, 9, 9, 4}
print(my_set)
my_set.update({5,'Dana'})
print(my_set.discard(1))
print(my_set)