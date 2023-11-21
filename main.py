import random


def secret_santa(names):
    """Function: Returns a list of secret santa's and their receivers in a format."""
    secret_santa_names = names
    random.shuffle(secret_santa_names)

    first_name = secret_santa_names[0]
    for i in range(len(secret_santa_names)):
        if i == len(secret_santa_names)-1:
            secret_santa_names[i] = secret_santa_names[i] + " = " + first_name + "\n"
        else:
            secret_santa_names[i] = secret_santa_names[i] + " = " + secret_santa_names[i + 1] + "\n"

    return secret_santa_names


# File handling - List of names participating in Secret Santa
with open('names.txt', "r") as file:
    names = file.readlines()

    for i in range(len(names)):
        names[i] = names[i].strip('\n')  # To remove \n

    # Rules for Secret Santa
    # You cannot get assigned to yourself
    # Each person should get assigned someone
    # No person should be repeated
    # Print the result in another file in the format: Dels = Smith
    secret_santa_names = secret_santa(names)

    # Output the secret santa list into a new file
    with open("secret_santa.txt", mode="w") as file:
        for i in range(len(secret_santa_names)):
            file.write(secret_santa_names[i])
