# a nested nested function needs to climb up step by step
# also this could be practical to protect executions

def callLimit(limit: int):
    """This is a wrapper that allows only a certain number of execution"""
    try:
        count = 0

        def callLimiter(function):
            def limit_function(*args: any, **kwds: any):

                nonlocal count
                nonlocal limit
                nonlocal function

                assert limit > -1
                if count < limit:
                    function()
                    count = count + 1
                else:
                    print("Error:", function, "call too many times")
                return (0)
            return (limit_function)
        return (callLimiter)

    except Exception as e:
        print("Error:", e.str())
