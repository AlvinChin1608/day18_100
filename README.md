# day18_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner stage and later on intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------------------------------
# Python Tuple
## What is a Tuple?
A tuple is a collection data type in Python that is ordered and immutable, meaning once a tuple is created, its elements cannot be changed. Tuples are defined by enclosing the elements in parentheses ().

**Creating Tuples**
You can create a tuple by placing a comma-separated sequence of elements within parentheses:
```python
my_tuple = (1, 2, 3)
another_tuple = ("apple", "banana", "cherry")
mixed_tuple = (1, "apple", 3.5)
```
**Accessing Tuple Elements**
You can access elements in a tuple using indexing, similar to lists:
```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
```
**Converting Tuples to Lists**
Although tuples are immutable, you can convert them to a list if you need to make changes:
```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
**When to Use Tuples**
- Use tuples when you want to ensure that the data remains constant throughout the program.
- Tuples are useful when you need to store heterogeneous data.
- They are also more memory-efficient compared to lists.
