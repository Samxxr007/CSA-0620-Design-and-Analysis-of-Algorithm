arr = [1,2,3,4,5]
n=4
for i in range(len(arr)):
    if arr[i]==n:
        print("Match Found at Index",i)
        break;
else:
     print("Match not Found")