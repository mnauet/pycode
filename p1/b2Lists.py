import sys
import os
import random
grocery_list = ['Juice', 'Tomatoes',  'Potatoes', 'Bananas']
print('First Item : = ' , grocery_list[0])
print('print subset := ' , grocery_list[1:3])
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [grocery_list, other_events]
print(to_do_list)
print(to_do_list[0][1])
print(to_do_list[1][1])
grocery_list.append('Oninion')
print(to_do_list)
grocery_list.remove('Potatoes')
print(to_do_list)
grocery_list.sort()
print(to_do_list)
grocery_list.reverse()
print(to_do_list)
del to_do_list[1][2]
print(to_do_list)
