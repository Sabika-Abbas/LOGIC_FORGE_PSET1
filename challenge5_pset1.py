# Input:  "()())()"
# Output: ["(())()", "()()()"]

def fix_broken_expression(s):
    result=set()
    queue=[s]
    visited={s}
    while queue:
        current=queue.pop(0)
        if is_valid(current):
            result.add(current)
        else:
            for i in range(len(current)):
                new_expr=current[:i]+current[i+1:]
                if new_expr not in visited:
                    visited.add(new_expr)
                    queue.append(new_expr)
    if len(result)==0:
        return [""]  
    max_length=max(len(expr) for expr in result)
    return [expr for expr in result if len(expr)==max_length]




def is_valid(expression):
    count_paranthesis=0
    for i in expression:
        if i=="(":
            count_paranthesis+=1
        elif i==")":
            count_paranthesis-=1
        if count_paranthesis<0:
            return False
    return count_paranthesis==0
    

print(fix_broken_expression("()())()"))