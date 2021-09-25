class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s += '$'
        pre_flag = '+'
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)#因为传入的是字符串，所以当数字大于一位时，需要循环输入并*10得到实际的数
            elif c == ' ': continue #题干里有空格的情况，直接继续循环
            else:
                if pre_flag == '+':
                    stack.append(num)#因为加法可以直接用sum来计算，所以当数字前面为+时可以直接入栈
                elif pre_flag == '-':
                    stack.append(-num)#若为-，则将数字变为负数后入栈
                elif pre_flag == '*':
                    stack.append(stack.pop() * num)#当为*时弹出栈顶元素并计算
                elif pre_flag == '/':
                    stack.append(int(stack.pop() / num))#同*法
                pre_flag = c
                num = 0
        return sum(stack)

yy = Solution()
yy.calculate('100+26-300*4/5+6')