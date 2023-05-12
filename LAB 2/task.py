import math
import time
import matplotlib.pyplot as plt 
import numpy as np

def lcg(x0,a,c,m,n):
    x = [x0]
    for i in range(n):
        x.append((a*x[i]+c) % m)
    return x    
def period(result, num):
    flg = 0;
    cnt = 0;
    for i in range(len(result)):  
        if(result[i]==num):
            flg+=1
        if(flg == 2):
            break
        elif(flg==1):
            cnt+=1

    return cnt  
 
def GetSubsequence(nums):
  res = []
  for num in nums:
    if (num > 1000):
      res.append(num%1000)
    elif(num > 100):
      res.append(num%100)
    else:
       res.append(num%10)
  return res

def boksMull(n):
    np.random.seed(4832)
    X = np.random.uniform(-1,1,size = n)
    Y = np.random.uniform(-1,1,size = n)

    plt.hist(X)
    plt.show()

    plt.hist(Y)  
    plt.show()

    S = np.power(X,2) + np.power(Y, 2)
    for i in range(len(S)):
        if(S[i]>1 or S[i]==0):
           S = np.power(X,2) + np.power(Y, 2)
    Z1 = X * np.sqrt(-2 * np.log(S)/S)
    Z2 = Y * np.sqrt(-2 * np.log(S)/S)

    plt.hist(Z1,bins =100)
    plt.show()
    
    plt.hist(Z2,bins =100)    
    plt.show()
    
def Gauss(x): # для нормального распределения среднеквадратическое отлонение равно 1, а  мат ожидание 0
    return (1/math.sqrt(2*math.pi)*math.exp((-1/2)*(x**2)))


A = 69069
X0 = 50
C = 5
M = 2**10

print('linear cong method')
res = lcg(X0,A,C,M,10000)
print(res)

print('enter number to search')
n = input()
print("generator period:",period(res,21))

fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(res)
 
# Show plot
plt.show()

subsec = GetSubsequence(res)

print('least digit')
print(subsec)

print('enter number to search')
n = input()
print("generator period:",period(subsec,2))

fig, axs = plt.subplots(figsize =(10, 7))
axs.hist(subsec)

plt.show()

boksMull(10000)

print("gaussian func at x = 1:", Gauss(0))
print("gaussian func at x = 1:", Gauss(1))
print("gaussian func at x = 3:", Gauss(3))