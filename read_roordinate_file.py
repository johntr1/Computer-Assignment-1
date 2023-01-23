import numpy as np
def read_coordinate_file(filename):
    #Open file in read mode and get data
    with open(f'{filename}',mode='r') as file:
        line=file.readline()
        l=''
        while line:
            print(line)
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.replace('\n','')
            print(line)
            l=l+line
            print(l)
            line=file.readline()
    l=l.split(',')
    print(l)

read_coordinate_file('SampleCoordinates.txt')