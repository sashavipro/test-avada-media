import logging

logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def is_pythagorean_triplet(numbers):
    try:
        if len(numbers) != 3:
            raise ValueError("Має бути рівно 3 числа.")

        a, b, c = sorted(numbers)
        result = a**2 + b**2 == c**2
        logging.info(f"Перевірка для {numbers} -> {result}")
        return result

    except Exception as e:
        logging.error(f"Помилка для {numbers}: {str(e)}")
        return False
