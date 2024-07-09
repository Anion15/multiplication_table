c = 0   # c는 b 보조
d = 0   # d는 a 보조
e = 0   # e는 결과 값
f = 0   # f는 결과 보조
g = 0   # g는 출력 값 보조
h = 0   # h는 출력 값 while 보조
몇개 = int(input("구구단을 몇단까지 출력할까요? : "))
얼마 = int(input("출력하는 구구단을 몇 까지 곱할까요? : "))
my_list = []


def multiplication(a, b):  #a는 몇단인지, b는 어디까지 return(print) 할 것인지.
  c = 1
  d = 1
  e = 0
  f = 0
  my_list.clear()
  my_list.append(" ")
  my_list.append(" ")
  my_list.append("----------구구단 " + str(a) + "단----------")
  my_list.append(" ")
  while c < b + 1:
    e = a * c
    f = str(a) + " x " + str(c) + " = " + str(e)
    my_list.append(f)
    c = c + 1

while 몇개 > h:
  multiplication(h + 1, 얼마)
  g = 0
  while g < len(my_list):
    print(my_list[g])
    g = g + 1
  h = h + 1
while True:
   pass