import numpy as np
f = open("data_rcr", "r")
p={}
size=[64, 576, 1536, 4096, 1024]
lines = f.readlines()
for line in lines:
    if (line.find(" implementation ") != -1):
        tag = line.strip("\n").split(" ")[7]
    if (line.find(" keybytes ") != -1):
        tag += "_"+line.strip("\n").split(" ")[7]
        p[tag]={}
    if (line.find(" compiler ") != -1):
        comp = line.strip("\n").split(" ")[7]
        p[tag]['compiler']=comp

  
    if (line.find("xor_cycle") != -1):
        b1 = line.strip("\n").split(" ")
        b = b1[7:]
        a=[]
        for i in b:
            a += [int(i)]
        #p[int(a[0])-1] = a[1:]
        if (a[0] in size):
            med = np.median(a[1:])/a[0]
            if ( a[0] in p[tag] ):
                if ( med < p[tag][a[0]]):
                    p[tag][a[0]] = med
            else:
                p[tag][a[0]] = med

for imp in p:
    print(imp, p[imp]['compiler'], p[imp][size[0]], p[imp][size[1]], p[imp][size[2]], p[imp][size[3]], ((p[imp][size[3]]*4096) - (p[imp][size[4]]*1024))/3072)
