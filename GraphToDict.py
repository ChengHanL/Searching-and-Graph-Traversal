import json

fileName = input("Input txt file name (with format, i.e. roadNet-PA.txt): ")
f = open(fileName, "r")

#Find number of nodes listed in document
print("Estimating number of Nodes...")
for index, i in enumerate(f):
    if index == 2:
        numOfNode = i.split()[2]
        break

#Create numOfNodes number of keys
print("Creating Empty Dictionary...")
thisdict={}
for i in range(int(numOfNode)):
    thisdict[i] = []

next(f)

#Try catch used in case key is not created, key will then be created.
print("Compiling Dictionary...")
for i in f:
    thisline = i.split()
    try:
        thisdict[int(thisline[0])].append(int(thisline[1]))
    except:
        thisdict[int(thisline[0])]=[int(thisline[1])]

print("Dumping Dictionary to JSON...")
with open(fileName[:-4]+'.json', 'w') as fp:
    json.dump(thisdict, fp)

print("Done")