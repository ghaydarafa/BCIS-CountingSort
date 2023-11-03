import tracemalloc
import time
import math
import os

# Based on pseudocode from Adnan Saher Mohammed, S¸ahin Emrah Amrahov, and Fatih V C¸ elebi. Bidirectional Conditional
# Insertion Sort algorithm; An efficient progress on the classical insertion sort. Future Generation Computer Systems, 71:102–112, 2017.
def BCIS(array):
    def ISEQUAL(array, SL, SR):
        """memeriksa apakah semua elemen dalam array
        dari SL ke SR adalah sama. Jika ada elemen yang berbeda,
        maka mereka akan ditukar sehingga semuanya sama.
        Jika semua elemen sama, fungsi akan mengembalikan -1."""
        for k in range(SL + 1, SR):
            if array[k] != array[SL]:
                array[k], array[SL] = array[SL], array[k]
                return k
        return -1

    def InsRight(array, curr_item, SR, right):
        """memasukkan curr_item ke dalam array di sebelah kanan (right)
        dari indeks SR sesuai dengan urutan."""
        j = SR
        while j <= right and curr_item > array[j]:
            array[j - 1] = array[j]
            j += 1
        array[j - 1] = curr_item

    def InsLeft(array, curr_item, SL, left):
        """memasukkan curr_item ke dalam array di sebelah kiri (left)
        dari indeks SL sesuai dengan urutan."""
        j = SL
        while j >= left and curr_item < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = curr_item

    def SWAP(array, i, j):
        """menukar elemen di indeks i dan j."""
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    # SL: indeks awal array, SR: indeks akhir array
    left = 0
    right = len(array) - 1
    SL = left
    SR = right

    while SL < SR:
        # Menukar elemen di indeks SR dan indeks di tengah antara SL dan SR
        # untuk memastikan elemen di SL adalah yang terkecil dan elemen di SR adalah yang terbesar
        SWAP(array, SR, SL + math.ceil((SR - SL) / 2))

        if array[SL] == array[SR]:
            if ISEQUAL(array, SL, SR) == -1:
                return

        if array[SL] > array[SR]:
            SWAP(array, SL, SR)

        if (SR - SL) >= 100:
            for i in range(SL + 1, int((SR - SL) ** 0.5)):
                if array[SR] < array[i]:
                    SWAP(array, SR, i)
                elif array[SL] > array[i]:
                    SWAP(array, SL, i)

        i = SL + 1

        LC = array[SL]
        RC = array[SR]

        while i < SR:
            curr_item = array[i]

            if curr_item >= RC:
                array[i] = array[SR - 1]
                InsRight(array, curr_item, SR, right)
                SR -= 1
            elif curr_item <= LC:
                array[i] = array[SL + 1]
                InsLeft(array, curr_item, SL, left)
                SL += 1
                i += 1
            else:
                i += 1

        SL += 1
        SR -= 1
# end


# Bbased on Counting Sort pseudocode from Slide DAA 07: Sorting in Linear Time
def counting_sort(array, output_array, M):
    n = len(array)
    C = [0] * (M + 1)

    for j in range(n):
        C[array[j]] += 1

    for i in range(1, M + 1):
        C[i] += C[i - 1]

    for j in range(n - 1, -1, -1):
        output_array[C[array[j]] - 1] = array[j]
        C[array[j]] -= 1

def load_dataset_from_text(filename):
    cur_path = os.path.dirname(__file__)
    dataset_path = os.path.join(cur_path, "dataset", filename)

    with open(dataset_path, "r") as file:
        numbers = [int(x) for x in file.readline().split(',')]

    return numbers

def run(dataset):
    dataset_BCIS = dataset.copy()

    # Mulai melacak alokasi memori dan waktu
    tracemalloc.start()
    start_time = time.time()

    # Jalankan algoritma
    BCIS(dataset_BCIS)

    # Hitung penggunaan memori dan waktu
    end_time = time.time()
    memory_stats = tracemalloc.get_traced_memory()[1] / 1000000
    tracemalloc.stop()
    runtime_in_seconds = end_time - start_time
    runtime_in_milliseconds = runtime_in_seconds * 1000

    print(f"Runtime BCIS: {runtime_in_milliseconds:.6f} ms")
    print(f"Memory BCIS: {memory_stats:.6f} MB")

    # Create output array initiate with 0
    output_array = [0] * len(dataset)
    # Finding the maximum element of input_array.
    M = max(dataset)
    
    # Mulai melacak alokasi memori dan waktu
    tracemalloc.start()
    start_time = time.time()

    # Jalankan algoritma
    counting_sort(dataset, output_array, M)

    # Hitung penggunaan memori  dan waktu
    end_time = time.time()
    memory_stats = tracemalloc.get_traced_memory()[1] / 1000000
    tracemalloc.stop()
    runtime_in_seconds = end_time - start_time
    runtime_in_milliseconds = runtime_in_seconds * 1000

    print(f"Runtime Counting Sort: {runtime_in_milliseconds:.6f} ms")
    print(f"Memory Counting Sort: {memory_stats:.6f} MB")
    print()

small_sorted = load_dataset_from_text("small_sorted.txt")
small_random = load_dataset_from_text("small_random.txt")
small_reversed = load_dataset_from_text("small_reversed.txt")

medium_sorted = load_dataset_from_text("medium_sorted.txt")
medium_random = load_dataset_from_text("medium_random.txt")
medium_reversed = load_dataset_from_text("medium_reversed.txt")

large_sorted = load_dataset_from_text("large_sorted.txt")
large_random = load_dataset_from_text("large_random.txt")
large_reversed = load_dataset_from_text("large_reversed.txt")

print("========== Small Sorted ==========")
run(small_sorted)
print("========== Small Random ==========")
run(small_random)
print("========== Small Reversed ==========")
run(small_reversed)

print("========== Medium Sorted ==========")
run(medium_sorted)
print("========== Medium Random ==========")
run(medium_random)
print("========== Medium Reversed ==========")
run(medium_reversed)

print("========== Large Sorted ==========")
run(large_sorted)
print("========== Large Random ==========")
run(large_random)
print("========== Large Reversed ==========")
run(large_reversed)