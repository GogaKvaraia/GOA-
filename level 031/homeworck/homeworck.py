# 2. Double the numbers in a list using map
numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)

# 3. Concatenate "Hello, " to each name in a list using map
names = ["Alice", "Bob", "Charlie"]
greeted_names = list(map(lambda name: f"Hello, {name}", names))
print("Greeted names:", greeted_names)

# 4. Calculate the lengths of strings in a list using map
words = ["apple", "banana", "kiwi"]
lengths = list(map(len, words))
print("Lengths of strings:", lengths)

# 5. Keep only positive numbers from a list using filter
numbers_with_negatives = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers_with_negatives))
print("Positive numbers:", positive_numbers)

# 6. Extract words starting with the letter "p" from a list using filter
fruits = ["pear", "apple", "peach", "grape"]
p_words = list(filter(lambda word: word.startswith("p"), fruits))
print("Words starting with 'p':", p_words)

# 7. Find numbers greater than 50 in a list using filter
random_numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, random_numbers))
print("Numbers greater than 50:", greater_than_50)
