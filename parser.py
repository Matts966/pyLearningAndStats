# coding: utf-8
# Here your code !
S = input()
num = [str(i) for i in range(10)]
alph = [chr(i) for i in range(97, 97+26)]

def wordCounter(String):
    result = [0 for i in range(26)]
    point = 0
    while point < len(String):
        if String[point] in alph:
            result[alph.index(String[point])] += 1
        elif String[point] in num:
            count = point + 1
            while String[count] in num:
                count += 1
            if String[count] == '(':
                stack = [0]
                count += 1
                cnt = count + 1
                while True:
                    if String[cnt] == '(':
                        stack.append(0)
                    elif String[cnt] == ')':
                        stack.pop()
                    if len(stack) == 0:
                        break
                    else:
                        cnt += 1
                numm = int(String[point:count-1])
                ret = list(map(lambda x: x*numm,wordCounter(String[count:cnt])))
                for i in range(26):
                    result[i] += ret[i]
                point = cnt
            else: 
                result[alph.index(String[count])] += int(String[point:count])
                point = count 
        point += 1
                
    return result

result = wordCounter(S)      
for i in range(26):
    print(alph[i], result[i])
    
