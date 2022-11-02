player_score = 12


def game():
    def drink_potion():
        potion_strength = 2
        print(player_score)
        print(potion_strength)

    drink_potion()


game()

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def decrease_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies - 1


enemies = decrease_enemies()
print(f"enemies outside function: {enemies}")



