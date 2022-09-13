def Anagrams():
    str1=sorted(name1)
    str2=sorted(name2)
    if str1==str2:
        print("it is a anagrams:  ")
    else:
        print("it is not anarams:  ")

name1=input("enter the name")
name2=input("enter the name")
Anagrams()

# input abcd , bcad 
# output it is Anagrams

# input zxcv bzxc 
# output it is not Anagrams