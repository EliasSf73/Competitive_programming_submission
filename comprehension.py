if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print (ans)
    # for i in range(0, x + 1):
    #     for j in range(0, y + 1):
    #         for k in range(0, z + 1):
    #             if (x + y + z != n):
    #                 w=([i, j, k])
    #                 print(w)
                    