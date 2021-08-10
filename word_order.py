n = int(input())
dic  = {}

for _ in range(n):
  w = input()
  if w in dic.keys():
    dic[w]+=1
  else:
    dic.update({w:1})

print(len(dic.keys()))
print(*dic.values())
