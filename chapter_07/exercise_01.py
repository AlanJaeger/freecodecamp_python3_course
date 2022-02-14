#Write a program to read through a file and print the contents of the file (line by line) all in upper case.
#Executing the program will look as follows:
#in addiction of the exercise, i put a try except verification and a counter for lines in file

try:
    file_input = open('mbox-short.txt')
except:
    print('there is no file with that name in folder')
    quit()
    
line_count = 0

for line in file_input:
    line_count += 1
    line_without_blank_line = line.rstrip()
    print(line_without_blank_line.upper())

print('this file have',line_count, 'lines')