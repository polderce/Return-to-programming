small=True
green=True
cherry=small and not green
peas=green and small
watermelon=green and not small
pumpkin=not green and not small
if cherry == small and green:
    print('Соотвествует')
else:
    print('Не соответсвтует')
if peas == small and green:
    print('Соотвествует')
else:
    print('Не соответсвтует')
if watermelon == small and green:
    print('Соотвествует')
else:
    print('Не соответсвтует')
if pumpkin == small and green:
    print('Соотвествует')
else:
    print('Не соответсвтует')