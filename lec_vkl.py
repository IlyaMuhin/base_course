symbols = 'Python'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes)  # список


symbols = 'Snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes)  

for object in symbol_codes:
    print(object)