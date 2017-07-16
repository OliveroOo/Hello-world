import re

#Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


#postfix
def eval_postfix(expr):
    token_list = re.split("([^0-9])",expr)
    stack = Stack()
    for token in token_list:
        if token == '' or token == ' ':
            continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == '/':
            product = stack.pop() / stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

#postfix
def eval_2postfix(expr):
    pass

#Infix
def eval_infix(expr):
    token_list = re.split('([^0-9 ])',expr)
    stack = Stack()
    i = 0
    for tok in token_list:
        token = tok.strip()
        if token.isdigit():
            stack.push(int(token))
            i += 1

            if i == 2:
                if token_last == '+':
                    sum = stack.pop() + stack.pop()
                    stack.push(sum)
                    i = 1
                if token_last == '*':
                    product = stack.pop() * stack.pop()
                    stack.push(product)
                    i = 1
                if token_last == '/':
                    production = stack.pop() + stack.pop()
                    stack.push(production)
                    i = 1

        else:
            token_last = token
    return stack.pop()

if __name__ == '__main__':
    print(eval_postfix('55 56 + 2 *'))
    print(eval_postfix('123 555 + 2 /'))
    print(eval_postfix('1 2 + 3 *'))
    print(eval_infix('1 + 2 * 3 + 55'))
