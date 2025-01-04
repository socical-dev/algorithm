angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1+angle2)-360*int((angle1 + angle2) / 360)    # angle1+a00ngle2한 값에 360 로 나눠진 값의 * 360을 곱해서 그만큼 빼면 360도 미만으로 값이 나올거라 추측
print(sum_angle)