my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}

my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = [0.25, 0.3, 0.5, 1, 1.5]
my_dict['dict'] = {
    'fruit': 'apple',
    'fruit1': 'banana',
    'fruit2': 'orange',
    'fruit3': 'peach',
    'fruit4': 'grape'
}
my_dict['set'] = {'window', 'door', 'floor', 'wall', 'ceiling'}

print(my_dict['tuple'][-1])

my_dict['list'].append(2)
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = (2, 4, 6, 8)
my_dict['dict'].pop('fruit')

my_dict['set'].add('man')
my_dict['set'].discard('wall')

print(my_dict)
