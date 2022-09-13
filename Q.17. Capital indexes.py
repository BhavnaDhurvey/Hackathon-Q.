
def dad():
    a="HeLlO"
    i=0
    Uppercase=0
    Lowercase=0
    d=[]
    while i<len(a):
        if a[i].isupper():
            Uppercase+=1
        elif a[i].islower():
            Lowercase+=1
          
        d.append(Lowercase,Uppercase)
        i=i+1
       
    print(d)
dad()
