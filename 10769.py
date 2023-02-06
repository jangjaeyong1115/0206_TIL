msg = input()

happy = msg.count(':-)')
sad = msg.count(':-(')

if happy == 0 and sad == 0:
    print('None')

elif happy == sad :
    print('unsure')

elif happy > sad:
    print('happy')

elif happy < sad:
    print('sad')
