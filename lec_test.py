a = {1: 'sfff', 2: "fafasfafa"}
print(a[1])
for i in range(3):
    a[f'Human{i+1}'] = 'fafafsaf'
print(a)
del a[f'Human{1}']
print(a)