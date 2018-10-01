def function(a, b):
    if a < 0 or b <= 0:
        raise Exception('Try again')
    temp = False
    if a % b == 0:
        temp = True
        return temp

print(function( a =int(input('Enter first number: ')), b =int(input('Enter second number: '))))