from operator import truediv


def test_number(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True
    else:
        return False
#user inout
x=int(input("enter the number"))
y=int(input("enter the number"))
print(test_number(x,y))
#direct value 
print(test_number(2,2))
print(test_number(3,2))
print(test_number(7,3))
print(test_number(27,53))