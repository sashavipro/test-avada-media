from pythagorean import is_pythagorean_triplet
from plants_vs_zombies import plants_win

def run_tests1():
    test_cases = [
        ([5, 3, 4], True),
        ([6, 8, 10], True),
        ([100, 3, 65], False)
    ]

    for inputs, expected in test_cases:
        result = is_pythagorean_triplet(inputs)
        print(f"{inputs} -> {result} (фактично: {expected})")

def run_tests2():
    test_cases = [
        ([2, 4, 6, 8], [1, 3, 5, 7], True),
        ([2, 4], [1, 3, 5, 7], False),
        ([2, 4, 0, 8], [1, 3, 5, 7], True),
        ([1, 2, 1, 1], [2, 1, 1, 1], True),
    ]

    for plants, zombies, expected in test_cases:
        result = plants_win(plants, zombies)
        print(f"zombies={zombies} plants={plants} -> {result} (фактично: {expected})")

if __name__ == "__main__":
    print("Test 1\n")
    run_tests1()
    print("\nTest 2\n")
    run_tests2()
    print("\nTest 3\n")
