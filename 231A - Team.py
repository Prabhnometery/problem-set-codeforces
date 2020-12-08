# Solution to problem 231A - Team
# Link - https://codeforces.com/problemset/problem/231/A



n = int(input())
count = 0


for i in range(0,n):
  num = str(input())
  if num == '1 1 0' or num == '1 0 1' or num == '1 1 1' or num == '0 1 1':
    count = count +  1 
print(count)





