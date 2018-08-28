import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Data1=pd.DataFrame([[0,75,99,9,35,63,8],[51,0,86,46,88,29,20],[100,5,0,16,28,35,28],[20,45,11,0,59,53,49],[86,63,33,65,0,76,72],[36,53,89,31,21,0,52],[58,31,43,67,52,60,0]],
columns=["A","B","C","D","E","F","G"], index=["A","B","C","D","E","F","G"])
Data1

X0 = ["B","A","C","D","F","E","G"] # intial solution , starts from A to G,then goes back to A

Distances = [] #The OF as a list of the basic intial solution that we gave

t=0
for i in range(len(X0)-1):
    X1 = Data1.loc[X0[t],X0[t+1]] #gives the value of the address in Data frame- that is 1,2 value in the matrix.
    X11 = Data1.loc[X0[-1],X0[0]] # the last city to first one
    Distances.append(X1)# keep adding the distances to the list.
    t=t+1

Distances.append(X11)#Append the distance of last city to first one
Length_of_Travel = sum(Distances)
print(Distances)
print(Length_of_Travel)


######Optimizing part now , where we use SA to get lowest possible distances

T0 = 3000
M = 2
N = 2
Alpha = 0.85

##For Graph visualisation
Temp = []
Min_Distance = []


for i in range(M):
    for j in range (N):
        #Random numbers to swap cities
        Ran1=np.random.randint(0,len(X0))
        Ran2=np.random.randint(0,len(X0))
        while Ran1==Ran2:
            R2=np.random.randint(0,len(X0))

        Xtemp = []
        A1 = X0[Ran1]
        A2 = X0[Ran2]
        ##the above is assigning the two random nos. to the cities in X0

        #Making a list of new cities
        w = 0
        for i in X0:
            if X0[w]==A1:
                Xtemp=np.append(Xtemp,A2)
            elif X0[w]==A2:
                Xtemp=np.append(Xtemp,A1)
            else:
                Xtemp=np.append(Xtemp,X0[w])
            w=w+1

        Xtemp=list(Xtemp)

        Distances_X0 = [] #The OF as a list for the original solution that we had established at the start

        t=0
        for i in range(len(X0)-1):
            X1_1 = Data1.loc[X0[t],X0[t+1]] #gives the value of the address in Data frame- that is 1,2 value in the matrix.
            X11 = Data1.loc[X0[-1],X0[0]] # the last city to first one
            Distances_X0.append(X1_1)# keep adding the distances to the list.
            t=t+1

        Distances_X0.append(X11)
        Len_X0 = sum(Distances_X0)

        
        Distances_Xtemp = [] #The OF as a list for the n+1 

        t=0
        for i in range(len(Xtemp)-1):
            X1_2 = Data1.loc[Xtemp[t],Xtemp[t+1]] #gives the value of the address in Data frame- that is 1,2 value in the matrix.
            X11 = Data1.loc[Xtemp[-1],Xtemp[0]] # the last city to first one
            Distances.append(X1_2)# keep adding the distances to the list.
            t=t+1

        Distances_Xtemp.append(X11) 
        Len_Xtemp = sum(Distances_Xtemp)


        rand_num = np.random.rand() #RN to check if it is greater or less or equal to the probability

        #The formula to check if we must accept the next worse move or no.

        form_1 = 1/(np.exp((Len_Xtemp-Len_X0)/T0))


        #Checking if Random var is greater or less than the Formula

        if Len_Xtemp <= Len_X0: #Them temp solution is better than our exisitng solution 
            X0 = Xtemp

        elif rand_num <= form_1:
            X0 = Xtemp

        else: #Do NOT accept the new solution , stay where you are .
            X0 = X0


    #The above loop runs N times 
    Temp = np.append(Temp,T0)  #for the graph , this is for each M run we store the Temp value and the corresponding L_Temp. 
    Min_Distance = np.append(Min_Distance,Len_Xtemp)

    T0 = Alpha*T0 #Temp reduces for every M
    #this loop will exit when we run it M times


print("Final Solution is :" , X0)
print("Minimized Distance is :" , Len_X0)


#Graphical visuals

plt.plot(Temp, Min_Distance)
plt.title("Distance vs Temperature", fontsize = 20, fontweight ='bold')
plt.xlabel("Temperature", fontsize = 18, fontweight = 'bold')
plt.ylabel("Distance", fontsize=18, fontweight = 'bold')
plt.xlim(3000,0)
plt.xticks(np.arrange(min(Temp), max(Temp), 100), fontweight = 'bold')
plt.yticks(fontweight = 'bold')
plt.show()




    

            



       
        





    

