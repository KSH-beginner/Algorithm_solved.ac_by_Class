while True:
    stack = []
    sentence = input()
    
    if sentence == ".":
        break
    
    for i in range(len(sentence)):
        if sentence[i] == "(":
            stack.append("(")
        
        if sentence[i] == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append("X")
                break
            
        if sentence[i] == "[":
            stack.append("[")
        
        if sentence[i] == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("X")
                break
        
    if len(stack) == 0:
        print("yes")
    else:
        print("no") 