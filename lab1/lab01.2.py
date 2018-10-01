def function (a,b):
    if a < 0 or b <=0:
        raise Exception('try again')
    list =[]
    if b < a :
        for num in range(b, a + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        print(list)
    else:
        for num in range(a, b + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        print(list)
    if not list:
        print('NoSimpleDigits')

function(a = int(input('Enter first number: ')),b = int(input('Enter second number: ')))