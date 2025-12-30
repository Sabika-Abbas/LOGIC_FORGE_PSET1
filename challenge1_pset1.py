# Input: contributions = [-1, 1, 0, -3, 3]
# Output: impact = [0, 0, 9, 0, 0]

def calculate_impact(contribution):
    n=len(contribution)
    if n==0:
        return []
    left_array=[1]*n
    right_array=[1]*n
    for i in range(1,n):
        left_sum=left_array[i-1]*contribution[i-1]
        left_array[i]=left_sum
    for j in range(n-2,-1,-1):
        right_sum=right_array[j+1]*contribution[j+1]
        right_array[j]=right_sum    

    impact=[]
    for x in range(n):
        impact.append(left_array[x]*right_array[x])
    
    return impact
contributions = [-1, 1, 0, -3, 3]
impact = calculate_impact(contributions)
print(impact)  # Output: [0, 0, 9, 0, 0]
