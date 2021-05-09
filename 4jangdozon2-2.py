input = int(input('구입 음악 개수:'))
price = 400
total = input * price
halin = total * 0.3
print('총 가격:', total, "원")
print('할인금액:', halin, "원")
print("총 구입 가격:", total - halin, "원")