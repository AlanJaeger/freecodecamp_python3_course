#Write a program to read through a file and print the contents of line that begin with "from" and stract the third word using lists.

try:
    file_input = open('mbox-short.txt')
except:
    print('There is no file with that name in folder.')
    quit()


for line in file_input:
    line = line.rstrip()
    word_list = line.split()
    len_list = len(word_list)
    
    if line.startswith('From') and len_list > 2:
        third_word = word_list[2]
        print(third_word)