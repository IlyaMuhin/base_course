name = "Muhin Ilya"
name = '_'.join(name)
name = name.upper()
name_codes1 = [ord(symbol) for symbol in name]


name = name.lower()
name_codes2 = [ord(symbol) for symbol in name]

print(f'Max: {max(name_codes1 + name_codes2)}')
print(f'Min: {min(name_codes1 + name_codes2)}')
