#create a list of most commum words and sort by the values.
try:
    file_input = open('clown.txt')
except:
    print('There is no file with that name in folder.')
    quit()

word_dict = dict()
ordering = list()

for line in file_input:
    lines = line.split()
    for word in lines:
        word_dict[word] = word_dict.get(word, 0) + 1

for c,v in word_dict.items():
    ordering.append((v,c))
    order_tuple = sorted(ordering, reverse=True)

for v,k in order_tuple[:5]:
    print(k,v)

# print(order_t[:5])
# print(sorted(ordering, reverse=True)[:5])
