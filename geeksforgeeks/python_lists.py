if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        co = input().split()
        if co[0] == "insert":
            li.insert(int(co[1]), int(co[2]))
        elif co[0] == "print":
            print(li)
        elif co[0] == "remove":
            li.remove(int(co[1]))
        elif co[0] == "append":
            li.append(int(co[1]))
        elif co[0] == "sort":
            li.sort()
        elif co[0] == "pop":
            li.pop()
        elif co[0] == "reverse":
            li.sort(reverse=True)
