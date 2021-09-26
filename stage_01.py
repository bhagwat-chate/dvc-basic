text = 'Hello Data Version Control.'
text = text + ' DVC is working!'

with open('artifacts01.txt', 'w') as f:
    f.write(text)

print('Message written in artifacts01.txt')