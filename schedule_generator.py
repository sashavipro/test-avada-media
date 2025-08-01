import logging
from datetime import datetime, timedelta
from typing import List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> List[datetime]:
    try:
        if days <= 0 or work_days <= 0 or rest_days < 0:
            raise ValueError("Неправильні вхідні параметри")

        schedule = []
        current_date = start_date
        generated_days = 0

        while generated_days < days:
            for _ in range(work_days):
                if generated_days >= days:
                    break
                schedule.append(current_date)
                current_date += timedelta(days=1)
                generated_days += 1
            current_date += timedelta(days=rest_days)

        logging.info(f"Розклад згенеровано на {len(schedule)} днів")
        return schedule

    except Exception as e:
        logging.error(f"Помилка при генерації розкладу: {e}")
        return []
