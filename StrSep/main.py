WIN_SEP = "\\"
WIN_SEP_TWI = "\\\\"
UNIX_SEP = "/"


def str_convert():
    print("input the source string:")
    source = input()
    print("input the mode.[0:win to unix;1:unix to win")
    mode_inp = input()
    if mode_inp == "":
        mode = 0
    else:
        mode = int(mode_inp)
    if mode == 0:
        source = UNIX_SEP + source.replace(WIN_SEP_TWI, UNIX_SEP).replace(WIN_SEP, UNIX_SEP)
    else:
        if source.startswith(UNIX_SEP):
            source = source.lstrip(UNIX_SEP)
        source = source.replace(UNIX_SEP, WIN_SEP)
    return source


if __name__ == '__main__':
    print(str_convert())
