string = 'asadasfrwdgargregehtsrtjnytjyojhgoaPWERRAWogkrogeog'
pos = -1
lpos = string.rfind('o')
while pos != lpos:
    pos = string.find('o', pos+1)
    print(pos, end=' ')
