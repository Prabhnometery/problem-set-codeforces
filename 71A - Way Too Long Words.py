# Solution to problem 71A - Way Too Long Words
# Link - https://codeforces.com/problemset/problem/71/A


n = int(input())

for i in range(0, n):
  text = str(input())
  length = len(text)
  if length > 10:
    print(text[0] + str(length - 2) + text[-1])
  else:
    print(text)



