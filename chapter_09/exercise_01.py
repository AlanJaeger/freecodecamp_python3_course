#open a file and count how many time a word appears and print the word with the count.

from itertools import count


try:
    file_input = open('clown.txt')
except:
    print('There is no file with that name in folder.')
    quit()

word_dict = dict()

for line in file_input:
    split_lines = line.split()
    # print(split_lines)

    for word in split_lines:
        word_dict[word] = word_dict.get(word,0)+1
    
    print(word_dict)
    
    word = None
    counter = None
    #find the most common word
    for w,c in word_dict.items():
        if counter is None or c > counter:
            word = w
            counter = c
        # else:
        #     # print(c, "is not big than", counter)
            
    print(word,counter)