# Reading a Txt file
try:
    file = open('sample.txt','r+')
    read_file = file.readline()
    read_file2 = file.readline()
    print("Reading the file content\n","Line 1 : ",read_file,"Line 2 : ", read_file2)
    file.close()
except FileNotFoundError:
    print("This File 'sample1.txt' Not Found ")
finally:
    print("Continue Code")


