# 주기문

# 문자열 s 를 입력 받는다.
s = input()

# p 배열 초기
p = [0 for _ in range(len(s))]


# prefix = surfix 인 개수 저
def pi_make (list):
    global p

    j = 0

    for i in range(1, len(list)):
        while j > 0 and list[i] != list[j]:
            j = p[j-1]

        if list[i] == list[j]:
            j = j + 1
            p[i] = j

    return p

pi = pi_make(s)
#print(p)

for i in range(len(s)):
    if pi[i] != 0 and (i+1)%(i+1-pi[i]) == 0:
        first = i + 1
        second = int((i+1) / (i+1-pi[i]))
        print(str(first) + " " + str(second))



