import time
import random

inventory = []
current_episode = 1
game_over = False
player_name = ""


#ИНВЕНТАРЬ
def add_item(item):
    """Добавить предмет в инвентарь"""
    inventory.append(item)
    print(f"\n>>> {item} добавлен в инвентарь")

def remove_item(item):
    """Удалить предмет из инвентаря"""
    if item in inventory:
        inventory.remove(item)
        print(f"\n>>> {item} удален из инвентаря")
        return True
    return False

def show_inventory():
    """Показать инвентарь"""
    if inventory:
        print(f"\n--- ИНВЕНТАРЬ: {', '.join(inventory)} ---")
    else:
        print("\n--- ИНВЕНТАРЬ пуст ---")

def has_item(item):
    """Проверить наличие предмета"""
    return item in inventory

#ПРОВЕРКА И ОШИБКИ
def get_choice(choices):
    while True:
        try:
            choice = input("\nВаш выбор: ").strip().lower()
            if choice in choices:
                return choice
            else:
                print("Неверный выбор. Попробуйте снова.")
        except:
            print("Ошибка ввода. Попробуйте снова.")
#АНИМАЦИЯ ТЕКСТА
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def wait_for_continue():
    input("\nНажмите Enter чтобы продолжить...")

#ПЕРВЫЙ ЭТАП
def episode_1():

    #ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ ДЛЯ ВОЗМОЖНОСТИ ИЗМЕНЕНИЯ ВЫБОРА
    global current_episode
    
    slow_print("\n=== ЭПИЗОД 1: ПРОБУЖДЕНИЕ? ===")
    slow_print("Вы медленно открываете глаза... В голове резкие позывы боли.")
    slow_print("Вокруг темнота, пахнет плесенью и сыростью.")
    slow_print("Вы лежите на холодном полу, сделанный из бетона.")
    
    #ПЕРВЫЙ ВЫБОР
    while True:
        slow_print("\nВаши дальнейшие действия:")
        slow_print("1 - Попытаться встать")
        slow_print("2 - Осмотреться вокруг")
        slow_print("3 - Попытатся что-то вспомнить")
        slow_print("4 - Кричать о помощи")
        slow_print("i - Посмотреть инвентарь")
        
        choice = get_choice(['1', '2', '3', '4', 'i'])
        
        if choice == 'i':
            show_inventory()
            continue
            
        if choice == '1':
            slow_print("\nВы с трудом поднимаетесь на ноги. Голова кружится.")
            slow_print("Вы стоите в небольшом подвале примерно 3x3 метра.")
            break
        elif choice == '2':
            slow_print("\nВ полумраке вы различаете:")
            slow_print("- Старую полку с какими-то банками")
            slow_print("- Металлическую дверь в стене")
            slow_print("- Что-то блестящее в углу")
        elif choice == '3':
            slow_print("\nВы вздыхаете и пытаетесь вспомнить как здесь очутились.")
            slow_print("Память возвращается... Вы помните как шли домой вечером,лишь один фонарь ярко светил на тропинку, возле которой не было не души кроме вас...")
            slow_print("И потом... темнота.")
        elif choice == '4':
            slow_print("\nВы кричите: 'Помогите! Кто-нибудь!'")
            slow_print("В ответ - только эхо. Кажется, вы совсем одни.")
    
    #ИССЛЕДОВАНИЕ ПОДВАЛА
    door_locked = True
    key_found = False
    
    while door_locked:
        slow_print("\nВы в центре подвала. Что вам приглянулось?")
        slow_print("1 - Металлическая дверь")
        slow_print("2 - Полка с банками") 
        slow_print("3 - Мелькающий предмет в углу")
        slow_print("4 - Стены подвала")
        slow_print("i - Инвентарь")
        
        choice = get_choice(['1', '2', '3', '4', 'i'])
        
        if choice == 'i':
            show_inventory()
            
        elif choice == '1':
            slow_print("\nВы подходите к металлической двери.")
            slow_print("Она выглядит масивной. Ручка холодная, вы дергаете ее несколько раз, не поддается, видимо она заперта...")
            if has_item('ключ'):
                slow_print("Вы используете ключ... Замок щелкает!")
                slow_print("Дверь открывается...")
                door_locked = False
            else:
                slow_print("Вам нужен ключ.")
                
        elif choice == '2':
            slow_print("\nНа полке стоят несколько запыленных банок.")
            slow_print("В одной из них что-то шевелится... Лучше не трогать.")
            if not has_item('записка'):
                slow_print("За одной из банок вы находите смятую записку")
                add_item('записка')
                
        elif choice == '3':
            slow_print("\nВы подходите к блестящему предмету.")
            slow_print("Оказывается это старый ржавый ключ")
            if not key_found:
                add_item('ключ')
                key_found = True
                
        elif choice == '4':
            slow_print("\nСтены подвала влажные, покрыты плесенью.")
            slow_print("На одной стене вы находите странные царапины...")
            slow_print("Легкая дрожь бежит по вашей спине, к вам приходят скверные мысли...")
    
    #ВЫХОД
    slow_print("\nДверь ведет в темный коридор...")
    slow_print("Вы делаете шаг вперед...")
    wait_for_continue()
    current_episode = 2

#ВТОРОЙ ЭТАП
def episode_2():
    global current_episode

    slow_print("\n=== ЭПИЗОД 2: СТАРЫЙ ДОМ  ===")
    slow_print("Вы выходите из подвала в темный коридор.")
    slow_print("Воздух тяжелый, пахнет дезинфекцией и чем-то сладковатым...")
    
    #ОСОБЫВ ПРЕДМЕТЫ
    clues_needed = ['фотография', 'дневник', 'нож', 'медальон']
    clues_found = []
    
    #КОМНАТА ИССЛЕДОВАНИЯ
    rooms_visited = []
    
    while len(clues_found) < len(clues_needed):
        slow_print(f"\n--- Найдено улик: {len(clues_found)}/{len(clues_needed)} ---")
        slow_print("\nКуда вы пойдете?")
        
        rooms = []
        if 'коридор' not in rooms_visited:
            rooms.append("1 - Исследовать коридор")
        if 'кухня' not in rooms_visited or not has_item('нож'):
            rooms.append("2 - Заглянуть на кухню")
        if 'гостиная' not in rooms_visited or not has_item('дневник'):
            rooms.append("3 - Пройти в гостиную")
        if 'спальня' not in rooms_visited or not has_item('фотография'):
            rooms.append("4 - Осмотреть спальню")
        if 'ванная' not in rooms_visited or not has_item('медальон'):
            rooms.append("5 - Проверить ванную")
        if all(room in rooms_visited for room in ['коридор', 'кухня', 'гостиная', 'спальня', 'ванная']):
            rooms.append("6 - Попытаться найти выход")
            
        rooms.append("i - Инвентарь")
        
        for room in rooms:
            slow_print(room)
        
        choice = get_choice(['1', '2', '3', '4', '5', '6', 'i'])
        
        if choice == 'i':
            show_inventory()
            continue
            
        if choice == '1':
            slow_print("\nВы в коридоре. На стенах висят странные картины, их гримассы наводят на вас ужас...")
            slow_print("Вы задумываетесь о том как сюда попали и за что вы были заперты в этом доме.")
            slow_print("С каждой последующей картиной гримассы становились все страшнее и уродливее, вы решили быстро пройти дальше.")
            rooms_visited.append('коридор')
            
        elif choice == '2':
            slow_print("\nКухня... Нет уж, скорее комната пыток...")
            slow_print("Стол покрыт пятнами, несколько разных инструментов разложены в возростающем порядке.")
            if not has_item('нож'):
                slow_print("В начале инструметов вы замечаете небольшой нож с резной ручкой и красивым узором в виде бабочки с боку рукоятки.")
                add_item('нож')
                clues_found.append('нож')
            rooms_visited.append('кухня')
            
        elif choice == '3':
            slow_print("\nГостиная. Мебель старая, покрыта пылью, по середине стоит манекен и будто держит в руке...")
            slow_print("На журнальном столике лежит толстая книга.")
            if not has_item('дневник'):
                slow_print("Дневник! Вы подбираете на вид чистый дневник. Страницы исписаны на непонятном для вас языке.")
                add_item('дневник')
                clues_found.append('дневник')
            rooms_visited.append('гостиная')
            
        elif choice == '4':
            slow_print("\nСпальня. Кровать заправлена идеально.")
            slow_print("На тумбочке стоит фотография в рамке.")
            if not has_item('фотография'):
                slow_print("На фото - человек, его глаза кажутся пустыми и пугающими...")
                add_item('фотография')
                clues_found.append('фотография')
            rooms_visited.append('спальня')
            
        elif choice == '5':
            slow_print("\nВанная комната. Зеркало разбито.")
            slow_print("Под разбившемся стеклом на раковине вы замечаете старый медальон.")
            if not has_item('медальон'):
                slow_print("Вы рассматриваете медальен и находите в нем прядь волос...")
                add_item('медальон')
                clues_found.append('медальон')
            rooms_visited.append('ванная')
            
        elif choice == '6' and len(clues_found) == len(clues_needed):
            slow_print("\nУ вас есть все улики! Пора выбираться!")
            break
    
    #ДЕЙСТВИЕ ПЕРВОЕ
    slow_print("\nВы собрали все улики и направляетесь к выходу...")
    slow_print("Неожиданно сзади раздаются приглушенные шаги...")
    slow_print("Вы слышите тяжело дыхание...")
    slow_print("Страх сковывает вас, но вы решаетесь обернутся...")
    wait_for_continue()
    current_episode = 3

#ТРЕТИЙ ЭТАП
def episode_3():
    global game_over
    
    slow_print("\n=== ЭПИЗОД 3: ПРАВДА ===")
    slow_print("...но вместо ожидаемой смерти все вокруг начинает расплываться.")
    slow_print("Стены тают, пол уходит из-под ног...")
    slow_print("Вы чувствуете, что падете в темнату...")
    wait_for_continue()
    
    slow_print("\n*** ЩЕЛЧЕК ***")
    slow_print("Вы резко открываете глаза.")
    slow_print("Вы лежите на холодном полу... в том же подвале.")
    slow_print("Рядом стоит человек в маске.")
    
    slow_print("\nНезнакомец снимает маску...")
    slow_print("Это доктор Энтони Сварнесс из психиатрической клиники.")
    
    slow_print(f"\nДоктор: 'Простите, {player_name}. Эксперимент провалился...'")
    slow_print("Доктор: 'Ваше сознание в замешательству, не понимая что происходит вы с недоумением смотрите на доктора.'")
    slow_print("Доктор: 'Все эти улики... дом маньяка... это была симуляция.'")
    
    #ФИНАЛОЧКА
    slow_print("\nСобираясь с мыслями вы отвечаете:")
    slow_print("1 - 'Я ведь на самом деле умер...Да?'")
    slow_print("2 - 'Зачем вы это сделали?'")
    slow_print("3 - Молчать, пытаясь осознать")
    
    choice = get_choice(['1', '2', '3'])
    
    if choice == '1':
        slow_print("\nДоктор: 'Что вы, конечно же нет. Мы пытались вылечить ваши фобии.'")
    elif choice == '2':
        slow_print("\nДоктор: 'Это была терапия. В детстве вы попали в страшную ситуацию...\nПосле многих лет вы решили обратиться к нам за помощью.'")
    else:
        slow_print("\nДоктор смотрит на вас с сожалением: 'Я понимаю, это шок...Скоро вы все вспомните.'")
    
    slow_print("\nДоктор помогает вам подняться.")
    slow_print("Вы выходите из белой комнаты, похожей на лабораторию.")
    slow_print("Все это время вы были подключены к аппаратуре.")
    
    #ВЫБОР КОНЦОВКИ
    slow_print("\nДоктор предлагает: 'Хотите посмотреть записи эксперимента?'")
    slow_print("1 - Посмотреть записи")
    slow_print("2 - Уйти и забыть")
    
    choice = get_choice(['1', '2'])
    
    if choice == '1':
        slow_print("\nНа экране - вы в подвале. Ваши движения скованы, лицо искажено страхом.")
        slow_print("Доктор: 'Ваш разум воссоздал целуя историю, которая когда то коснулась вас, но увы эти шрамы навсегда останутся с вами...'")
        slow_print("Вы чувствуете боль в груди... И ощущаете пустоту, пожирающую вас изнутри.")
        slow_print("Спустя несколько месяцев вы вновь приходите к Mr.Энтони.")
        slow_print("Доктор: 'Добрый день сер, что у вас случилось?'\n{player_name}: 'Доктор мне...\nнужна...\nТерапия.'")
    else:
        slow_print("\nВы выходите из клиники. Солнце слепит глаза.")
        slow_print("Но что-то гложет вас... Чувство дежавю?")
    
    slow_print("\n=== КОНЕЦ ИГРЫ ===")
    slow_print("Спасибо за прохождение!")
    game_over = True

#СТАРТОВОЕ МЕНЮ
def main_menu():
    slow_print("=== СТРАХ ===")
    slow_print("Психологический хоррор-новелла")
    slow_print("\n1 - Начать игру")
    slow_print("2 - Об игре")
    slow_print("3 - Выйти")
    
    choice = get_choice(['1', '2', '3'])
    return choice

def about_game():
    slow_print("\n=== ОБ ИГРЕ ===")
    slow_print("'Темные сны' - психологический хоррор")
    slow_print("Исследуйте локации, собирайте предметы")
    slow_print("и раскройте тайну своего появления.")
    slow_print("\nУправление:")
    slow_print("- Выбирайте цифры для действий")
    slow_print("- i - посмотреть инвентарь")
    wait_for_continue()

#ЦИКЛЫ
def main():
    global player_name, current_episode, game_over, inventory
    
    slow_print("Добро пожаловать в игру!")
    
    while not game_over:
        choice = main_menu()
        
        if choice == '1':
            #СБРОС
            inventory = []
            current_episode = 1
            game_over = False
            
            #ИМЯ
            player_name = input("\nВведите имя персонажа: ").strip()
            if not player_name:
                player_name = "Кевин"
            
            slow_print(f"\nДобро пожаловать, {player_name}! Приготовьтесь к испытанию...")
            wait_for_continue()
            
            #СТАРТ ЭПИЗОДОВ
            while not game_over:
                if current_episode == 1:
                    episode_1()
                elif current_episode == 2:
                    episode_2()
                elif current_episode == 3:
                    episode_3()
                    
        elif choice == '2':
            about_game()
        elif choice == '3':
            slow_print("До свидания!")
            break

#ЗАПУСК ИГРЫ
if __name__ == "__main__":
    main()