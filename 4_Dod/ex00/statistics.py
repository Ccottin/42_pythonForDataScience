
# * = unpacking operator returning a tuple(unmutable list) that works for
# positionals args
# ** = same but returns a dict for named args


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Will return median, mean, quartile, standard deviation or variance
    according to numbers and keywords given"""

    try:
        assert len(args) is not None and len(kwargs) is not None
        i = 0
        total = 0
        for arg in args:
            i = i + 1
            total = total + arg
        sorted_args = list(args)
        sorted_args.sort()

        for key, value in kwargs.items():
            if i == 0:
                print("ERROR")
            elif value == "mean":
                print("mean :", total / i)
            # usually you need +1 before div to find median but we count from 0
            elif value == "median":
                print("median :", sorted_args[int((i) / 2)])
            elif value == "quartile":
                quartile = sorted_args[int((i) / 4)]

                #formatting is wrong here
                quartile3 = sorted_args[int((i) / 6)]
                print("quartile :", [float(f'{quartile:.1}'),
                                     float(f'{quartile3:.1}')])
            elif value == "std":
                mean = total / i
                temp = 0
                for arg in args:
                    temp = temp + ((arg - mean) ** 2)
                #same shit here, you need to substract 1 to i but we count from 0
                print("std:", (temp / i) ** 0.5)
            elif value == "var":
                mean = total / i
                temp = 0
                for arg in args:
                    temp = temp + ((arg - mean) ** 2)
                print("var:", temp / i)

    except Exception as e:
        print("Error:", str(e))
        return (None)
