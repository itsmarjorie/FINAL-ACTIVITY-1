#Part 1: Identify & Create (Warm-up)

# 1. Tuple of 5 favorite fruits
fruits = ("apple", "", "mango", "grapes", "orange")

# 2. List of 5 daily tasks
tasks = ["wake up", "exercise", "eat", "study", "sleep"]

# 3. Set of unique numbers
numbers = set([19, 21, 7, 6, 4, 18, 22])

# 4. Dictionary
student = {
    "name": "Marjorie",
    "age": 18,
    "course": "IT"
}

#PRINT OUTPUT
print("Tuple:", fruits)
print("List:", tasks)
print("Set:", numbers)
print("Dictionary:", student)

# PART 2: MANIPULATION CHALLENGE

# LIST TASKS
tasks = ["wake up", "exercise", "eat", "study", "sleep"]
tasks.append("go to market")
tasks.remove("sleep")
tasks.sort()

print(tasks)

# TUPLE TASKS
fruits = ("apple", "", "mango", "grapes", "orange")
fruits[0] = "pineapple"

# SET TASKS
numbers = set([19, 21, 7, 6, 4, 18, 22])
numbers.add(11)
numbers.remove(18)

print(numbers)

# SHOW DUPLICATES remove
print(set([2, 5, 2, 6, 6, 4, 5]))

# DICTIONARY TASKS
student = {
    "name": "Marjorie",
    "age": 18,
    "course": "IT"
}

student["name"] = "Marj"
student["age"] = "19"

print(student.keys())
print(student.values())
