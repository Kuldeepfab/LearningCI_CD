# Writing basic functions
 
def add(x,y):
    'Adding Two Values'
    return(x + y)

def sub(x,y):
    return(x - y)

def iseven(x):
    if x%2==0:
        return(True)
    else:
        return(False)

def multiply(x,y):
    return(x * y)

def divide(x,y):
    if y==0:
        raise ValueError('cant divide by Zero')
    return(x/y)