
def even(mn,mx):
    l = []
    for i in range (mn,mx):
        if(i % 2 == 0):
            l.append(i)
    print(l)
        
def getval():
    a = int (input("Enter your min number: "))
    b = int (input("Enter your max number: "))
    even(a,b)
    
getval()
    