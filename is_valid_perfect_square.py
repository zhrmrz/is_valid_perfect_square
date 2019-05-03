from math import *
class Sol:
    def is_valid_perfect_square(self,num):
        left=0
        right=num
        for i in range(int(log2(num)+2)):
            n=int((right+left)/2)
            if n*n==num:
                return True
            elif n*n>num:
                right=n
            else:
                left=n
        return False

if __name__ == '__main__':
    p1=Sol()
    print(p1.is_valid_perfect_square(728))
