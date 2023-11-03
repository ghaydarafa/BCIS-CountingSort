import random

def generate_dataset(size, status):
    numbers = list(range(1, size))

    if status == "sorted":
        numbers.sort()
    elif status == "random":
        random.shuffle(numbers)
    elif status == "reversed":
        numbers.sort()
        numbers.reverse()

    return numbers

def save_dataset_to_text(dataset_combinations):
    for size, status in dataset_combinations:
        if size == 500:
            size_label = "small"
        elif size == 5000:
            size_label = "medium"
        elif size == 50000:
            size_label = "large"

        filename = f"{size_label}_{status}.txt"
        dataset = generate_dataset(size, status)
        with open(filename, 'w') as textfile:
            textfile.write(', '.join(map(str, dataset)) + '\n')

dataset_combinations = [(500, "sorted"), (500, "random"), (500, "reversed"),
                        (5000, "sorted"), (5000, "random"), (5000, "reversed"),
                        (50000, "sorted"), (50000, "random"), (50000, "reversed")]

save_dataset_to_text(dataset_combinations)
