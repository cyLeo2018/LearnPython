unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print('Printing model:{0}...'.format(current_design))
    completed_models.append(current_design)

print('The following models have been printed:')
for i in completed_models:
    print(i)

