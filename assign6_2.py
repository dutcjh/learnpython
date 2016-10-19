s1 = input('Please enter a string of lowercase letters: ')
s1 = s1.lower()
s2 = s1[0]
s3 = ''
for i in range(len(s1)-1):
    if s1[i] <= s1[i + 1]:
        s2 = s2 + s1[i + 1]
    else:
        if len(s3) < len(s2):
            s3, s2 = s2, s1[i + 1]
        else:
            s2 = s1[i + 1]
if len(s3) < len(s2):
    s3 = s2
print('Longest substring in alphabetical order is: '+s3)
