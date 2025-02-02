import random
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import List

def deterministic_quick_sort(arr: List[int]) -> List[int]:
    """
    Реалізація детермінованого QuickSort з вибором останнього елемента як опорного
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # Вибираємо останній елемент як опорний
    left = []
    right = []
    
    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

def randomized_quick_sort(arr: List[int]) -> List[int]:
    """
    Реалізація рандомізованого QuickSort з випадковим вибором опорного елемента
    """
    if len(arr) <= 1:
        return arr
    
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    left = []
    right = []
    
    for i in range(len(arr)):
        if i != pivot_idx:
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
    
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

def measure_sorting_time(sort_func, arr: List[int], iterations: int = 5) -> float:
    """
    Вимірювання середнього часу виконання сортування
    """
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

def plot_results(sizes: List[int], rand_times: List[float], det_times: List[float]):
    """
    Побудова графіку порівняння часу виконання
    """
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, 'b-o', label='Рандомізований QuickSort')
    plt.plot(sizes, det_times, 'r-o', label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння ефективності алгоритмів QuickSort')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Розміри масивів для тестування
    sizes = [10_000, 50_000, 100_000, 500_000]
    rand_times = []
    det_times = []
    
    for size in sizes:
        # Генерація випадкового масиву
        arr = [random.randint(1, 1000000) for _ in range(size)]
        
        # Вимірювання часу для обох алгоритмів
        rand_time = measure_sorting_time(randomized_quick_sort, arr)
        det_time = measure_sorting_time(deterministic_quick_sort, arr)
        
        rand_times.append(rand_time)
        det_times.append(det_time)
        
        print(f"\nРозмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")
    
    # Побудова графіку
    plot_results(sizes, rand_times, det_times)

if __name__ == "__main__":
    main()
