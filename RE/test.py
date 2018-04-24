import re

text = "PythonTab.com is a good Python website"
m = re.match(r"(\w+)\s",text)
if m :
    print(m.group(0))
    print(m.group(1))
else:
    print('No match!')

n = re.search(r'\Pyt(on)n\s',text)
if n :
    print(n.group(0))
    print(n.group(1))
else:
    print('No match!')





