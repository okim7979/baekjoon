while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except ValueError:
        break
    except EOFError:
        break