

def soso_10(p,l):
    i=0
    string=""
    while i<l:
        d=str(p[i])
        e=d[-1]
        string=string+e
        i=i+1
    print(string)
    if (int(string)%10==0):
        return "yes"
    return "no"
p=[85,25,65,21,84]
l=len(p)
Q=soso_10(p,l)
print(Q)



# utput =
# 55514
# no