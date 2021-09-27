with open('artifacts01.txt', 'r') as f:
    text = f.read()

with open('artifacts02.txt','w') as f:
    f.write('Content added at Stage 02')

print(text)
print('Message written in artifacts02.txt')
