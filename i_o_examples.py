# explaining file i/o


file_writer_object = open('random_file_name.txt', 'w') # this creates a new file in the same folder
#as this script

# this creates a file reader
# the os does the file reading/writing the file reader
# is python's way of asking the OS to do this

file_writer_object.write("This is some random stuff\n") # this asks the OS to write to our file
file_writer_object.write("This is some random stuff\n") 
file_writer_object.write("This is some random stuff\n\n\n\n\n") 
file_writer_object.write("This is some random stuff\n")


file_writer_object.close()  # this say save file and release to the general public



file_reader_object = open('random_file_name.txt', 'r') # this asks the os to allow us to read the contents of a file


# files are text strings separated by newlines

for line in file_reader_object:
    print(line)  # this is the same a repeatedly calling file_reader_object.readline()

file_reader_object.close()
print('_______________________________________________________')
file_reader_object = open('random_file_name.txt', 'r')
wholetext = file_reader_object.read()
print('_______________________________________________________')
print()
print(wholetext)


wholetext_list = wholetext.split('\n')

print('_______________________________________________________')
print(wholetext_list) # notice the error in the way we entered the file info



print('_______________________________________________________')


while '' in wholetext_list:
    wholetext_list.pop(wholetext_list.index(''))

print(wholetext_list)


for index in range(len(wholetext_list)):

    wholetext_list[index] = wholetext_list[index].split(' ')
    


print('_______________________________________________')

print(wholetext_list)

print('_______________________________________________')
print(f"{number1} behavior outer prebeahvior")

print('_______________________________________________')


# demystifying nested loops 

for number1 in range(3):
    print(f"{number1} behavior outer prebeahvior")
    # do some code
    print("output of prebehavior code" )
    for number2 in range(3):
        #do some code 
        print(f"{number2} inner loop")
        print("output of inner code")
    
    print(f"{number1} behavior outer post")
    # do some more code 
    print("output of post behavior code")










