def main():

    print("proper and meets expectation..")
    board = [ ['_']  * 3 for i in range(3)]
    from pprint import pprint
    pprint(board)
    board[1][2] = 'X'
    pprint(board)

    print("List of same object...")
    bad_board = [['_'] *3]  *3
    from pprint import pprint
    pprint(bad_board)
    bad_board[1][2] = 'X'
    pprint(bad_board)

    l = [1, 2, 3]
    print(id(l))
    l *= 2
    print(id(l))

    t = (1, 2, 3)
    print(id(t))
    t *= 2
    print(id(t))


if __name__=="__main__":
    main()

