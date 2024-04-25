from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2), "\n")
print(slice_me(family, 1, -2), "\n")
print(slice_me(family, 'hello', 'itsme'))
print(slice_me(family, 0, 0), "\n")
print(slice_me(family, None, None), "\n")


family = []

print(slice_me(family, 0, 2), "\n")
print(slice_me(family, 1, -2), "\n")

family = [[1.80, 78.4, 3],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 0), "\n")
print(slice_me(family, 1, -2), "\n")

family = 4
print(slice_me(family, 1, -2), "\n")
