vocab = tuple('lowerbower')
print(vocab)
pair = ('o', 'w')

i = 0
result = []
while i < len(vocab):
    if i == len(vocab) - 1:
        result.append(vocab[i])
        i += 1
    elif vocab[i] == pair[0] and vocab[i+1] == pair[1]:
        result.append(pair[0] + pair[1])
        i += 2
    else:
        result.append(vocab[i])
        i += 1

print(result)

# voc = [('l', 'o', 'w'), ('l', 'o', 'w', 'e', 'r'), ('w', 'i', 'd', 'e', 's', 't'), ('n', 'e', 'w', 'e', 's', 't')]
# for i in voc:
#     print(len(i))
# print(sum([len(i) for i in voc]))

# voc2 = ('l', 'o', 'w')
# print(len(voc2))


# dct = {('l','o','w'):2, ('e','r'):1}
# print(dct)
# print(list(dct))
# print([letter for key in dct for letter in key])