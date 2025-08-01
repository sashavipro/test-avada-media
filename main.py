from pythagorean import is_pythagorean_triplet

test_cases = [
    ([5, 3, 4], True),
    ([6, 8, 10], True),
    ([100, 3, 65], False)
]

for inputs, expected in test_cases:
    result = is_pythagorean_triplet(inputs)
    print(f"{inputs} -> {result} (фактично: {expected})")
