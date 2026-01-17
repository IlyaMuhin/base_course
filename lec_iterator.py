f = open('example.txt')


#readline - команда для чтения файла построчно
# print(f.readline(), end = '')
# print(f.readline(), end = '')
# print(f.readline(), end = '')

#метод __next__
print(next(f), end = '')
print(next(f), end = '')
# # print(next(f), end = '')

f2 = open('example2.txt')
for i in f2 : #Итератор файла
    print(i, end = '')


new_f = iter(f)
print(new_f)
f.close()
f2.close()