from give_bmi import give_bmi, apply_limit


def moartest(height, weight, limit):
    bmi = give_bmi(height, weight)
    print("bmi :", bmi, ",limits :", limit, "\nresult :",
          apply_limit(bmi, limit), "\n")


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26), "\n")

    print('moartest(None, None, None)')
    moartest(None, None, None)
    print('moartest([12], [12], None)')
    moartest([12], [12], None)
    print('moartest(None, [12], 12)')
    moartest(None, [12], 12)
    print(' moartest(None, [12], 12)')
    moartest(None, [12], 12)

    print('(78, 78, 78)')
    moartest(78, 78, 78)
    print('([78], [78], [78])')
    moartest([78], [78], [78])
    print('([-78], [78], [78])')
    moartest([-78], [78], 78)
    print('([78], [-78], 78)')
    moartest([78], [-78], 78)
    print('([78], [78], -78)')
    moartest([78], [78], -78)
    print('(coucou, [78], 78)')
    moartest(["coucou"], [78], 78)
    print('([78], [78], coucou)')
    moartest([78], [78], "coucou")

    height = [2.71, 1.15, 1.0, 1, 2, 1.87561235, 987]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    limit = 30
    print('''
    height = [2.71, 1.15, 1.0, 1, 2, 1.87561235, 987]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    limit = 30''')
    moartest(height, weight, limit)

    height = [2.71, 1.15, 1.0, 1, 2, 1.87561235, 79456]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    limit = 50
    print('''
    height = [2.71, 1.15, 1.0, 1, 2, 1.87561235, 79456]
    weight = [165.3, 38.4, 40, 64, 98, 654, 489156864]
    limit = 50''')
    moartest(height, weight, limit)

    height = [2.71, 1.15, 1.0]
    weight = [165.3, 38.4]
    limit = 50
    print('''
    height = [2.71, 1.15, 1.0]
    weight = [165.3, 38.4]
    limit = 50''')
    moartest(height, weight, limit)


if __name__ == "__main__":
    main()
