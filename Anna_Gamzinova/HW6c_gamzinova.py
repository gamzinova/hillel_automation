# Counting how many times each letter appears in this file

import re

with open("text.txt", "r") as file:
    text = file.read()
# all the special symbols and digits removed
text_updated = re.sub(r'\W|\d', r'', text)

for letter in sorted(set(text_updated)):
    print(f'{letter}: {text_updated.count(letter)}')

