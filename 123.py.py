import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import copy
I = mpimg.imread('C:/Users/Administrator/Desktop/image.png')
rows,cols=I.shape[:2]
for j in range(rows):
    I[j][cols-1]=1

def Find_Points(I):
    Points= []
    i=7
    j=100
    while i<rows-100:
        while j<cols-10:
            for m in range(i-2,i+3):
                for n in range(j-2, j+3):
                    r,g,b=I[m][n]

                    if r+g+b>2:
                        break
                if n<j+2:
                    break
            if m==i+2 and n==j+2:
                r,g,b=I[i][j-9]
                if r+g+b>2:
                    r,g,b=I[i-9][j]
                    if r+g+b >2:
                        Points.append([i,j])
            j+=5
        i+=5
        j=100
    return Points

def Find_All_Points_Vectors(Points):
    Points_Vectors = []
    for K in Points:
        i=K[0]
        j=K[1]
        m=1
        while sum(I[i-m][j])<2:
            m+=1
        a1=i-m
        while sum(I[i+m][j])<2:
            m+=1
        a2=i+m
        while sum(I[i][j-m])<2:
            m+=1
        a3=j-m
        while sum(I[i][j+m])<2:
            m+=1
        a4=j+m
        Points_Vectors.append([(a1+a2)//2,(a3+a4)//2])
    b=Points_Vectors
    k = []
    for i in range(len(b) - 1):
        for j in range(i + 1, len(b)):
            if abs(b[i][0] - b[j][0]) < 10 and abs(b[i][1] - b[j][1]) < 10:
                k.append(i)
    k = set(k)
    print(len(k))
    b_new = copy.deepcopy(b)
    for j in k:
        b.remove(b_new[j])
    return Points_Vectors

def Find_Special_Points_Vectors(Points_Vectors):
    b=Points_Vectors
    k=[]
    for i in range(len(b) - 1):
        for j in range(i + 1, len(b)):
            if abs(b[i][0] - b[j][0]) < 24 and abs(b[i][1] - b[j][1]) < 24:
                k.append(b[i])
                k.append(b[j])
    A=[]
    Special_Points_Vectors=[]
    for i in range(len(k) - 1):
        for j in range(i + 1, len(k)):
            if k[i][0]==k[j][0]:
                A.append(k[j])
    Special_Points_Vectors.append(A[3])
    Special_Points_Vectors.append(A[0])
    Special_Points_Vectors.append(A[6])
    return Special_Points_Vectors

def Find_Regular_Points_Vectors(Points_Vectors,Special_Points_Vectors):
    a=Points_Vectors
    b=Special_Points_Vectors
    a_new = copy.deepcopy(a)
    for j in a:
        for i in b:
            if i[0]==j[0]:
                a.remove(j)
    Regular_Points_Vectors=a
    return Regular_Points_Vectors


a=Find_Points(I)
b=Find_All_Points_Vectors(a)
c=Find_Special_Points_Vectors(b)
d=Find_Regular_Points_Vectors(b,c)
b=np.array(b)
c=np.array(c)
d=np.array(d)
x1=c[:,0]
y1=c[:,1]
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(y1, 750-x1, c='k', marker='.')
plt.ylim(80, 750)
plt.xlim(100, 1020)
x1=d[:,0]
y1=d[:,1]
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(y1, 750-x1, c='k', marker='.')
plt.show()
np.savetxt("C:/Users/Administrator/Desktop/Special_Points.txt", c,fmt='%d',delimiter=',')
np.savetxt("C:/Users/Administrator/Desktop/Regular_Points.txt", d,fmt='%d',delimiter=',')













