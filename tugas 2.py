print('''
Harry Shabri
17220385''')
matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range(4):
    for j in range(4):
        if i==j:
            matriks[i][j]=i+1
        if i<j:
            matriks[i][j]=0
        if i>j:
            matriks[i][j]=i+1
for i in range(4): 
    print(matriks[i]) 