def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)


def main():
    print(silnia(5))


if __name__ == '__main__':
    main()
