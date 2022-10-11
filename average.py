total = 0
count = 0
while (True):
    inp = input('Enter one number from the user: ')
    if inp == 'done':
        break
    try:
        value = float(inp)
    except:
        print('Invalid input')
        continue
    total = total + value
    count += 1

average = total / count
print('Average:', average)
