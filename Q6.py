pizza: int = 4
slices: int = pizza * 8
people: int = 5
print('Each guest gets', slices // people , 'slices of pizza')
print('There are' , slices % people , 'slices left to claim' )