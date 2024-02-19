from give_bmi import give_bmi, apply_limit


def moartest(height, weight, limit):
    bmi = give_bmi(height, weight)
    print(apply_limit(bmi, 26))


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    print('moartest(None, None, None)')
    moartest(None, None, None)
    print('moartest([12], None, None)')
    moartest([12], None, None)
    print('moartest(None, [12], None)')
    moartest(None, [12], None)
    print(' moartest(None, None, 12)')
    moartest(None, None, 12)

    print('(78, 78, 78)')
    moartest(78, 78, 78)
    print('([78], [78], [78])')
    moartest([78], [78], [78])
    print('(-[78], [78], [78])')
    moartest([-78], [78], [78])
    print('([78], -[78], [78])')
    moartest([78], [-78], [78])
    print('([78], [78], -[78])')
    moartest([78], [78], [-78])
    print('(coucou, 78, 78)')
    moartest(["coucou"], [78], 78)

    height = [2.71, 1.15, 1.0, 1, 2, 1.87561235, 987]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    limit = 30
    print(''' height = [2.71, 1.15, 1.0, 1, 2, 1.87561235, 987]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    limit = 30''')
    moartest(height, weight, limit)

    height = [2.71, 1.15, 1.0, 1, 2, 1.87561235]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    print(''' height = [2.71, 1.15, 1.0, 1, 2, 1.87561235]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
''')
    moartest(height, weight, limit)


if __name__ == "__main__":
    main()
