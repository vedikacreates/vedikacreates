# Take in Two Strings and Display the Larger String without Using Built-in Functions

str1 = 'Hello'
str2 = 'How are you'

count1 = 0
count2 = 0

for i in str1:
    count1 += 1
for i in str2:
    count2 +=1

if count1 > count2:
    print(str1)
else:
    print(str2)