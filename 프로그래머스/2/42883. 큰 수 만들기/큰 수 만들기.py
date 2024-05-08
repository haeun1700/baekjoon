def solution(number, k):
    answer = ''
    
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1 # 1
            stack.pop()
        stack.append(num) # 7, 7, 5, 8, 4, 1
    
    if k != 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
        
    return answer