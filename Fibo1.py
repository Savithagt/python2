def fib(num):
    if num<=0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
num=int(input("Enter a Number:"))
print("Fibonacci of given number",num,"is:",fib(num))
