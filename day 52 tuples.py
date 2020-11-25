if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

#for i in range(n):
    #input_list = map(int, integer_list)

t = tuple(integer_list)
print (hash(t))
