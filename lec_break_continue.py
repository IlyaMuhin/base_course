for symbol in 'hello world':
    if symbol == 'o':
        break
    print(symbol)

for symbol in 'hello world':
    if symbol == 'o' or symbol == "l":
        continue
    print(symbol)