import random

flower_list = ['rose', 'sunflower', 'daffodil']
color_list = ['red', 'yellow', 'white','green','blue']
dictionary = {}



dictionary['rose'] = color_list[random.randint(0,4)]
dictionary['sunflower'] = color_list[random.randint(0,4)]
dictionary['daffodil'] = color_list[random.randint(0,4)]
print(dictionary)