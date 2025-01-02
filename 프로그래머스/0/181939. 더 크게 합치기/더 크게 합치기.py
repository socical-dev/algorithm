def solution(a, b):
    # a ⊕ b 와 b ⊕ a 중에 더 큰 값을 리턴
    # 만약 둘이 같으면 a ⊕ b 값으로 리턴
    
    # a, b 각 값은 정수이기에 + 를 하면 더해기에 처음에는 String 형식으로 넣어놓고, %d(정수)로 포멧팅 후 int로 형변환을 한다.
    aNum = int("%d%d" %(a,b))
    bNum = int("%d%d" %(b,a))
    
    if aNum < bNum:
        answer = bNum
    else:
        answer = aNum
    return answer