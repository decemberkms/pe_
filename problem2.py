'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
'''
def fibo(n):
    a = 1
    b = 2
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fibo(10):
    print(i)

def fibon(n):
    a = 1
    b = 2
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b

    return output

print(fibon(10))
'''
a = 1
b = 2
list_fibo = []
while a <= 4000000:
    print(a)
    list_fibo.append(a)
    a,b = b, a + b
    print(list_fibo)

sum_fibo = 0
for i in list_fibo:
    if i % 2 == 0:
        sum_fibo += i
print("Answer: ",sum_fibo)

'''
## simple
a,b=1,1
total_b=0
while b<=4000000:
    a,b=b,a+b
    if b%2==0:
        total_b+=b
print(total_b)
'''
