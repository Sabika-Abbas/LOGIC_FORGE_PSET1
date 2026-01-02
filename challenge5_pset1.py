# Input:  "()())()"
# Output: ["(())()", "()()()"]

def fix_broken_expression(s):
    output=[]
    if is_valid(s):
        output.append(s)
        return output
    if s[-1]=="(" :
        s=s[:-1]
    if s[0]==")":
        s=s[1:]
    for i in range(len(s)):
        if s[-1]=="(" :
            s=s[:-1]
        if s[0]==")":
            s=s[1:]
        new_expression=s[:i]+s[i+1:]
        if is_valid(new_expression) and new_expression not in output:
            output.append(new_expression)
    return output
    
def is_valid(expression):
    count_paranthesis=0
    for i in expression:
        if i=="(":
            count_paranthesis+=1
        elif i==")":
            count_paranthesis-=1
    if count_paranthesis==0:
        return True
    return False
    

print(fix_broken_expression("()())()"))