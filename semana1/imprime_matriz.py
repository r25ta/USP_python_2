def imprime_matriz(mtz):
    l = 0
    for lin in mtz:
        c = 0
        ret = ""
        for col in range(len(lin)):
            ret = str(mtz[l][c])
            if c + 1 < len(lin):
                print(ret,end=" ")
            else:
                print(ret)
            c += 1
        l += 1
"""
def main():
    mtz = [[1, 2, 7], [3, 4, 8], [1, 2, 3]]
    imprime_matriz(mtz)

main()
"""