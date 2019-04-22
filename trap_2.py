
with open('forti_msg','r') as f:
    lines = f.readlines()


x = []

for l in lines:
    l =l.split()
    x.append(l[9])
print(''.join(x))