from multiprocessing import Process, Queue
import time
from random import randint


class RandNumGeneratorError(Exception):
    def __init__(self, message):
        self.message = message

        super().__init__(self.message)


def f_square(number, result):
    result.put(number ** 2)


def generate_random_numbers(quantity, minimum, maximum):
    if quantity > 0 and minimum < maximum and minimum.is_integer() and maximum.is_integer():
        return [randint(minimum, maximum) for _ in range(quantity)]
    else:
        raise RandNumGeneratorError("Переменный для функции generate_random_numbers() не удовлетворяют одному из "
                                    "условий.")


def get_squares(numbers):
    result = Queue()

    processes = []
    for number in numbers:
        if number.is_integer():
            process = Process(target=f_square, args=(number, result))
            processes.append(process)
            process.start()
        else:
            raise Exception("В списке находятся не численные элементы.")

    # завершение всех процессов
    for process in processes:
        process.join()

    # результаты вычислений из каждого процесса
    squared_numbers = []
    while not result.empty():
        squared_numbers.append(result.get())

    return sorted(squared_numbers)


if __name__ == "__main__":
    numbers = generate_random_numbers(10, 1, 100)
    start_time = time.time()
    squared_numbers = get_squares(numbers)
    end_time = time.time()
    print(squared_numbers)
    execution_time = end_time - start_time
    print("Время выполнения функции:", execution_time, "секунд")
