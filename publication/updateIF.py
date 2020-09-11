
import os

directory = '.'
str_to_find = "Impact Factor: 3.331"
str_to_replace = "Impact Factor: 4.778"

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        with open(os.path.join(directory, filename)) as f:
            s = f.read()
            s = s.replace(str_to_find, str_to_replace)
        with open(os.path.join(directory, filename), 'w') as f:
            f.write(s)
