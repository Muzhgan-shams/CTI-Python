import random
names = ["Emma", "Veronica", "Bety", "Violet", "Elle", "Madolena"]

# First approach
# random_name_one = random.choice(names)
# random_name_two = random.choice(names)
# print(
#     f"Door opener: {random_name_one}\n{random_name_one}, you are on door duty today.")
# print(
#     f"Door holder: {random_name_two}\n{random_name_two}, you are holding the door today.")


# Second approach
selection = random.sample(names, k=2)  # Select 2 unique names into a list
opener = selection[0]  # Extract names by their position in the new list
holder = selection[1]
print(
    f"🚪 Door opener: {opener}\n🗝️  {opener}, you are on door duty today 😊\n"
)
print(
    f"🚪 Door holder: {holder}\n🙌 {holder}, you are holding the door today ⭐"
)


# Third approach
# i = random.randint(0, len(names)-1)
# j = random.randint(0, len(names)-1)
# if i == j:
#     j = (j + 1) % len(names)
# name1 = names[i]
# name2 = names[j]
# print(
#     f"Door opener: {name1}\n{name1}, you are on door duty today.")
# print(
#     f"Door holder: {name2}\n{name2}, you are holding the door today.")
