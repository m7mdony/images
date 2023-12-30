import os
def check(labels):
    counter1=0
    counter2=0
    
    for fileanme in os.listdir(labels):
        filepath=os.path.join(labels,fileanme)
        with open(filepath,"r") as file:
            for line in file:
                line=line.split()
                if line[0]=="0":
                    counter1+=1
                elif line[0]=="1":
                    counter2+=1
    print(f' the annotations for 0 is {counter1}')
    print(f' the annotations for 1 is {counter2}')
labels="labels"

check(labels)