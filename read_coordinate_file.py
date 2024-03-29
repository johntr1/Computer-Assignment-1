# Function name: read_coordinate_file
# Input: File with the data for the coordinates given in degrees
# Output: An array with the coordiantes given in x and y format


import numpy as np


def read_coordinate_file(filename):
    #Open file in read mode and get data
    with open(f'{filename}',mode='r') as file:
        line=file.readline()
        #An empty string that can save the degree coordinates in
        l=''
        while line:#A while loop for each line in the file
            #Removes everything that't not a number or a .
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.replace('\n',',')
            #Adds it to a long string
            l=l+line
            line=file.readline()
    #Splits the string and removes the last string which is empty
    l=l.split(',')
    l.pop()
    #Defines the right shape of the array and makes it with float as values
    shape=(int(len(l)/2),2)
    ab=np.empty(shape, dtype=float)
    n=0
    #A for loop that fills the array with as [a b] from the list made
    for i in l:
        i=float(i)
        if n%2==0:
            ab[int(n/2)][0]=i
        else:
            ab[int(n/2)][1]=i
        n+=1
    R=1
    coor=np.zeros(shape, dtype=float)
    print(ab)
    for a in range(len(ab)):
        coor[a][0]=R*np.pi*ab[a][1]/180
        coor[a][1]=R*np.log(np.tan(np.pi/4 + np.pi*ab[a][0]/360))
    print('coor')
    print(coor)
    return coor


