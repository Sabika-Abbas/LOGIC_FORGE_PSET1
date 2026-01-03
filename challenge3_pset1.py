# Input:  scoresA = [1, 3], scoresB = [2]
# Output: 2.0

def balanced_performance(scoresA, scoresB):
    m=len(scoresA)
    n=len(scoresB)
    total=m+n
    i=j=0
    count=0
    prev=curr=None
    while count<=total//2:
        if i<m and (j>=n or scoresA[i]<=scoresB[j]):
            curr=scoresA[i]
            i+=1
        else:
            curr=scoresB[j]
            j+=1
        count+=1
        if count==total:
            prev=curr

    if total%2==0:
        return (prev+curr)/2
    else:
        return float(curr)
    

print(balanced_performance([1,4,6,8],[2,3,7]))