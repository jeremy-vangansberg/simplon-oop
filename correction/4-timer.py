import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Obtient le temps de début
        result = func(*args, **kwargs)  # Appelle la fonction originale
        end_time = time.time()  # Obtient le temps de fin
        duration = end_time - start_time  # Calcule la durée
        print(f"{func.__name__} a pris {duration:.4f} secondes pour s'exécuter.")
        return result
    return wrapper


@timer_decorator
def ma_fonction():
    time.sleep(2)  # Simule une fonction qui prend du temps à s'exécuter
    print("Fonction terminée!")


ma_fonction()
