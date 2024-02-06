if __name__ == '__main__':
    N = int(input())
    List = []

    for _ in range(N):
        operation = input().split()
        command = operation[0]
        
        if command == 'insert':
            index, element = int(operation[1]), int(operation[2])
            List.insert(index, element)
        elif command == 'print':
            print(List)
        elif command == 'remove':
            element = int(operation[1])
            List.remove(element)
        elif command == 'append':
            element = int(operation[1])
            List.append(element)
        elif command == 'sort':
            List.sort()
        elif command == 'pop':
            List.pop()
        elif command == 'reverse':
            List.reverse()