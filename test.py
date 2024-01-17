import itertools

def backtrack(stack, remaining):
    if not remaining:
        return 1 if not stack else 0
    
    result = 0
    for i in range(len(remaining)):
        new_stack = stack[:]
        new_remaining = remaining[:i] + remaining[i+1:]
        
        # 模拟 4 先出栈
        if remaining[i] == 4:
            result += backtrack(new_stack, new_remaining)
        # 其他元素正常入栈
        else:
            result += backtrack(new_stack + [remaining[i]], new_remaining)
    
    return result

# 给定的入栈序列
input_sequence = [1, 2, 3, 4, 5]

# 从第一个元素开始
total_ways = backtrack([], input_sequence)
print("总共有 %d 种出栈顺序。" % total_ways)