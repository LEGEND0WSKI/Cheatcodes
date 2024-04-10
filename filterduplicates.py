# maintain order and remove duplicates
old = ['jake','benson','carter','jake','ark','carter','dale','jake','jake']

# Sets dont maintain order
# s1=set(old)
# print(s1)

# slower way
new = []
for i in old:
    if i not in new:
        new.append(i)
print(new)

# faster way
new = list(dict.fromkeys(old,0))
print(new)
