k = input('enter the string ')
output=""
for i in k:
    if i not in output:
        output += i

print(output)