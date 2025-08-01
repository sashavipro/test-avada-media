from pythagorean import is_pythagorean_triplet
from plants_vs_zombies import plants_win
from datetime import datetime
from schedule_generator import generate_schedule

def run_tests1():
    test_cases = [
        ([5, 3, 4], True),
        ([6, 8, 10], True),
        ([100, 3, 65], False)
    ]

    for inputs, expected in test_cases:
        result = is_pythagorean_triplet(inputs)
        print(f"{inputs} -> {result} (очікується: {expected})")

def run_tests2():
    test_cases = [
        ([2, 4, 6, 8], [1, 3, 5, 7], True),
        ([2, 4], [1, 3, 5, 7], False),
        ([2, 4, 0, 8], [1, 3, 5, 7], True),
        ([1, 2, 1, 1], [2, 1, 1, 1], True),
    ]

    for plants, zombies, expected in test_cases:
        result = plants_win(plants, zombies)
        print(f"zombies={zombies} plants={plants} -> {result} (очікується: {expected})")

def run_tests3():
    days = 5
    work_days = 2
    rest_days = 1
    start_date = datetime(2020, 1, 30)

    expected = [
        datetime(2020, 1, 30, 0, 0),
        datetime(2020, 1, 31, 0, 0),
        datetime(2020, 2, 2, 0, 0),
        datetime(2020, 2, 3, 0, 0)
    ]

    result = generate_schedule(days, work_days, rest_days, start_date)
    print("Генератор розкладу:")
    print(f"days={days}, work_days={work_days}, rest_days={rest_days}, start_date={start_date}")
    print(" -> ")
    for dt in result:
        print(f"  {dt}")
    print(f"(очікується: {[dt for dt in expected]})\n")

if __name__ == "__main__":
    print("Test 1\n")
    run_tests1()
    print("\nTest 2\n")
    run_tests2()
    print("\nTest 3\n")
    run_tests3()