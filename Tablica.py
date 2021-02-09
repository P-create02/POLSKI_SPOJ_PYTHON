a = input('')
output = ''
a_l = a.split(' ')
a_l.reverse()
for n in range(0, len(a_l), +1):
    if n == len(a_l)-1:
        output += a_l[n]
    else:
        output += a_l[n]+" "
print(output)
exit(0)
