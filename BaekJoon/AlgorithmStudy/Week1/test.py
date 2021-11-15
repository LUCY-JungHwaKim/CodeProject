# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

# print("|\_/|")
# print("|q p|   /}")
# print("( 0 )"'"""\\')
# print("|"+'"^"`    |')
# print("||_/=\\\\__|")

# a,b = map(int, input().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

#Problem Num 2588

# a = int(input())
# b = int(input())

# first_num = b%10
# third_num = int(b/100)
# second_num = int((b-(third_num*100))/10)

# # print(first_num)    #일의자리
# # print(second_num)   #10의자리
# # print(third_num)    #100의자리

# print(a*first_num)
# print(a*second_num)
# print(a*third_num)
# print(a*b)

# a = int(input())

# if a >= 90 and a <=100:
#     print("A")
# elif a >= 80 and a <=89:
#     print("B")
# elif a >= 70 and a <=79:
#     print("C")
# elif a >= 60 and a <=69:
#     print("D")
# else:
#     print("F")

# a = int(input())

# if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
#     print(1)
# else:
#     print(0)

# a = int(input())
# b = int(input())

# if a>0 and b>0:
#     print(1)
# elif a<0 and b>0:
#     print(2)
# elif a<0 and b<0:
#     print(3)
# else:
#     print(4)

# a,b = map(int, input().split())

# if (a >= 0 and a<=23) and (b>=0 and b<=59):

#     if b>=45:
#         print(a,b-45)
#     elif b<45 and a>0:
#         print(a-1, (60+b)-45)
#     else:
#         print(23, (60+b)-45)

# a = int(input())

# for i in range(9):
#     print(str(a) + " * " + str(i+1) + " = " + str(a*(i+1)))

# a = int(input())
# sum_ary = []
# for i in range(a):
#     b,c = map(int, input().split())
#     sum_ary.append(b+c)

# for i in range(a):
#     print(sum_ary[i])

# a = int(input())
# sum_num = 0

# for i in range(a):
#     sum_num += (i+1)

# print(sum_num)

# import sys
# a = int(input())
# sum_ary = []
# for i in range(a):
#     a,b = map(int,sys.stdin.readline().split()) #여기 빠른 입력 기억
#     sum_ary.append(a+b)

# for i in range(len(sum_ary)):
#     print(sum_ary[i])
# import sys
# a = int(input())

# sum_ary = []
# first_num = []
# second_num = []
# for i in range(a):
#     a,b = map(int,sys.stdin.readline().split()) #여기 빠른 입력 기억
#     if a > 0 and b<10:
#         first_num.append(a)
#         second_num.append(b)
#         sum_ary.append(a+b)

# for i in range(len(sum_ary)):
#     print("Case #" + str(i+1) + ": " + str(first_num[i]) + " + " + str(second_num[i]) + " = " + str(sum_ary[i]))


# a = int(input())
# for i in range(a-1, -1, -1):
#     print(" "*i, end='')
#     print("*"*(a-i))

a,b = map(int, input().split())

num_ary = list(map(int, input().split()))

for i in range(a):
    if num_ary[i] < b:
        print(num_ary[i], end=" ")