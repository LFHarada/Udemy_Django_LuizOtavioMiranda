import random

character = "YKZV368GYCGU87E9AT2FPHDR"
characters = list(character)


def generate_random_code():
    while True:
        print("Generating random code...")
        random.shuffle(characters)
        code = []
        for i in range(12):
            code.append(random.choice(characters))
        random.shuffle(code)
        print("".join(code))


generate_random_code()
