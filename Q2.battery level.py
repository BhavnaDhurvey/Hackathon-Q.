def fun(S,R,T):
    if S:
       print("yes")

    if R<S:
       print("yes")

    if T>S:
       print("no")
S=int(input("enter the number...."))
R=int(input("enter the number     "))  
T=int(input("enter the number   "))
fun(S,R,T)

# input 15,3,65   
# output  yes yes no