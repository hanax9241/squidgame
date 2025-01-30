import random


class Player:
    def __init__(self, number):
        self.number = number
        self.strength = 0
        self.agility = 0
        self.endurance = 0
        self.health = 0
        self.inventory = []
        self.redistribute_points = 0
        self.wins = 0
        self.knife_bonus = 0
        self.experience = 0
        self.level = 1
        self.level_up_points = 0
        self.got_normal_knife = False
        self.stole_good_knife = False
        self.visited_women = False
        self.visited_old_man = False
        self.pearls = 0
        self.ak_bonus = 0

    def set_stats(self, strength, agility, endurance):
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.health = self.endurance * 16

    def level_up(self):
        self.level += 1
        self.level_up_points += 3
        self.experience = 0
        print(f"\nУровень повышен.Ваш уровень:{self.level}")

    def redistribute_stats(self):
        total_points = 10 + self.level_up_points
        if self.level_up_points > 0:
            print(f"\nУ вас есть {total_points} очков для перераспределения.")

        if self.redistribute_points <= 0 and self.level_up_points <= 0:
            print("У вас нет очков для перераспределения характеристик.")
            return

        while True:
            try:
                new_strength = int(input(f"Новая сила (текущая: {self.strength}): "))
                new_agility = int(input(f"Новая ловкость (текущая: {self.agility}): "))
                new_endurance = int(input(f"Новая выносливость (текущая: {self.endurance}): "))

                total_points_spent = new_strength + new_agility + new_endurance

                if total_points_spent > total_points or total_points_spent < 0:
                    print(f"В сумме не должно выходить больше {total_points} очков. Попробуйте снова")
                    continue
                if total_points_spent < total_points:
                    print("У вас еще остались лишние очки,попробуйте снова")
                    continue
                if new_strength < 0 or new_agility < 0 or new_endurance < 0:
                    print("Нельзя использовать отрицательные числа,попробуйте снова")
                    continue

                if sum([new_strength, new_agility, new_endurance]) > total_points:
                    print(f"Сумма всех значений не должна быть выше {total_points},попробуйте еще раз")
                    continue

                self.set_stats(new_strength, new_agility, new_endurance)
                self.redistribute_points = 0
                self.level_up_points = 0
                print("Характеристики успешно перераспределены")
                self.print_stats()
                break

            except ValueError:
                print("Пожалуйста, введите целые числа.")

    def print_stats(self):
        print("\nТекущие Характеристики:")
        print(f"Сила: {self.strength}")
        print(f"Ловкость: {self.agility}")
        print(f"Выносливость: {self.endurance}")
        print(f"Здоровье: {self.health}")
        print(f"Текущий уровень: {self.level}")
        print(f"Текущий опыт: {self.experience}/10")
        print(f"Кол-во жемчужин: {self.pearls}")

    def add_experience(self):
        self.experience += random.randint(4, 6)
        if self.experience >= 10:
            self.level_up()

    def print_inventory(self):
        print("\nИнвентарь:")
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Пусто")

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_knife(self):
        if "Обычный нож" in self.inventory:
            self.knife_bonus += 5
            self.inventory.remove("Обычный нож")
            print("Вы использовали обычный нож.Теперь вы будете наносить на 5 больше урона")
        elif "Хороший нож" in self.inventory:
            self.knife_bonus += 10
            self.inventory.remove("Хороший нож")
            print("Вы использовали хороший нож.Теперь вы будете наносить на 10 больше урона")
        else:
            print("У вас нет ножа.")

    def use_food(self):
        if "Еда" in self.inventory:
            heal_amount = random.randint(5, 10)
            self.health += heal_amount
            print(f"Вы использовали еду и восстановили {heal_amount} здоровья.")
            self.inventory.remove("Еда")
        else:
            print("У вас нет еды")

    def use_pearl(self):
        if self.pearls > 0:
            self.pearls -= 1
            print("Вы кинули жемчужину во врага,и она попала в глаз. Враг оглушен,и пропускает свой ход")
            return True
        else:
            print("У вас нет жемчужин")
            return False

    def use_magic_powder(self):
        if "Волшебная пыльца" in self.inventory:
            self.knife_bonus += random.randint(5, 15)
            self.inventory.remove("Волшебная пыльца")
            print("Вы использовали волшебную пыльцу.Ваш урон увеличется в следующей битве.")
            return True
        else:
            print("У вас нет волшебной пыльцы")
            return False

    def use_poison(self):
        if "Фласка с ядом" in self.inventory:
            self.inventory.remove("Фласка с ядом")
            print("Вы использовали фласку с ядом.Враг оглушен,и получил 10 едениц урона.")
            return True
        else:
            print("У вас нет фласки с ядом")
            return False

    def use_ak(self):
        if "Автомат Калашникова" in self.inventory:
            self.ak_bonus += 100
            self.inventory.remove("Автомат Калашникова")
            print("Вы использовали Автомат Калашникова и навсегда увеличили урон на 100 единиц")
        else:
            print("У вас нет Автомата Калашникова")


class Dalgoana:
    def __init__(self, name, min_damage, max_damage):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.health = 10

    def attack(self):
        return random.randint(self.min_damage, self.max_damage)

    def print_stats(self):
        print(f"Фигура: {self.name}")
        print(f"Урон вашей уверенности: {self.min_damage}-{self.max_damage}")
        print(f"Прочность: {self.health}")


class Enemy:
    def __init__(self, name, strength, agility, endurance):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.health = endurance * 10

    def attack(self):
        return self.strength + random.randint(1, 2)

    def print_stats(self):
        print(f"Противник: {self.name}")
        print(f"Сила: {self.strength}")
        print(f"Ловкость: {self.agility}")
        print(f"Выносливость: {self.endurance}")
        print(f"Здоровье: {self.health}")


def create_enemy():
    enemies = [
        Enemy("Мужчина с розочкой", 5, 2, 4),
        Enemy("Мужчина без оружия", 3, 3, 3),
        Enemy("Женщина с битой", 4, 4, 2),
        Enemy("Женщина без оружия", 1, 5, 1)
    ]
    return random.choice(enemies)


def battle(player, enemy=None):
    if enemy == None:
        enemy = create_enemy()
        print("\nВы столкнулись со случайным врагом!")

    enemy.print_stats()

    while player.health > 0 and enemy.health > 0:
        print(f"\nВаше здоровье: {player.health}")
        print(f"Здоровье противника: {enemy.health}")
        print("Выберите действие:")
        print("1. Атаковать")
        print("2. Уклониться")
        print("3. Инвентарь")
        if player.pearls > 0:
            print("4. Кинуть жемчужину")

        choice = input("Введите номер действия: ")

        if choice == "1":
            player_attack = player.strength + random.randint(1, 2) + player.knife_bonus + player.ak_bonus
            enemy.health -= player_attack
            print(f"Вы нанесли {player_attack} урона!")
            player.knife_bonus = 0
        elif choice == "2":
            if random.randint(1, 10) <= player.agility:
                print("Вы успешно уклонились от атаки!")
            else:
                enemy_attack = enemy.attack()
                player.health -= enemy_attack
                print(f"Вам нанесли {enemy_attack} урона!")
        elif choice == "3":
            player.print_inventory()
            while True:
                print("1. Использовать еду") if "Еда" in player.inventory else None
                print(
                    "2. Использовать нож") if "Обычный нож" in player.inventory or "Хороший нож" in player.inventory else None
                print("3. Использовать волшебную пыльцу") if "Волшебная пыльца" in player.inventory else None
                print("4. Использовать фласку с ядом") if "Фласка с ядом" in player.inventory else None
                print("5. Использовать Автомат Калашникова") if "Автомат Калашникова" in player.inventory else None
                print("6. Ничего")
                inventory_choice = input("Выберите действие:")
                if "Еда" in player.inventory and inventory_choice == "1":
                    player.use_food()
                    break
                elif (
                        "Обычный нож" in player.inventory or "Хороший нож" in player.inventory) and inventory_choice == "2":
                    player.use_knife()
                    break
                elif "Волшебная пыльца" in player.inventory and inventory_choice == "3":
                    player.use_magic_powder()
                    break
                elif "Фласка с ядом" in player.inventory and inventory_choice == "4":
                    if player.use_poison():
                        enemy.health -= 10
                        break
                elif "Автомат Калашникова" in player.inventory and inventory_choice == "5":
                    player.use_ak()
                    break
                elif inventory_choice == "6":
                    break
                else:
                    print("Неверный выбор")
        elif choice == "4":
            if player.use_pearl():
                enemy.health -= 2
            else:
                continue
        else:
            print("Неверный выбор.")
            continue

        if enemy.health > 0:
            if choice != "4" or player.pearls == 0:
                enemy_attack = enemy.attack()
                player.health -= enemy_attack
                print(f"Вам нанесли {enemy_attack} урона!")

    if player.health <= 0:
        print("Вы проиграли в бою, игра окончена")
        return False
    else:
        print("Вы одержали победу!")
        player.add_experience()
        return True


def night(player):
    night_actions = 0
    visited_location = False
    while night_actions < 3:
        print("\nНаступила ночь. Что вы будете делать?")
        print("1. Лечь спать")
        print("2. Сидеть настороже, ожидая утра")
        print("3. Перераспределить характеристики")
        print("4. Посмотреть инвентарь")
        print("5. Осмотреть комнату")
        choice = input("Введите номер действия: ")

        if choice == "1":
            if random.randint(1, 4) == 1:
                print("К сожалению, вас убили во сне.")
                return False
            else:
                print("Вы выжили эту ночь.")
                return True
        elif choice == "2":
            if random.randint(0, 1) == 0:
                print("Вы не встретили никаких опасностей")
                night_actions += 1
            else:
                print("На вас напали")
                if battle(player):
                    night_actions += 1
                else:
                    return False
        elif choice == "3":
            player.redistribute_stats()
        elif choice == "4":
            player.print_inventory()
        elif choice == "5":
            if not visited_location:
                visited_location = True
                night_actions += 1

            while True:
                print("\nКуда вы хотите пойти?")
                print("1. Задиры")
                print("2. Простые ребята")
                print("3. Группа женщин")
                print("4. Одинокий старик")
                print("5. Вернуться на свою койку")

                location_choice = input("Введите номер места: ")

                if location_choice == "1":
                    print("\nВы подошли к задирам. Они настроены агрессивно.")
                    if battle(player, Enemy("Задира", 6, 3, 5)):
                        print("Вы отбились от задиры и вернулись на койку")
                    else:
                        return False
                    break
                elif location_choice == "2":
                    print("\nВы подошли к простым ребятам.")

                    if player.got_normal_knife:
                        print("Вы уже попросили помощи,и у вас нет возможности сделать это снова")
                        while True:
                            print("1. Осмотреть их лагерь")
                            print("2. Отойти от их лагеря")
                            guys_choice = input("Выберите действие: ")

                            if guys_choice == "1":
                                if not player.stole_good_knife:
                                    while True:
                                        print("Вы замечаете хороший нож,хотите попытаться его украсть?")
                                        print("1. Да")
                                        print("2. Нет")
                                        steal_choice = input("Выберите действие:")
                                        if steal_choice == "1":
                                            if random.randint(1, 100) <= 65:
                                                player.add_to_inventory("Хороший нож")
                                                player.stole_good_knife = True
                                                print(
                                                    "Вы украли хороший нож,теперь при использовании в бою,он навсегда увеличит ваш урон")
                                                break
                                            else:
                                                print("Вы провалили попытку кражи!")
                                                if battle(player, Enemy("Мужчина без оружия", 3, 3, 3)):
                                                    print("Вы победили мужчину,и вернулись на свою койку")
                                                else:
                                                    return False
                                                break
                                        elif steal_choice == "2":
                                            print("Вы проигнорировали находку и вернулись к ребятам")
                                            break
                                        else:
                                            print("Неверный выбор")
                                            continue
                                    break
                                else:
                                    print("Вы уже украли хороший нож,и у вас нет возможности сделать это снова")
                                    break
                            elif guys_choice == "2":
                                break
                            else:
                                print("Неверный выбор")
                                continue
                        break

                    else:
                        while True:
                            print("1. Попросить о помощи")
                            print("2. Осмотреть их лагерь")
                            print("3. Отойти от их лагеря")
                            guys_choice = input("Выберите действие: ")
                            if guys_choice == "1":
                                print("Они решили помочь вам и дали вам обычный нож")
                                player.add_to_inventory("Обычный нож")
                                player.got_normal_knife = True
                                break
                            elif guys_choice == "2":
                                if not player.stole_good_knife:
                                    while True:
                                        print("Вы замечаете хороший нож,хотите попытаться его украсть?")
                                        print("1. Да")
                                        print("2. Нет")
                                        steal_choice = input("Выберите действие:")
                                        if steal_choice == "1":
                                            if random.randint(1, 100) <= 65:
                                                player.add_to_inventory("Хороший нож")
                                                player.stole_good_knife = True
                                                print(
                                                    "Вы украли хороший нож,теперь при использовании в бою,он навсегда увеличит ваш урон")
                                                break
                                            else:
                                                print("Вы провалили попытку кражи!")
                                                if battle(player, Enemy("Мужчина без оружия", 3, 3, 3)):
                                                    print("Вы победили мужчину,и вернулись на свою койку")
                                                else:
                                                    return False
                                                break
                                        elif steal_choice == "2":
                                            print("Вы проигнорировали находку и вернулись к ребятам")
                                            break
                                        else:
                                            print("Неверный выбор")
                                            continue
                                    break
                                else:
                                    print("Вы уже украли хороший нож,и у вас нет возможности сделать это снова")
                                    break

                            elif guys_choice == "3":
                                break
                            else:
                                print("Неверный выбор")
                                continue
                        break

                elif location_choice == "3":
                    if player.visited_women:
                        print("Вы подходите к лагерю женщин,но обнаруживаете что их всех убили задиры")
                    else:
                        if player.health < 30:
                            print("Женщины испугались из-за вашего плохого состояния,и отказались контактировать")
                        else:
                            player.add_to_inventory("Еда")
                            print("Вы поговорили с женщинами и получили еду.")
                            player.visited_women = True
                    break
                elif location_choice == "4":
                    if player.visited_old_man:
                        print("Вы подходите к койке старика,но никого там не находите.")
                        while True:
                            print("1. Осмотреть койку")
                            print("2. Вернуться на свою койку")
                            old_man_choice = input("Выберите действие: ")
                            if old_man_choice == "1":
                                print("На койке ничего нет")
                                break
                            elif old_man_choice == "2":
                                break
                            else:
                                print("Неверный выбор")
                                continue
                    else:
                        print("\nВы подошли к старику. Он предлагает вам сыграть в карты.")
                        while True:
                            play_cards = input("Сыграть в карты? (да/нет): ").lower()
                            if play_cards == "да":
                                print("Вы всю ночь играли в карты. Ночь прошла")
                                night_actions = 3
                                player.visited_old_man = True
                                break
                            elif play_cards == "нет":
                                print("Вы отказались,и вернулись на свою койку")
                                break
                            else:
                                print("Неверный выбор")
                                continue
                    break
                elif location_choice == "5":
                    break
                else:
                    print("Неверный выбор.")
                    continue
        else:
            print("Неверный выбор.")
    return True


def dalgona_game(player):
    print("\nВы решили попытать свою удачу в каких то странных играх,и попали на первую из них. Добро пожаловать в игру Далгона!")
    skip = input("Пропустить игру? (да/нет): ").lower()
    if skip == "да":
        print("Игра пропущена")
        return True
    print("Выберите фигуру, которую вы будете вырезать:")
    print("1. Круг")
    print("2. Треугольник")
    print("3. Звезда")
    print("4. Зонтик")

    while True:
        try:
            choice = int(input("Введите номер фигуры (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Неверный выбор. Введите число от 1 до 4.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    if choice == 1:
        dalgona = Dalgoana("Круг", 1, 2)
    elif choice == 2:
        dalgona = Dalgoana("Треугольник", 0, 1)
    elif choice == 3:
        dalgona = Dalgoana("Звезда", 2, 4)
    else:
        dalgona = Dalgoana("Зонтик", 4, 6)

    print(f"Вы выбрали {dalgona.name}. Начинаем вырезание!")
    dalgona.print_stats()
    player_health = 10

    while player_health > 0 and dalgona.health > 0:
        print("\nВыберите действие:")
        print("1. Попытаться вырезать фигуру")

        action = input("Введите номер действия: ")

        if action == "1":
            player_attack = player.agility
            dalgona.health -= player_attack
            print(f"Вы нанесли {player_attack} урона.")
        else:
            print("Неверный выбор.")
            continue

        if dalgona.health <= 0:
            print("Вы успешно вырезали фигуру!")
            return True

        dalgona_attack = dalgona.attack()
        player_health -= dalgona_attack
        print(f"Печенье трескается,и наносит {dalgona_attack} урона вашей уверенности.")

        print(f"Ваша уверенность: {player_health}, Прочность фигуры: {dalgona.health}")

        if player_health <= 0:
            print("Вы проиграли в игре Далгона.")
            return False


def pearl_game(player):
    print("\nДобро пожаловать в игру 'Жемчужины'!\n Вам необходимо сделать так,чтобы у вас было 20 жемчужин. Вы играете против другого игрока.У вас по 10 жемчужин.\nВы делаете ставку,и ваш оппонент тоже делает ставку.далее вы угадываете,четная ли ставка у врага,или нет.\nЕсли вы угадываете,то враг отдает вам свою ставку,а если вы ошибаетесь,то враг забирает вашу.\nДалее враг делает то же самое.")
    skip = input("Пропустить игру? (да/нет): ").lower()
    if skip == "да":
        print("Игра пропущена")
        return True

    opponent_number = random.choice([i for i in range(1, 457) if i != player.number])
    print(f"Ваш противник: Игрок {opponent_number}")

    player_pearls = 10
    opponent_pearls = 10

    while player_pearls > 0 and opponent_pearls > 0:
        print(f"\nВаши жемчужины: {player_pearls}")
        print(f"Жемчужины противника: {opponent_pearls}")

        while True:
            try:
                player_bet = int(input("Сколько жемчужин вы ставите? "))
                if 1 <= player_bet <= player_pearls:
                    break
                else:
                    print("Ставка должна быть не меньше 1 и не больше ваших жемчужин")
            except ValueError:
                print("Введите целое число")

        opponent_bet = random.randint(1, min(opponent_pearls, player_bet))

        while True:
            guess = input("Четное или нечетное? (чет/нечет): ").lower()
            if guess in ["чет", "нечет"]:
                break
            else:
                print("Введите 'чет' или 'нечет'")

        if (opponent_bet % 2 == 0 and guess == "чет") or (opponent_bet % 2 != 0 and guess == "нечет"):
            print(f"Противник поставил {opponent_bet} жемчужин.")
            print(f"Вы угадали! Забираете {opponent_bet} жемчужин противника.")
            player_pearls += opponent_bet
            opponent_pearls -= opponent_bet
        else:
            print(f"Противник поставил {opponent_bet} жемчужин.")
            print(f"Вы не угадали! Отдаете {player_bet} жемчужин противнику.")
            player_pearls -= player_bet
            opponent_pearls += opponent_bet

        if player_pearls <= 0 or opponent_pearls <= 0:
            break

        if player_pearls > 0 and opponent_pearls > 0:
            print("Ход противника")

            while True:
                try:
                    player_bet = int(input("Сколько жемчужин вы ставите? "))
                    if 1 <= player_bet <= player_pearls:
                        break
                    else:
                        print("Ставка должна быть не меньше 1 и не больше ваших жемчужин")
                except ValueError:
                    print("Введите целое число")

            opponent_bet = random.randint(1, min(opponent_pearls, player_bet))
            print(f"Противник сделал ставку: {opponent_bet}")
            if random.randint(0, 1) == 1:
                print(f"Противник угадал вашу ставку,и забрал {player_bet} жемчужин")
                opponent_pearls += player_bet
                player_pearls -= player_bet
            else:
                print(f"Противник не угадал вашу ставку,и вы забрали {opponent_bet} жемчужин")
                player_pearls += opponent_bet
                opponent_pearls -= opponent_bet

    if player_pearls <= 0:
        print("Вы проиграли в игре 'Жемчужины,и были нейтрализованы'.")
        return False
    else:
        print("Вы выиграли в игре 'Жемчужины'!")
        player.pearls += 12
        print("Вы решаете забрать себе жемчужины,но роняете часть из них,у вас остается только 12 штук.Берегите их,они могут пригодиться...")
        return True


def glass_bridge_game(player):
    print("\nДобро пожаловать в игру 'Стеклянный мост'! Испытание было рассчитано на несколько человек,но увы,прошлой ночью все умерли\nНадеюсь,что вы сохранили жемчужины. Удачи!")
    skip = input("Пропустить игру? (да/нет): ").lower()
    if skip == "да":
        print("Игра пропущена")
        return True

    bridge_length = 14
    for stage in range(1, bridge_length + 1):
        print(f"\n--- Этап {stage} ---")

        safe_glass = random.choice(["левое", "правое"])

        while True:
            print("Перед вами два стекла: левое и правое.")
            print("1. Прыгнуть на левое стекло")
            print("2. Прыгнуть на правое стекло")
            if player.pearls > 0:
                print("3. Бросить жемчужину")

            choice = input("Выберите действие: ")

            if choice == "1":
                selected_glass = "левое"
                if selected_glass == safe_glass:
                    print("Вы успешно перешли на следующий этап!")
                    break
                else:
                    print("Стекло разбилось! Вы упали и погибли!")
                    return False
            elif choice == "2":
                selected_glass = "правое"
                if selected_glass == safe_glass:
                    print("Вы успешно перешли на следующий этап!")
                    break
                else:
                    print("Стекло разбилось! Вы упали и погибли!")
                    return False
            elif choice == "3" and player.pearls > 0:
                player.pearls -= 1
                print(f"Вы кинули жемчужину. Безопасное стекло: {safe_glass}")
            elif choice == "3" and player.pearls <= 0:
                print("У вас нет жемчужин")
            else:
                print("Неверный выбор,попробуйте снова")

    print("\nПоздравляем! Вы успешно преодолели Стеклянный мост!")
    return True


def endless_mode(player):
    enemy_wins = 0
    player_wins = 0

    while True:

        if player_wins % 2 == 0 and player_wins != 0:
            player.health = player.endurance * 10
            player.redistribute_stats()
            print("Комната отдыха")

        if battle(player):
            player_wins += 1
            if random.randint(1, 100) <= 20:
                print("Враг оставил после себя волшебную пыльцу")
                player.add_to_inventory("Волшебная пыльца")
            if random.randint(1, 100) <= 50:
                print("Враг оставил после себя фласку с ядом")
                player.add_to_inventory("Фласка с ядом")
            if random.randint(1, 100) <= 5:
                print("Враг оставил после себя Автомат Калашникова!")
                player.add_to_inventory("Автомат Калашникова")
            player.print_stats()

            while True:
                choice = input("Продолжить или закончить? (продолжить/закончить): ").lower()
                if choice == "продолжить":
                    break
                elif choice == "закончить":
                    print("Игра закончена")
                    return
                else:
                    print("Неверный выбор")
        else:
            print("Игра окончена")
            return


def main():
    while True:
        try:
            number = int(input("Выберите свой номер участника (1-456): "))
            if 1 <= number <= 456:
                break
            else:
                print("Номер должен быть в диапазоне от 1 до 456.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    player = Player(number)

    print(f"Отлично, вы - Игрок {player.number}.")
    print("Ваши характеристики будут показаны ниже. Вы сможете их перераспределить при достижении нового уровня")

    strength = random.randint(5,7)
    agility = random.randint(5,7)
    endurance = random.randint(5,7)
    player.set_stats(strength,agility,endurance)

    player.print_stats()

    game_active = True
    night_number = 1
    while game_active:
        if player.wins >= 3:
            print("Вы прошли все испытания,и выйграли 45 миллиардов рублей. Поздравляем с победой!")
            while True:
                choice = input("Хотите ли вы продолжить в бесконечном режиме? (да/нет): ").lower()
                if choice == "да":
                    endless_mode(player)
                    return
                elif choice == "нет":
                    print("Игра закончена")
                    return
                else:
                    print("Неверный выбор")

        if player.wins == 0:
            if dalgona_game(player) == False:
                game_active = False
                break
            player.wins += 1
            print("Далгона пройдена. Наступает ночь", night_number)
            if night(player) == False:
                game_active = False
                break
        elif player.wins == 1:
            if pearl_game(player) == False:
                game_active = False
                break
            player.wins += 1
            print("Жемчужины пройдена,наступает ночь", night_number)
            if night(player) == False:
                game_active = False
                break
        elif player.wins == 2:
            if glass_bridge_game(player) == False:
                game_active = False
                break
            player.wins += 1
            print("Стеклянный мост пройден")

        night_number += 1
        print("Следующий день")


if __name__ == "__main__":
    main()