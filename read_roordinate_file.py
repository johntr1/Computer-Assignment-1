import numpy as np
def read_coordinate_file(filename):
    #Open file in read mode and get data
    with open(f'{filename}',mode='r') as file:
        coors=file.read()
        print(coors)
        print('hej')

read_coordinate_file('SampleCoordinates.txt')