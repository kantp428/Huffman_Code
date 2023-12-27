with open('Pathcode.txt', 'r') as file:
    path_string = file.read()

with open('Encode.txt', 'r') as file:
    encode = file.read()

pairs = path_string[1:-1].split(', ')
pathcode = {}
for x in pairs:
    key, value = x.split(': ')
    pathcode[key.strip("'")] = value.strip("'")

Decode = ''
code = ''
while len(encode) > 0:
    code += encode[0]
    encode = encode[1:]
    for key, value in pathcode.items():
        if code == value:
            Decode += key
            code = ''
print("Decode:",Decode)
with open('Decode.txt', 'w') as file:
    file.write(str(Decode))