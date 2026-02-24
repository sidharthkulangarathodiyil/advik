import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('transparent 10%', 'transparent 15px')

with open('index.html', 'w') as f:
    f.write(content)

print("Fixed size!")
