# -*- coding: utf-8 -*-

def calculation(a, b):
    print((a+b,a-b))



def triangle_lambda():
    return ('lambda_triangle_area:  lambda b,h : b*h/2')



def sort_words(hyphen_str):
    w=hyphen_str.split("-")
    w.sort()
    print('-'.join(w))



def perfect_number():
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    print(sum(divisor)==2*num)


if __name__ == '__main__':
    pass