from collections import Counter

file_path = "your_file.txt"  # Replace "your_file.txt" with the actual file path

with open(file_path, "r") as file:
    text = file.read()

words = text.split()
word_counter = Counter(words)

for word, freq in word_counter.items():
    print(f"{word} = {freq}")
