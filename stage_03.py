
with open('artifacts01.txt', 'r') as f:
    text = f.read()

with open('artifacts03.txt', 'w') as f:
    text = f.write('This is artifacts03.txt file')

print(text)
print('Content added at Stage 03')