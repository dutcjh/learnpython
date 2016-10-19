s1 = input('Please enter a string of lowercase letters: ')
s1 = s1.lower()
s2 = ''
for i in range(len(s1)-1):
    s2 += s1[i]
    if s1[i] > s1[i + 1]:
        s2 += ','
s3 = s2.split(',')
m = list(map(lambda x: len(x), s3))
idx = m.index(max(m))
print('Longest substring in alphabetical order is: '+s3[idx])
