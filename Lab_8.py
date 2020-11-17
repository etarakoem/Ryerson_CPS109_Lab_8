'''
Question 1 (5 points)
Saved
A run is a sequence of adjacent repeatedvalues.
Write a program that generates a sequence of 20 random die
tosses and then prints the die values, marking the runs by including
them in parentheses, like this:
1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1

'''
import random
def Q1():
    dice_list = [random.randint(1,6) for i in range(20)]
    dice_list.append('None')
    print(dice_list)
    iRun = False
    for i in range(len(dice_list)-1):
        if i == 0 or i == len(dice_list):
            print(dice_list[i], end=' ')
        else:
            if iRun:
                if dice_list[i] != dice_list[i - 1]:
                    print(')', end=' ')
                    # result =result+ ')'
                    iRun = False
            else:
                if dice_list[i] == dice_list[i + 1]:
                    print('(', end=' ')
                    # result = result+ '('
                    iRun = True
        print(dice_list[i], end=' ')
    if iRun:
        print(')', end=' ')
    return
# Q1()
'''
Write a program that generates a sequence of 20 random die tosses and that prints the die values, 
marking only the longest run, like this:

1 2 5 5 3 3 2 4 3 (2 2 2 2) 3 6 5 5 6 3 1

'''
def replace_index(indexing,string,new_string):
    return string[:indexing]+new_string+string[indexing:]
def q2():
    dice_list = [random.randint(1, 6) for i in range(20)]
    dice_list.append('None')
    potential = []
    final_result = ' '
    result = ''
    iRun = False
    for i in range(0,len(dice_list) - 1):
        if iRun:
            if dice_list[i] != dice_list[i - 1]:
                result += ') '
                potential.append(i)
                iRun = False
        else:
            if dice_list[i] == dice_list[i + 1]:
                result += '( '
                potential.append(i)
                iRun = True
        result += str(dice_list[i])+' '
    if iRun:
        result += ') '
        potential.append(i)
    if result.count('(') == 0:
        print('No longest combo')
        return
    difference = [(potential[i+1]-potential[i])  for i in range(len(potential)) if i%2 == 0]
    max_position = difference.index(max(difference))
    potential_result = (potential[max_position*2],potential[max_position*2+1])
    for i in range(len(dice_list)-1):
        if i == potential_result[0]:
            final_result+= '( '+ str(dice_list[i]) + ' '
        elif i == potential_result[1]:
            final_result += ') ' + str(dice_list[i]) + ' '
        else:
            final_result += str(dice_list[i]) + ' '
    print(final_result)
    return
# q2()
def q3():
    dice_list = [random.randint(0,1) for i in range(20)]
    dice_list.append('None')
    for i in range(len(dice_list)):
        if dice_list[i] == 1:
            dice_list[i] = 'True'
        else:
            dice_list[i] = 'False'
    # print(dice_list)
    potential = []
    final_result = ''
    result = ''
    iRun = False
    for i in range(0,len(dice_list) - 1):
        final_result += dice_list[i]+' '
        if iRun:
            if dice_list[i] != dice_list[i - 1]:
                result += ') '
                potential.append(i)
                iRun = False
        else:
            if dice_list[i] == dice_list[i + 1]:
                result += '( '
                potential.append(i)
                iRun = True
        result += str(dice_list[i])+' '
    if iRun:
        result += ') '
        potential.append(i)
    if result.count('(') == 0:
        print('No longest combo')
        return
    # print(result)
    # print('potential:',potential)
    difference = [(potential[i+1]-potential[i])  for i in range(len(potential)) if i%2 == 0]
    # print('difference:',difference)
    max_position = difference.index(max(difference))
    # print('max_position:',max_position)
    potential_result = (potential[max_position*2],potential[max_position*2+1])
    # print('potential_result: ',potential_result)
    print(final_result)
    print(potential_result)
    return
# q3()
def find(string):
    # print('Start:')
    string += '0'
    # print(string)
    result =[]
    iRun = False
    for i in range(len(string)-1):
        if iRun:
            if (string[i] != string[i+1]) and (string[i]=='-'):
                iRun = False
                result.append(i)
        else:
            if (string[i]==string[i+1])and(string[i]=='-'):
                iRun = True
                result.append(i)
    # print('result:',result)
    potential = [result[i+1]-result[i]  for i in range(len(result)) if i%2 == 0]
    # print('potential:',potential)
    if potential != []:
        pos = potential.index(max(potential))
        return result[pos*2],result[pos*2+1]
    else:
        for i in range(len(string)-1):
            if string[i]=='-':
                return i,i
def print_in(string):
    midpoint = len(string) // 2
    return string[:midpoint] + 'X' + string[midpoint + 1:]
def occupy(n):
    result = '-'*n
    print(result)
    result_after= print_in(result)
    print(result_after)
    while result_after.count('-')>0:
        start,end = find(result_after)
        if start != end:
            result_after = result_after[:start]+print_in(result_after[start:end])+result_after[end:]
        else:
            result_after = result_after[:start]+'X'+result_after[start+1:]
        print(result_after)
    return result_after
occupy(10)