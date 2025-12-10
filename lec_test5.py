name = 'Muhin Ilya Aleksandrovich'

name_list1 = list(name.upper())
name_codes1 = [ord(symbol) for symbol in name_list1]


name_list2 = list(name.lower())
name_codes2 = [ord(symbol) for symbol in name_list2]

print(f'Сумма кодов: {sum(name_codes1) + sum(name_codes2)}')