'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def myFunction(truckCapacityUnits,packageListUnits):
    truckCapacityUnitsSimplified = truckCapacityUnits - 30
    resultSet=[]
    resultSetValue=[]
    
    for i in range(0,len(packageListUnits)):
        k = i+1
        for j in range(k,len(packageListUnits)):
            sumExpected = packageListUnits[i] + packageListUnits[j]
            if (sumExpected == truckCapacityUnitsSimplified):
                resultSetValue.append(packageListUnits[i])
                resultSetValue.append(packageListUnits[j])
                #print(max(resultSetValue))
                #print(str(packageListUnits[i]) +" , " + str(packageListUnits[j]))
                if ((packageListUnits[i]>= max(resultSetValue)) or (packageListUnits[j]>= max(resultSetValue))):
                    del resultSet[:]
                    resultSet.append(i)
                    resultSet.append(j)

    print(resultSet)
    #print(resultSetValue)
       
packageListUnits= [10,80,5,35,70,60,90,45,0,58,20,40]
truckCapacityUnits = 110

#print(len(packageListUnits))
myFunction(truckCapacityUnits,packageListUnits)
