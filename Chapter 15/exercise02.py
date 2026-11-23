#!/usr/bin/env python3

from date import Date


def main():
    first_date = Date(1933, 6, 22)
    second_date = Date(1933, 9, 17)

    print(first_date)
    print(second_date)

    print(second_date.is_after(first_date))
    print(first_date.is_after(second_date))


if __name__ == "__main__":
    main()
