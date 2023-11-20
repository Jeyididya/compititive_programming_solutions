import textwrap
from math import ceil


def wrap(string, max_width):

    ll = len(string)
    if ll <= max_width:
        # print(string)
        return string

    n = ceil(ll/max_width)
    i = 0
    ans = ""
    for j in range(n):
        # print(string[i:i+max_width])
        ans += string[i:i+max_width]+"\n"
        i = i+max_width

    return ans


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
