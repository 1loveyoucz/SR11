text = input().split(': ')
text_l = []
n = int(input())

for i in text:
    if len(i) > n and len(i) % n != 0:
        text_l.append(i)

print(', '.join([j.capitalize() for j in text_l]))

