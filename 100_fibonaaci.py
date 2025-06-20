def fib(n):
    if n <=1:
        return n
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

print(fib(5))

def fib_arr(n):
    if n<=1:
        return n
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp

print(fib_arr(5))