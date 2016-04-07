# python3

import sys

def Match(a, b):
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    if a == '(' and b == ')':
        return True
    return False


if __name__ == "__main__":
    text = sys.stdin.read()
    opening_brackets_stack = []
    Error=0
    if len(text.strip())==1 and text.strip() in ['(','{','[',']','}',')']:
        print ('1')
    else:
        for i, next in enumerate(text.strip()):
           
            if next == '(' or next == '[' or next == '{':
                opening_brackets_stack.append((i,next))
                
            if next == ')' or next == ']' or next == '}':
                if len(opening_brackets_stack) == 0 or not Match(opening_brackets_stack.pop()[1],next):
                    Error =(i+1)
                    print (Error) 
                    break
    
        if len(opening_brackets_stack) == 0 and Error==0:
            print('Success')
        elif len(opening_brackets_stack) != 0 and Error==0:
            print(opening_brackets_stack.pop()[0]+1)


