fhr = open("Idata.txt", 'r')
rd = fhr.read().splitlines()
test = list()
check = ['what ', 'where ', 'why ', 'who ', 'when ', 'how ']
for i1 in rd:
    for i2 in check:
        if i2 in i1:
            test.append(i1)
fhw = open('Odata.txt', 'w')
fhw.flush()
for i1 in rd:
    for i2 in test:
        if i1 is i2:
            fhw.write(i1 + '        YES' + '\n')

    if i1 not in test:
        fhw.write(i1 + '        NO' + '\n')

fhr.close()
fhw.close()
