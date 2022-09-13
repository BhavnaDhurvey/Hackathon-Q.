def mini_max(list):
    max=0
    mini=list[0]
    i=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        elif list[i]<mini:
            mini=list[i]
        i=i+1
    mid=max-mini
    return mid
print(mini_max([1,2,3]))

# output 2