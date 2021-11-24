l1 = [6545, 64544, 646464, 46451321, 61616, 61664]

print(l1[0])
print(l1[5])
print(l1[-1])

l2 = l1[1:5]
print(l1)
l2.append(653551)
print(l2)
l2.insert(3, 64446)
l2[1] = 5644
print(l2)


l3 = l2
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)


print('---------------')
print('')

l4 = [6465465, 6455, 6546494, 4965676, 215411, 'Hello Python 3', 646484]
print(l4)


# Extract the word 'Python' from l4
print(l4[5][6:12])
print(l4[5].split(' ')[1])

# Sum all number value of l4
l5 = l4[0:5] + l4[6:]
print(sum(l5))

my_sum = 0
for el in l4:
    if type(el)==int or type(el)==float:
        my_sum += el
print(my_sum)

l6 = [el for el in l4 if type(el)==int or type(el)==float]
sum_l6 = sum([el for el in l4 if type(el)==int or type(el)==float])
print(l6)
print(sum_l6)