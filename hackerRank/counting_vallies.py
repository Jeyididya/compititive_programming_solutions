def countingValleys(steps, path):
    # Write your code here
    val=0
    up=0
    down=0
    for i in range(steps):
        if path[i]=="U":
            up+=1
        elif path[i]=="D":
            up-=1
        if up==0 and path[i]=="U":
            val+=1
    return val