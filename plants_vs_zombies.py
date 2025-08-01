import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def plants_win(plants: list[int], zombies: list[int]) -> bool:
    try:
        plant_survivors = 0
        zombie_survivors = 0

        # Початкова сила атаки
        plant_power = sum(plants)
        zombie_power = sum(zombies)

        max_len = max(len(plants), len(zombies))

        for i in range(max_len):
            p = plants[i] if i < len(plants) else None
            z = zombies[i] if i < len(zombies) else None

            if p is None:
                zombie_survivors += 1
            elif z is None:
                plant_survivors += 1
            elif p > z:
                plant_survivors += 1
            elif z > p:
                zombie_survivors += 1
            else:
                continue  # обидва гинуть

        logging.info(f"Plants survivors: {plant_survivors}")
        logging.info(f"Zombies survivors: {zombie_survivors}")

        if plant_survivors > zombie_survivors:
            return True
        elif plant_survivors < zombie_survivors:
            return False
        else:
            if plant_power > zombie_power:
                return True
            elif plant_power < zombie_power:
                return False
            else:
                return True

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return False
