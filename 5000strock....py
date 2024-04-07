print('Чтобы виртульный помощник работал корректно, нужно запустить код в IDE редакторе')

# import time, random, webbrowser as wb, os, colorama
# from colorama import Fore, Back
# colorama.init()

# def all_assist():
#     greeting = 'Привет пользователь, меня зовут Vox или же просто V'
#     for char in greeting: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')

#     name_user = input('Как я могу обращаться к вам? ')
#     age_user = input('Сколько вам лет? ')

#     acquaintance = f'Очень приятно {name_user}'
#     for char in acquaintance: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')
# time.sleep(2)

# functions = "Я умею многое!"
# for char in functions: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')
# print(' ')

# functions_l = 'Вот список того что я умею'
# for char in functions_l: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# def l_func():
#     list_of_functions = '1) Вы можете скоротать время, сыграв в игры!' + Fore.LIGHTBLUE_EX + '(По команде "Давай поиграем")' + Fore.RESET
#     for char in list_of_functions: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')

#     list_of_functions1 = '2) Если вы любите читать, я знаю некоторые произведения!' + Fore.LIGHTBLUE_EX + '(По команде "Хочу читать")' + Fore.RESET
#     for char in list_of_functions1:
#         print(char, end='', flush=True)
#         time.sleep(0.05)
#     print('')

#     list_of_functions2 = '3) Вам нужно решить пример? Я вам помогу!' + Fore.LIGHTBLUE_EX + '(По команде "Посчитай пример")' + Fore.RESET
#     for char in list_of_functions2: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')

#     list_of_functions3 = '4) Я могу поставить таймер, секундомер или подсказать вам время!' + Fore.LIGHTBLUE_EX + '(По команде "Время")' + Fore.RESET
#     for char in list_of_functions3: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')

#     list_of_functions4 = '5) Я дружу с google! Могу найти все!' + Fore.LIGHTBLUE_EX + '(По команде "Найди")' + Fore.RESET
#     for char in list_of_functions4: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')

#     list_of_functions5 = '6) У меня есть рандомайзер' + Fore.LIGHTBLUE_EX + '(По команде "Включи рандомайзер")' + Fore.RESET
#     list_of_functions6 = 'Так же я могу включать: Youtube, прогноз погоды, карту, музыку, Wildberries, google disk, gmail, mail, yandex почту... Я могу открыть все самые часто используемые сайты'
#     for char in list_of_functions6: 
#         print(char, end='', flush=True) 
#         time.sleep(0.05)
#     print('')

#     question_class = input('Чем я могу вам помочь? ')

#     if question_class == 'Давай поиграем' or question_class == 'давай поиграем' or question_class == 'хочу поиграть' or question_class == 'играть':
# list_game = 'Игры:'
# for char in list_game: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# list_game1 = '1) Текстовая игра'
# for char in list_game1: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# list_game2 = '2) Квиз'
# for char in list_game2: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# list_game3 = '3) Угадай животное'
# for char in list_game3: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# list_game4 = '4) Бросить монетку'
# for char in list_game4: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# list_game5 = '5) Морской бой'
# for char in list_game5: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# list_game6 = '6) Камень - ножинцы - бумага'
# for char in list_game6: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')

# game_selection = input('В какую игру сыграем? ')
# if game_selection == 'Текстовая игра' or game_selection == 'текстовая игра':
#     def text_game():
#         while True:
#             door_addition = 'Перед вами'
#             door_addition1 = Fore.BLUE + ' дверь 1'
#             choosing_door = door_addition + door_addition1
#             for char in choosing_door: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             print(Fore.RESET + '____|____|____|____|____|____|____|____|____|____|')
#             print('__|____|____|____|____|____|____|____|____|____|__')
#             print('        _____|____|    _____  |____| _____')
#             print('       /     \        /\   /\       /\   /\ ___')
#             print('__   [|   1   |     [|  \ /  |    [|  \ /  |___|')
#             print('__|   |       |  ___ |   X   |     |   X   |')
#             print('      |     ] | |___||  / \] |     |  / \] |')
#             print('___  [|       |     [| /   \ | __ [| /   \ |')
#             print('___|__|_______|______|/_____\||__|_|/_____\|_____')
#             print('-- --  --   - -   - - -   - --- -     -  - - -  ')
#             print('-   -  - - --  - -- -- --    - - - - -   -- -- -')

#             answer = input('Войти в дверь? ' + Fore.BLUE + 'да/нет ' + Fore.RESET)
#             for char in answer: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             if answer == 'дверь 1':
#                 doors_answer = 'Вы выбрали дверь номер 1' 
#                 for char in doors_answer: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 break


#             elif answer == 'дверь 2':
#                 modification = 'Вы подошли к двери номер 2'
#                 for char in modification: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 modification1 = 'Вы дернули за ручку'
#                 for char in modification1: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 modificarion2 = 'Когда вы открыли дверь, подул сильный ветер'
#                 for char in modificarion2: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 print('(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ sorry')
#                 print('Эта дверь еще в разработке!')
#                 print('У меня был лишком маленький дедлайн')
#                 print('')


#             elif answer == 'дверь 3':
#                 modification = 'Вы подошли к двери номер 3'
#                 for char in modification: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 modification1 = 'Вы дернули за ручку'
#                 for char in modification1: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 modificarion2 = 'Когда вы открыли дверь, послышался громный рык монстра'
#                 for char in modificarion2: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 print(' ')
#                 print('(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ sorry')
#                 print(' ')
#                 print('Эта дверь еще в разработке!')
#                 print('У меня был лишком маленький дедлайн')
#                 print('')

#             elif answer == 'да':
#                 voiti = 'Вы вошли в дверь с номером 1'
#                 for char in voiti: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 break

#             elif answer == 'нет':
#                 die = 'Вы просидели час, смотря на дверь'
#                 for char in die: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#             else:
#                 print('Увы! Такой двери нет!')
#                 print('')

#         tunnel_ticket = False
#         maze_ticket = False
#         pickaxe = False
#         gold = False


#         def all(tunnel_ticket, maze_ticket, pickaxe, gold):

#             game_over = 'Game Over!'

#             choosing_extension = 'Когда вы вошли в 1 дверь, то сразу заметили, что впереди вас находится загадочный '
#             choosing_extension3 = Fore.BLUE + 'лабиринт'
#             choosing_extension2 = Fore.WHITE + ' и темный '
#             choosing_extension1 = Fore.BLUE + 'коридор' + Fore.RESET
#             chose = choosing_extension + choosing_extension1 + choosing_extension2 + choosing_extension3
#             for char in chose: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             print(Fore.RESET + '                  /|\                      /|')
#             print('\                / | \                    / |')
#             print(' \               | |  \                  /  |')
#             print('  \              | |   \                /   |')
#             print('  |              | |    \              /    |')
#             print('  |__          __| |     \            /     |')
#             print('  | |\        |  | |      \          /      |')
#             print('  | | \       |  | |       \        /       |')
#             print('  | |  \    /||  | |        \      /        |')
#             print('  | |   \__| ||  | |         \ __ /         |')
#             print('  | |   |__| ||  | |          |__|          |')
#             print('  | |   /  | ||  | |         /    \         |')
#             print('  | |  /    \||  | |        /      \        |')
#             print('  | | /      \|  | |       /        \       |')
#             print('  |_|/        |__| |      /          \      |')
#             print('  |              | |     /            \     |')
#             print('  |              | |    /              \    |')
#             print(' /                \|   /                \   |')
#             print('/                  \  /                  \  |')

#             chose1 = Fore.RESET + 'Что вы выберите ' + choosing_extension1 + Fore.RESET + ' или ' + choosing_extension3 + '? ' + Fore.RESET
#             answer1 = input(chose1)
#             for char in answer1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')


#             if answer1 == 'коридор':
#                 correction = 'Вы выбрали пойти в коридор'
#                 for char in correction: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('') 

#                 continuation = 'Пройдя по коридору, вы замечаете, что впереди горит яркий свет'
#                 for char in continuation: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 print(".._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..")
#                 print("   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  ")
#                 print("      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  ")
#                 print("..__  |     |`-!._ | `.| |		 ||.  |  _!.;    |      |  ")
#                 print("   |`` ..__ |    | `;.| i|		 |'| _!-|   |   _|..-|'    ")
#                 print("   |      |``--..|_ | `;!|		 |.'j   |_..!-'|     |     ")
#                 print("   |      |    |   |`-,!_|		 ||.!-;'  |    |     |     ")
#                 print("___|______|____!.,.!,.!,!|		 |,!,.!.,.!..__|_____|_____")
#                 print("      |     |    |  |  | |               || |   |   |    |      |  ")
#                 print("      |     |    |..!-;'i|               | |`-..|   |    |      |  ")
#                 print("      |    _!.-j'  | _!, |               ||!._|  `i-!.._ |      |  ")
#                 print("     _!.-'|    | _. |  !;|               |`.| `-._|    |``-.._  |  ")
#                 print("..-i'     |  _.''|  !-| !|               |.|`-. | ``._ |     |`` ..")
#                 print("   |      |.|    |.|  !| |               ||`. |`!   | ` .    |     ")
#                 print("   |  _.-'  |  .'  |.' |/|               |! |`!  `,.|    |-._|     ")
#                 print("  _! '|     !. |  . | . ||               |  \|  `. | `._  |   `-._ ")
#                 print("-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-")
# print("      |_.'|   .' | .' |/                   \  \ |  `.  | `._-   |  ")
# print("     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  ")
# print("  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  ")

# answer2_extension = 'Перед вами встал выбор, пройти по коридору '
# answer2_extension1 = Fore.BLUE + 'дальше '
# answer2_extension2 = Fore.WHITE + 'или развернуться и '
# answer2_extension3 = Fore.BLUE + 'пойти обратно' + Fore.RESET
# answer2_extension_final = Fore.WHITE + answer2_extension + answer2_extension1 + answer2_extension2 + answer2_extension3 + ' '
# answer2 = input(answer2_extension_final)
# for char in answer2: 
#     print(char, end='', flush=True) 
#     time.sleep(0.05)
# print('')


# if tunnel_ticket == False and pickaxe == False:
#     if answer2 == 'дальше':
#         correction1 = 'Вы прошли по коридору, перед вами яркий свет'
#         for char in correction1: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         correction2 = 'Прищурившись вы замечаете, что свет исходит из отверстия в камне'
#         for char in correction2: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         print('\__  __')
#         print('   \/  \  /|____               ________')
#         print('        \/    __\__________  _/         \ ')
#         print('        ___/             \_/            \__')
#         print('      _/                   \               |')
#         print('     /       ______  _      \__            \ ')
#         print('    /        \     \/ |_       \           |')
#         print('    |       _/ _/\   /\/        \______  __\ ')
#         print('    |      /^]/   ^\/         __|      \/')
#         print('    |                   _____/         /')
#         print('     \__     _____   __/               |')
#         print('        \___/     \_/ \     __________/')
#         print('            \          \___|')
#         print('             | ')
#         print('            /')


#         correction3 = 'Посмотрев в отверстие, вы понимаете, что свобода за этим огромным камнем '
#         for char in correction3: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')


#         clarification_with_an_addendum = 'Вы бы могли выбраться, '
#         clarification_with_an_addendum1 = Back.LIGHTBLACK_EX + 'если бы у вас была кирка' + Back.RESET
#         correction4 = clarification_with_an_addendum + clarification_with_an_addendum1
#         for char in correction4: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         answer3_extension = 'Вернуться '
#         answer3_extension1 = Fore.BLUE + 'назад '
#         answer3_extension2 = Fore.WHITE + 'или '
#         answer3_extension3 = Fore.BLUE + 'сдаться?'
#         answer3 = answer3_extension + answer3_extension1 + answer3_extension2 + answer3_extension3 + ' ' + Fore.RESET
#         answer3_inp = input(answer3)
#         for char in answer3_inp: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         if answer3_inp == 'назад':
#             tunnel_ticket = not tunnel_ticket
#             all(tunnel_ticket, maze_ticket, pickaxe, gold)

#         elif answer3_inp == 'сдаться':
#             for char in game_over: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             print('Ваш результат: 0 из 3 звезд')

#         else:
#             print('Увы! Такого выбора нет!')
#             print(' ')


#     elif answer2 == 'пойти обратно':
#         tunnel_ticket = True
#         all(tunnel_ticket, maze_ticket, pickaxe, gold)


#     else:
#         print('Увы! Такого выбора нет!')
#         print(' ')

# elif  tunnel_ticket == True and pickaxe == True:
#     if answer2 == 'дальше':
#         correction1 = 'Вы прошли по коридору, перед вами яркий свет'
#         for char in correction1: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         dig_up_add = Fore.BLUE + 'Раскопать выход' + Fore.RESET + 'или' + Fore.BLUE + 'вернуться назад? ' + Fore.RESET 
#         dig_up = input(dig_up_add)
#         for char in dig_up: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         if dig_up == 'раскопать выход':
#             excavation_with_pickaxe = 'Вы решаетесь раскопать себе проход '
#             for char in excavation_with_pickaxe: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             memory1 = 'Спустя два часа мучений, вы смогли выбраться на свободу!'
#             for char in memory1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             print('       _      _                   ')
#             print('      (_)    | |                  ')
#             print('__   ___  ___| |_ ___  _ __ _   _ ')
#             print("\ \ / / |/ __| __/ _ \| '__| | | |")
#             print(' \ V /| | (__| || (_) | |  | |_| |')
#             print('  \_/ |_|\___|\__\___/|_|   \__, |')
#             print('                             __/ |')
#             print('                            |___/ ')

#             print('Но теперь вы не можекте появляться в горое ,так как вас разыскивают')
#             print('Вы остались без своей любимой')
#             print('Ваш результат: 1 из 3 звезд')

#             print(' ')
#             print('                   ¶                    .                  .         ')
#             print('                  ¶¶¶                  ,O,                ,O,        ')
#             print('	         ¶¶¶¶¶      	      ,O O,              ,O O,       ')
#             print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    "oooooO   Oooooo"  "oooooO   Oooooo" ')
#             print('              ¶¶¶¶¶¶¶¶¶¶¶         `O         O`      `O          O`  ')
#             print('	        ¶¶¶¶¶¶¶             `O     O`          `O     O`     ')
#             print('               ¶¶¶¶_¶¶¶¶            O  O"O  O          O  O"O  O     ')
#             print('              ¶¶¶     ¶¶¶          OOO     OOO        OOO     OOO    ')

#         elif dig_up == 'вернуться назад':
#             all(tunnel_ticket, maze_ticket, pickaxe, gold)

#         else:
#             print('Увы! Такого выбора нет!')
#             print(' ')

# elif tunnel_ticket == False and pickaxe == True:
#     if answer2 == 'дальше':
#         correction1 = 'Вы прошли по коридору, перед вами яркий свет'
#         for char in correction1: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')
#         correction2 = 'Прищурившись вы замечаете, что свет исходит из отверстия в камне'
#         for char in correction2: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         print('\__  __')
#         print('   \/  \  /|____               ________')
#         print('        \/    __\__________  _/         \ ')
#         print('        ___/             \_/            \__')
#         print('      _/                   \               |')
#         print('     /       ______  _      \__            \ ')
#         print('    /        \     \/ |_       \           |')
#         print('    |       _/ _/\   /\/        \______  __\ ')
#         print('    |      /^]/   ^\/         __|      \/')
#         print('    |                   _____/         /')
#         print('     \__     _____   __/               |')
#         print('        \___/     \_/ \     __________/')
#         print('            \          \___|')
#         print('             | ')
#         print('            /')

#         correction3 = 'Посмотрев в отверстие, вы понимаете, что свобода за этим огромным камнем '
#         for char in correction3: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         memory = 'Но у вас есть кирка!'
#         for char in memory: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         dig_up_add = Fore.BLUE + 'Раскопать выход' + Fore.RESET + ' или ' + Fore.BLUE + 'вернуться назад? ' + Fore.RESET 
#         dig_up = input(dig_up_add)
#         for char in dig_up: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')


#             if dig_up == 'раскопать выход':
#                 memory1 = 'Спустя два часа мучений, вы смогли выбраться на свободу!'
#                 for char in memory1: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 print('       _      _                   ')
#                 print('      (_)    | |                  ')
#                 print('__   ___  ___| |_ ___  _ __ _   _ ')
#                 print("\ \ / / |/ __| __/ _ \| '__| | | |")
#                 print(' \ V /| | (__| || (_) | |  | |_| |')
#                 print('  \_/ |_|\___|\__\___/|_|   \__, |')
#                 print('                             __/ |')
#                 print('                            |___/ ')

#                 print('Но теперь вы не можекте появляться в горое ,так как вас разыскивают')
#                 print('Вы остались без своей любимой')
#                 print('Ваш результат: 1 из 3 звезд')

#                 print(' ')
#                 print('                   ¶                    .                  .         ')
#                 print('                  ¶¶¶                  ,O,                ,O,        ')
#                 print('	         ¶¶¶¶¶      	      ,O O,              ,O O,       ')
#                 print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    "oooooO   Oooooo"  "oooooO   Oooooo" ')
#                 print('              ¶¶¶¶¶¶¶¶¶¶¶         `O         O`      `O          O`  ')
#                 print('	        ¶¶¶¶¶¶¶             `O     O`          `O     O`     ')
#                 print('               ¶¶¶¶_¶¶¶¶            O  O"O  O          O  O"O  O     ')
#                 print('              ¶¶¶     ¶¶¶          OOO     OOO        OOO     OOO    ')

#             elif dig_up == 'вернуться назад':
#                 all(tunnel_ticket, maze_ticket, pickaxe, gold)


#             else:
#                 print('Увы! Такого выбора нет!')
#                 print(' ')
#     else:
#         print('Увы! Такого выбора нет!')
#         print(' ')

# elif answer1 == 'лабиринт':
#     if maze_ticket == True:
#         return_maze = 'Вы вернулись в лабиринт, ничего не изменилось'
#         for char in return_maze: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         return_maze1 = 'Вернуться' + Fore.BLUE + ' назад ' + Fore.RESET + 'или ' + Fore.BLUE + 'рассмотреть кости? ' + Fore.RESET
#         answer7 = input(return_maze1)
#         for char in answer7: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')


#         if answer7 == 'рассмотреть кости':
#             correction_bone = 'Вы начали рассматривать кости, и вдруг поняли, что одна из костей похожа на ключ!'
#             for char in correction_bone: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             correction_bone1 = 'Вероятно этот ключ от двери что находится за золотом!'
#             for char in correction_bone1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             print(' ')
#             print('      ______')
#             print("   ,-' ;  ! `-.")
#             print('  / :  !  :  . \ ')
#             print(' |_ ;   __:  ;  |')
#             print(' )| .  :)(.  !  |')
#             print(' |"    (##)  _  |')
#             print(" |  :  ;`'  (_) ( ")
#             print(' |  :  :  .     |')
#             print(' )_ !  ,  ;  ;  |')
#             print(' || .  .  :  :  |')
#             print(' |" .  |  :  .  |')
#             print(' |==--_;----.___|')
#             print(' ')

#             correction_bone2 = Fore.BLUE + 'Открыть дверь' + Fore.RESET + ' или ' + Fore.BLUE + 'вернуться назад? ' + Fore.RESET
#             answer8 = input(correction_bone2)
#             for char in answer8: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             if answer8 == 'открыть дверь':
#                 correction_bone3 = 'Полные счастья и усталости вы открыли дверь'
#                 for char in correction_bone3: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 correction_bone4 = 'Выйдя в дверь вы оказались в замке полном стражей'
#                 for char in correction_bone4: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 correction_bone5 = 'Пока сражи не заметили вас'
#                 for char in correction_bone5: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 correction_bone5_add = 'Вы блуждаете по замку, как вдруг вас замечает один из стражников'
#                 for char in correction_bone5_add: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 correction_bone6 = 'В панике вы начали бежать, нужно быстрее что то сделать' + Fore.BLUE + ' залезть в шкаф ' + Fore.RESET + 'или' + Fore.BLUE + ' под ковер? ' + Fore.RESET
#                 wardrobe_or_carpet =  input(correction_bone6)
#                 for char in wardrobe_or_carpet: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 if wardrobe_or_carpet == 'залезть в шкаф':
#                     correction_wardrobe = 'Вы в панике запрыгнули в шкаф'
#                     for char in correction_wardrobe: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     correction_wardrobe1 = 'Стражник пробежал мимо вас'
#                     for char in correction_wardrobe1: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     correction_wardrobe2 = 'Выйти из шкафа? ' + Fore.BLUE + 'да/нет '+ Fore.RESET
#                     answer_wardrobe = input(correction_wardrobe2)
#                     for char in answer_wardrobe: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     if answer_wardrobe == 'да':
#                         correction_warbone3 = 'Вы вышли из шкафа'
#                         for char in correction_warbone3: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                         print('')

#                         correction_wardrobe4 = 'Вы быстро осмотрелись'
#                         for char in correction_wardrobe4: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                         print('')

#                         correction_wardrobe5 = 'Срези множества комнат и дорогих вещей вы заметили сранную дверь с нарисованой короной в цепях'
#                         for char in correction_wardrobe5: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                         print('')

#                         correction_wardrobe6 = Fore.BLUE + 'Пойти дальше' + Fore.RESET + ' или ' + Fore.BLUE + 'зайти в комнату? '+ Fore.RESET 
#                         answer_tower = input(correction_wardrobe6)
#                         for char in answer_tower: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                         print('')

#                         if answer_tower == 'зайти в комнату':
#                             correction_wardrobe7 = 'Вы зашли в дверь, на удивление она не была заперта'
#                             for char in correction_wardrobe7: 
#                                     print(char, end='', flush=True) 
#                                     time.sleep(0.05)
#                             print('')

#                             correction_wardrobe8 = 'Вы начали осматриваться'
#                             for char in correction_wardrobe8: 
#                                     print(char, end='', flush=True) 
#                                     time.sleep(0.05)
#                             print('')

#                             correction_wardrobe9 = 'Перед вами высокая лестника ведущая вверх'
#                             for char in correction_wardrobe9: 
#                                     print(char, end='', flush=True) 
#                                     time.sleep(0.05)
#                             print('')

#                             correction_ladder = 'Подняться по лестнице? ' + Fore.BLUE + 'да\нет ' + Fore.RESET
#                             answer_ladder = input(correction_ladder)
#                             for char in answer_ladder: 
#                                     print(char, end='', flush=True) 
#                                     time.sleep(0.05)
#                             print('')

#                             if answer_ladder == 'да':
#                                 correction_ladder1 = 'Вы начали подниматься по лестнице, как вдруг заметили охранника у двери'
#                                 for char in correction_ladder1: 
#                                         print(char, end='', flush=True) 
#                                         time.sleep(0.05)
#                                 print('')

#                                 if gold == True:
#                                     gold_true = Fore.BLUE + 'Подкупить стража' + Fore.RESET + ' или ' + Fore.BLUE + 'напасть? ' + Fore.RESET
#                                     answer_gold_true = input(gold_true)
#                                     for char in answer_gold_true: 
#                                         print(char, end='', flush=True) 
#                                         time.sleep(0.05)
#                                     print('')

#                                     if answer_gold_true == 'подкупить стража':
#                                         answer_bribe = 'Скупой страж сразу согласился, но предявил свое условие!'
#                                         for char in answer_bribe: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe1 = 'Условие: когда ты войдешь за это дверь у тебя будеть ровно 5 минут, чтобы забрать принцессу'
#                                         for char in answer_bribe1: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe2 = 'По истечении времени я зайду в комнату и если ты все еще там будешь, я тебя посажу в тюрьму!'
#                                         for char in answer_bribe2: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe3 = 'Вы нехотя согласились'
#                                         for char in answer_bribe3: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe4 = 'Вы вошли в дверь, на кровате сидела заплаканная принцесса'
#                                         for char in answer_bribe4: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe5 = 'У вас нет времени обьяснять! Но попытались'
#                                         for char in answer_bribe5: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe6 = 'Принцесса обрадовалась!'
#                                         for char in answer_bribe6: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_bribe7 = 'По вышему быстро выдуманному плану вы должны вырубить стражу вы выбежать из замка'
#                                         for char in answer_bribe7: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_brieb8 = 'В качестве оружия что вы выбирете ' + Fore.BLUE +  'плюшевую пони ' + Fore.RESET + 'или ' + Fore.BLUE + 'сковороду? ' + Fore.RESET
#                                         answer_weapon = input(answer_brieb8)
#                                         for char in answer_weapon: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         if answer_weapon == 'плюшевую пони':
#                                             weapon = 'Вы сделали довольно странный выбор'
#                                             for char in weapon: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             weapon1 = 'Вы прижались к стене, вдруг открылась дверь, в нее забежал стражник'
#                                             for char in weapon1: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             weapon2 = 'Как только вы увидели его сразу ударили мягкой игрушкой'
#                                             for char in weapon2: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             weapon3 = 'Обескураженный страж свалился на пол'
#                                             for char in weapon3: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le = 'Вы не расстерялись и сразу выбежали с принцессой из башни!'
#                                             for char in continued_le: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le1 = 'Вы не знаете куда бежать, так что вы полностью решили положиться на принцессу'
#                                             for char in continued_le1: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le2 = 'Бегаю по замку вы собрали за собой хвост из стражей'
#                                             for char in continued_le2: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le3 = 'Принцесса приводит вас в в книжный зал невероятных размеров'
#                                             for char in continued_le3: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le4 = 'Там вы смогли скрыться от стражей'
#                                             for char in continued_le4: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le5 = 'Вы замечаюте довольно странную книгу, обвешенную кристаллами и странными надписями'
#                                             for char in continued_le5: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le6 = 'Дервнув за эту книгу, чтена начала двигаться'
#                                             for char in continued_le6: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             continued_le7 = 'Эта книга привела вас на улицу города!'
#                                             for char in continued_le7: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             final = 'Вы смогли сбежать с принцессой!'
#                                             for char in final: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             final1 = 'Но вы еще в розыске!'
#                                             for char in final1: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             print('       _      _                   ')
#                                             print('      (_)    | |                  ')
#                                             print('__   ___  ___| |_ ___  _ __ _   _ ')
#                                             print("\ \ / / |/ __| __/ _ \| '__| | | |")
#                                             print(' \ V /| | (__| || (_) | |  | |_| |')
#                                             print('  \_/ |_|\___|\__\___/|_|   \__, |')
#                                             print('                             __/ |')
#                                             print('                            |___/ ')

#                                             result = 'Ваш результат: 2 из 3 звезд!'
#                                             for char in result: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             print('                   ¶                    ¶                  .         ')
#                                             print('                  ¶¶¶                  ¶¶¶                ,O,        ')
#                                             print('	         ¶¶¶¶¶      	      ¶¶¶¶¶              ,O O,       ')
#                                             print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  "oooooO   Oooooo" ')
#                                             print('              ¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶       `O          O`  ')
#                                             print('	        ¶¶¶¶¶¶¶              ¶¶¶¶¶¶¶            `O     O`     ')
#                                             print('               ¶¶¶¶_¶¶¶¶            ¶¶¶¶_¶¶¶¶          O  O"O  O     ')
#                                             print('              ¶¶¶     ¶¶¶          ¶¶¶     ¶¶¶        OOO     OOO    ')

#                                         elif answer_weapon == 'сковороду':
#                                             frying_pan = 'Довольно смелый выбор!'
#                                                         for char in frying_pan: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         for char in weapon1: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         frying_pan = 'Вы со всей силы бьете стража, но он будто и не чувствуя, нападает на вас!'
#                                                         for char in frying_pan: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         for char in game_over: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                     else:
#                                                         print('Увы! Такого выбора нет!')
#                                                         print(' ')

#                                                 elif answer_gold_true == 'напасть':
#                                                     attack = 'Вы решились напасть на стража'
#                                                     for char in attack: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     attack1 = 'Но страж оказался не из слабых!'
#                                                     for char in attack1: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     attack2 = 'На вашу драку прибежало еще 3 стража и вас схватили!'
#                                                     for char in attack2: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     for char in game_over: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                 else:
#                                                     print('Увы! Такого выбора нет!')
#                                                     print(' ')

#                                             elif gold == False:
#                                                 gold_false = 'У вас не осталось выбора придется нападать!'
#                                                 for char in gold_false: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 attack = 'Вы решились напасть на стража'
#                                                 for char in attack: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 attack1 = 'Но страж оказался не из слабых!'
#                                                 for char in attack1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 attack2 = 'На вашу драку прибежало еще 3 стража и вас схватили!'
#                                                 for char in attack2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 for char in game_over: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                         elif answer_ladder == 'нет':
#                                             think = 'Вы немного подумали и поняли что другого выбора нет, придется подниматься'
#                                             for char in think: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                             print('')

#                                             correction_ladder1 = 'Вы начали подниматься по лестнице, как вдруг заметили охранника у двери'
#                                             for char in correction_ladder1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                             print('')

#                                             if gold == True:
#                                                 gold_true = Fore.BLUE + 'Подкупить стража' + Fore.RESET + ' или ' + Fore.BLUE + 'напасть? ' + Fore.RESET
#                                                 answer_gold_true = input(gold_true)
#                                                 for char in answer_gold_true: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')


#                                                 if answer_gold_true == 'подкупить стража':
#                                                     answer_bribe = 'Скупой страж сразу согласился, но предявил свое условие!'
#                                                     for char in answer_bribe: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe1 = 'Условие: когда ты войдешь за это дверь у тебя будеть ровно 5 минут, чтобы забрать принцессу'
#                                                     for char in answer_bribe1: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe2 = 'По истечении времени я зайду в комнату и если ты все еще там будешь, я тебя посажу в тюрьму!'
#                                                     for char in answer_bribe2: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe3 = 'Вы нехотя согласились'
#                                                     for char in answer_bribe3: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe4 = 'Вы вошли в дверь, на кровате сидела заплаканная принцесса'
#                                                     for char in answer_bribe4: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe5 = 'У вас нет времени обьяснять! Но попытались'
#                                                     for char in answer_bribe5: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe6 = 'Принцесса обрадовалась!'
#                                                     for char in answer_bribe6: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_bribe7 = 'По вышему быстро выдуманному плану вы должны вырубить стражу вы выбежать из замка'
#                                                     for char in answer_bribe7: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     answer_brieb8 = 'В качестве оружия что вы выбирете ' + Fore.BLUE +  'плюшевую пони ' + Fore.RESET + 'или ' + Fore.BLUE + 'сковороду? ' + Fore.RESET
#                                                     answer_weapon = input(answer_brieb8)
#                                                     for char in answer_weapon: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     if answer_weapon == 'плюшевую пони':
#                                                         weapon = 'Вы сделали довольно странный выбор'
#                                                         for char in weapon: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         weapon1 = 'Вы прижались к стене, вдруг открылась дверь, в нее забежал стражник'
#                                                         for char in weapon1: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         weapon2 = 'Как только вы увидели его сразу ударили мягкой игрушкой'
#                                                         for char in weapon2: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         weapon3 = 'Обескураженный страж свалился на пол'
#                                                         for char in weapon3: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le = 'Вы не расстерялись и сразу выбежали с принцессой из башни!'
#                                                         for char in continued_le: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le1 = 'Вы не знаете куда бежать, так что вы полностью решили положиться на принцессу'
#                                                         for char in continued_le1: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le2 = 'Бегаю по замку вы собрали за собой хвост из стражей'
#                                                         for char in continued_le2: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le3 = 'Принцесса приводит вас в в книжный зал невероятных размеров'
#                                                         for char in continued_le3: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le4 = 'Там вы смогли скрыться от стражей'
#                                                         for char in continued_le4: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le5 = 'Вы замечаюте довольно странную книгу, обвешенную кристаллами и странными надписями'
#                                                         for char in continued_le5: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le6 = 'Дервнув за эту книгу, чтена начала двигаться'
#                                                         for char in continued_le6: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         continued_le7 = 'Эта книга привела вас на улицу города!'
#                                                         for char in continued_le7: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         final = 'Вы смогли сбежать с принцессой!'
#                                                         for char in final: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         final1 = 'Но вы еще в розыске!'
#                                                         for char in final1: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         print('       _      _                   ')
#                                                         print('      (_)    | |                  ')
#                                                         print('__   ___  ___| |_ ___  _ __ _   _ ')
#                                                         print("\ \ / / |/ __| __/ _ \| '__| | | |")
#                                                         print(' \ V /| | (__| || (_) | |  | |_| |')
#                                                         print('  \_/ |_|\___|\__\___/|_|   \__, |')
#                                                         print('                             __/ |')
#                                                         print('                            |___/ ')

#                                                         result = 'Ваш результат: 2 из 3 звезд!'
#                                                         for char in result: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         print('                   ¶                    ¶                  .         ')
#                                                         print('                  ¶¶¶                  ¶¶¶                ,O,        ')
#                                                         print('	         ¶¶¶¶¶      	      ¶¶¶¶¶              ,O O,       ')
#                                                         print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  "oooooO   Oooooo" ')
#                                                         print('              ¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶       `O          O`  ')
#                                                         print('	        ¶¶¶¶¶¶¶              ¶¶¶¶¶¶¶            `O     O`     ')
#                                                         print('               ¶¶¶¶_¶¶¶¶            ¶¶¶¶_¶¶¶¶          O  O"O  O     ')
#                                                         print('              ¶¶¶     ¶¶¶          ¶¶¶     ¶¶¶        OOO     OOO    ')


#                                                     elif answer_weapon == 'сковороду':
#                                                         frying_pan = 'Довольно смелый выбор!'
#                                                         for char in frying_pan: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         for char in weapon1: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         frying_pan = 'Вы со всей силы бьете стража, но он будто и не чувствуя, нападает на вас!'
#                                                         for char in frying_pan: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')

#                                                         for char in game_over: 
#                                                             print(char, end='', flush=True) 
#                                                             time.sleep(0.05)
#                                                         print('')


#                                                     else:
#                                                         print('Увы! Такого выбора нет!')
#                                                         print(' ')

#                                                 elif answer_gold_true == 'напасть':
#                                                     attack = 'Вы решились напасть на стража'
#                                                     for char in attack: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     attack1 = 'Но страж оказался не из слабых!'
#                                                     for char in attack1: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     attack2 = 'На вашу драку прибежало еще 3 стража и вас схватили!'
#                                                     for char in attack2: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     for char in game_over: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')


#                                                 else:
#                                                     print('Увы! Такого выбора нет!')
#                                                     print(' ')

#                                             elif gold == False:
#                                                 gold_false = 'У вас не осталось выбора придется нападать!'
#                                                 for char in gold_false: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 for char in attack: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 for char in attack1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 for char in attack2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 for char in game_over: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')


#                                             else:
#                                                 print('Увы! Такого выбора нет!')
#                                                 print(' ')

#                                         else:
#                                             print('Увы! Такого выбора нет!')
#                                             print(' ')

#                                     elif answer_tower == 'пойти дальше':
#                                         farther = 'Вы блуждаете по большому замку, на удивление стражей нет'
#                                         for char in farther: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         farther1 = 'Спустя 10 минут блуждания по замку вы куда то забрели'
#                                         for char in farther1: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         farther2 = 'Вы немного осмотрелись, на ваш взгляд бросается строн'
#                                         for char in farther2: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         farther3 = 'На троне сидит король, а за ним армия стражей....'
#                                         for char in farther3: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         farther4 = 'Вам стало не хорошо, король тем временем идет в вашу сторону с мечом'
#                                         for char in farther4: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         farther5 = 'Подойдя к вам, он вам предложил 2 варианта исхода событий'
#                                         for char in farther5: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         event = '1 вариант: вы выходите на дуэль с королем. Победитель получает все! '
#                                         for char in event: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         event1 = '2 вариант: вы бежите из королевства и отныне вход во владения короля вам запрещен!'
#                                         for char in event1: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         answer_event_add = 'Что вы исход вы выберите ' + Fore.BLUE + '1' + Fore.RESET + ' или ' + Fore.BLUE + '2? ' + Fore.RESET
#                                         answer_event =  input(answer_event_add)
#                                         for char in answer_event: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                         print('')

#                                         if answer_event == '1':
#                                             king_fight = 'Вы готовитесь к дуэли'
#                                             for char in king_fight: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             king_fight1 = 'Из предложенных оружий есть: ' + Fore.BLUE + 'меч, лук, кинжал и секира' + Fore.RESET
#                                             for char in king_fight1: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             answer_fight = input('Что вы возьмете? ')
#                                             for char in answer_fight: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             if answer_fight == 'меч':
#                                                 sword = 'Вы сделали довольно классический выбор'
#                                                 for char in sword: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print('         />_________________________________ ')
#                                                 print('[########[]_________________________________>')
#                                                 print('         \>')

#                                                 sword_fight = 'Король с ухмылкой смотрит на вас'
#                                                 for char in sword_fight: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 timer = 'бой начинается на счет 3'
#                                                 for char in timer: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 time.sleep(1)
#                                                 print('1')
#                                                 time.sleep(1)
#                                                 print('2')
#                                                 time.sleep(1)
#                                                 print('3!')
#                                                 fight_start = 'Бой начинается'
#                                                 for char in fight_start: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight = 'Король сразу идет в атаку'
#                                                 for char in fight: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight1 = 'Вы сражаетесь уже полчаса '
#                                                 for char in fight1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight2 = 'Дуэль серьезно измотала вас и короля, все идет к тому, что будет ничья'
#                                                 for char in fight2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight3 = 'Вдруг выбегает принцесса, бой останавливается '
#                                                 for char in fight3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight4 = 'Король от изнеможения падает на пол, следом падаете и вы'
#                                                 for char in fight4: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end = 'Вы просыпаетесь в неизвестной комнате'
#                                                 for char in happy_end: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 time.sleep(1)
#                                                 happy_end1 = 'Вы решили пройтись по замку, хоть это было очень трудно'
#                                                 for char in happy_end1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end2= 'Немного продя, вы снова вернулись на место где была деэль'
#                                                 for char in happy_end2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end3 = 'Вас встретила стража'
#                                                 for char in happy_end3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 time.sleep(1)
#                                                 happy_end4 = 'Силой вас куда то повели'
#                                                 for char in happy_end4: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end5 = 'Стража привела вас к обессиленному королю, который лежал на кровати'
#                                                 for char in happy_end5: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end6 = 'Король рассказывает вам историю'
#                                                 for char in happy_end6: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 time.sleep(1)
#                                                 history = 'История: всех рыцарей, которые хотели получить серце моей дочери я проверял.'
#                                                 for char in history: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 history1 = 'Всех рыцарей сажали в подземелье, до тебя никто не смог выбраться из него.'
#                                                 for char in history1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 history2 = 'Многие просто умирали от монстра или сбегали с помощью кирки'
#                                                 for char in history2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 history3 = 'Я считаю тебя достойным, теперь ты можешь взять в жены мою дочь'
#                                                 for char in history3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win = 'Поздравляю вы победили, набрав максимальное колличество звезд вы большой молодец!'
#                                                 for char in win: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print(' ')
#                                                 print('                   ¶                    ¶                    ¶          ')
#                                                 print('                  ¶¶¶                  ¶¶¶                  ¶¶¶        ')
#                                                 print('	         ¶¶¶¶¶      	      ¶¶¶¶¶                ¶¶¶¶¶              ')
#                                                 print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
#                                                 print('              ¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶')
#                                                 print('	        ¶¶¶¶¶¶¶              ¶¶¶¶¶¶¶              ¶¶¶¶¶¶¶')
#                                                 print('               ¶¶¶¶_¶¶¶¶            ¶¶¶¶_¶¶¶¶            ¶¶¶¶_¶¶¶¶')
#                                                 print('              ¶¶¶     ¶¶¶          ¶¶¶     ¶¶¶          ¶¶¶     ¶¶¶')
#                                                 print(' ')

#                                                 win1 = 'Вы смогли выбрать правильный путь, хоть и некоторые выборы были довольно не понятны'
#                                                 for char in win1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win2 = 'В любом случае вы большой молодец! Из 11 возможных вариантов, в них входят 3 победных и 8 проигрышных!'
#                                                 for char in win2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win3 = 'Да, возможно игра плохо проработана и в ней много недостатков, но на ее создание я потратил очень много времени'
#                                                 for char in win3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win4 = 'Я старался сократить код как можно сильнее, ведь с таким кодом работать гораздо удобнее'
#                                                 for char in win4: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win5 = 'Сама игра переделовалась около 3 раз, но она так и осталась недоделанной'
#                                                 for char in win5: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win6 = 'P.S. на эту игру было потраченно колосальное колличество переменных весь список можно посмотреть в структуре'
#                                                 for char in win6: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')


#                                             elif answer_fight == 'лук':
#                                                 bow = 'В детстве вас учили стрелять, поэтому вы очень хорошо стреляете, а этот выбор возможно был очень хорошим'
#                                                 for char in bow: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print('          4$$-.')
#                                                 print('           4   ".')
#                                                 print('           4    ^. ')
#                                                 print('           4     $ ')
#                                                 print('           4      b ')
#                                                 print('           4      "b.')
#                                                 print('           4        $ ')
#                                                 print('           4        $r')
#                                                 print('           4        $F ')
#                                                 print('-$b========4========$b====*P=- ')
#                                                 print('           4       *$$F')
#                                                 print('           4        $$"')
#                                                 print('           4       .$F')
#                                                 print('           4       dP ')
#                                                 print('           4      F  ')
#                                                 print('           4     @ ')
#                                                 print('           4    . ')
#                                                 print('           J  . ')
#                                                 print('          $$')

#                                                 timer = 'бой начинается на счет 3'
#                                                 for char in timer: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')
#                                                 time.sleep(1)
#                                                 print('1')
#                                                 time.sleep(1)
#                                                 print('2')
#                                                 time.sleep(1)
#                                                 print('3!')

#                                                 fight_start = 'Бой начинается'
#                                                 for char in fight_start: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 bow_fight = 'Вы сражаетесь около 10 минут, король и вы очень устали'
#                                                 for char in bow_fight: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 bow_fight1 = 'Вдруг в какой то момент вы попадаете в короля, король падает на пол'
#                                                 for char in bow_fight1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 kill_or_not = Fore.BLUE + 'Убить' + Fore.RESET + ' или ' + Fore.BLUE + 'оставить в живых? ' + Fore.RESET 
#                                                 answer_kill_or_not = input(kill_or_not)
#                                                 for char in answer_kill_or_not: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 if answer_kill_or_not == 'убить':
#                                                     kill = 'Вы убили короля'
#                                                     for char in kill: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     print('           ______')
#                                                     print('        .-"      "-.')
#                                                     print('       /            \ ')
#                                                     print('      |              |')
#                                                     print('      |,  .-.  .-.  ,|')
#                                                     print('      | )(__/  \__)( |')
#                                                     print('      |/     /\     \|')
#                                                     print('      (_     ^^     _)')
#                                                     print('       \__|IIIIII|__/')
#                                                     print('        | \IIIIII/ |')
#                                                     print('        \          /')
#                                                     print('         `--------`')

#                                                     kill1 = 'Вы победили, но какой ценой... Принцесса теперь никогда вас не простит'
#                                                     for char in kill1: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     time.sleep(2)

#                                                     kill2 = 'Спустя 2 года правления вас свергли с трона'
#                                                     for char in kill2: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     time.sleep(1)

#                                                     print(' ')
#                                                     winner_or_looser = 'Победа?'
#                                                     for char in winner_or_looser: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     looser = 'Ваш результат 1 из 3 звезд'
#                                                     for char in looser: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     time.sleep(1)

#                                                     print('                   ¶                    .                  .         ')
#                                                     print('                  ¶¶¶                  ,O,                ,O,        ')
#                                                     print('	         ¶¶¶¶¶      	      ,O O,              ,O O,       ')
#                                                     print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    "oooooO   Oooooo"  "oooooO   Oooooo" ')
#                                                     print('              ¶¶¶¶¶¶¶¶¶¶¶         `O         O`      `O          O`  ')
#                                                     print('	        ¶¶¶¶¶¶¶             `O     O`          `O     O`     ')
#                                                     print('               ¶¶¶¶_¶¶¶¶            O  O"O  O          O  O"O  O     ')
#                                                     print('              ¶¶¶     ¶¶¶          OOO     OOO        OOO     OOO    ')

#                                                     hint = 'Подсказка: можно сделать выборы так, чтобы все остались живы...'
#                                                     for char in hint: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')


#                                                 elif answer_kill_or_not == 'оставить в живых':
#                                                     mercy = 'Вы благородно поступили'
#                                                     for char in mercy: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     time.sleep(1)

#                                                     hp_end = 'Силой стража вас куда то повела'
#                                                     for char in hp_end: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     happy_end5 = 'Стража привела вас к обессиленному королю, который лежал на кровати'
#                                                     for char in happy_end5: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     happy_end6 = 'Король рассказывает вам историю'
#                                                     for char in happy_end6: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     time.sleep(1)

#                                                     history = 'История: всех рыцарей, которые хотели получить серце моей дочери я проверял.'
#                                                     for char in history: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     history1 = 'Всех рыцарей сажали в подземелье, до тебя никто не смог выбраться из него.'
#                                                     for char in history1: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     history2 = 'Многие просто умирали от монстра или сбегали с помощью кирки'
#                                                     for char in history2: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     history3 = 'Я считаю тебя достойным, теперь ты можешь взять в жены мою дочь'
#                                                     for char in history3: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     time.sleep(1)

#                                                     history4 = 'Позже король умирает...'
#                                                     for char in history4: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')
#                                                     print(' ')

#                                                     result_king_dead = 'Вы прошли игру!'
#                                                     for char in result_king_dead: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')

#                                                     result_king_dead1 = 'Ваш результат: 2 из 3 звезд!'
#                                                     for char in result_king_dead1: 
#                                                         print(char, end='', flush=True) 
#                                                         time.sleep(0.05)
#                                                     print('')


#                                                 else:
#                                                     print('Увы! Такого выбора нет!')
#                                                     print(' ')

#                                             elif answer_fight == 'кинжал':
#                                                 bad_choice = 'Вы сделали очень плохой выбор'
#                                                 for char in bad_choice: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print(')xxxxx[;;;;;;;;;>')

#                                                 bad_choice1 = 'В ходе дуэли король вас ранил, вы упали без сознания'
#                                                 for char in bad_choice1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 bad_choice2 = 'Вы проснулись в кровати'
#                                                 # for char in bad_choice2: 
#                                                 #     print(char, end='', flush=True) 
#                                                 #     time.sleep(0.05)
#                                                 # print('')

#                                                 # bad_choice3 = 'Король оставил вас в живых, но отныне вам запрещено даже смотреть на принцессу'
#                                                 # for char in bad_choice3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')
#                                                 time.sleep(1)
#                                                 print(' ')

#                                                 bad_choice4 = 'Ваш результат: 1 из 3 звезд'
#                                                 for char in bad_choice4: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print(' ')
#                                                 print('                   ¶                    .                  .         ')
#                                                 print('                  ¶¶¶                  ,O,                ,O,        ')
#                                                 print('	         ¶¶¶¶¶      	      ,O O,              ,O O,       ')
#                                                 print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    "oooooO   Oooooo"  "oooooO   Oooooo" ')
#                                                 print('              ¶¶¶¶¶¶¶¶¶¶¶         `O         O`      `O          O`  ')
#                                                 print('	        ¶¶¶¶¶¶¶             `O     O`          `O     O`     ')
#                                                 print('               ¶¶¶¶_¶¶¶¶            O  O"O  O          O  O"O  O     ')
#                                                 print('              ¶¶¶     ¶¶¶          OOO     OOO        OOO     OOO    ')
#                                                 print(' ')

#                                             elif answer_fight == 'секира':
#                                                 axe = 'Вы сделали довольно необычный выбор, но в юношостве вы хорошо орудовали топором'
#                                                 for char in axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print(' ')
#                                                 print('   ,  /\  .')
#                                                 print(" / / -||-'\ \ ")
#                                                 print('( | -=||=- | )')
#                                                 print(' \ \,-||-./ /')
#                                                 print("   `  ||   '")
#                                                 print('      ||')
#                                                 print('      ||')
#                                                 print('      ||')
#                                                 print('      ||')
#                                                 print('      ||')
#                                                 print('      ()')
#                                                 print(' ')

#                                                 axe_fight = 'Король с ухмылкой смотрит на вас'
#                                                 for char in axe_fight: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 timer = 'бой начинается на счет 3'
#                                                 time.sleep(1)
#                                                 print('1')
#                                                 time.sleep(1)
#                                                 print('2')
#                                                 time.sleep(1)
#                                                 print('3!')
#                                                 fight_start_axe = 'Бой начинается'
#                                                 for char in fight_start_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight_axe = 'Король сразу идет в атаку'
#                                                 for char in fight_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight1_axe = 'Вы сражаетесь уже полчаса '
#                                                 for char in fight1_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight2_axe = 'Дуэль серьезно измотала вас и короля, все идет к тому, что будет ничья'
#                                                 for char in fight2_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight3_axe = 'Вдруг выбегает принцесса, бой останавливается '
#                                                 for char in fight3_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 fight4_axe = 'Король от изнеможения падает на пол, следом падаете и вы'
#                                                 for char in fight4_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end_axe = 'Вы просыпаетесь в неизвестной комнате'
#                                                 for char in happy_end_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')
#                                                 time.sleep(1)

#                                                 happy_end1_axe = 'Вы пройтись по замку, хоть это было очень трудно'
#                                                 for char in happy_end1_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end2_axe = 'Немного продя, вы снова вернулись на место где была деэль'
#                                                 for char in happy_end2_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end3_axe = 'Вас встретила стража'
#                                                 for char in happy_end3_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')
#                                                 time.sleep(1)

#                                                 happy_end4_axe = 'Силой вас куда то повели'
#                                                 for char in happy_end4_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end5_axe = 'Стража привела вас к обессиленному королю, который лежал на кровати'
#                                                 for char in happy_end5_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 happy_end6_axe = 'Король рассказывает вам историю'
#                                                 for char in happy_end6_axe: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')
#                                                 time.sleep(1)

#                                                 history = 'История: всех рыцарей, которые хотели получить серце моей дочери я проверял.'
#                                                 for char in history: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 history1 = 'Всех рыцарей сажали в подземелье, до тебя никто не смог выбраться из него.'
#                                                 for char in history1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 history2 = 'Многие просто умирали от монстра или сбегали с помощью кирки'
#                                                 for char in history2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 history3 = 'Я считаю тебя достойным, теперь ты можешь взять в жены мою дочь'
#                                                 for char in history3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win = 'Поздравляю вы победили, набрав максимальное колличество звезд вы большой молодец!'
#                                                 for char in win: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 print(' ')
#                                                 print('                   ¶                    ¶                    ¶          ')
#                                                 print('                  ¶¶¶                  ¶¶¶                  ¶¶¶        ')
#                                                 print('	         ¶¶¶¶¶      	      ¶¶¶¶¶                ¶¶¶¶¶              ')
#                                                 print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
#                                                 print('              ¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶')
#                                                 print('	        ¶¶¶¶¶¶¶              ¶¶¶¶¶¶¶              ¶¶¶¶¶¶¶')
#                                                 print('               ¶¶¶¶_¶¶¶¶            ¶¶¶¶_¶¶¶¶            ¶¶¶¶_¶¶¶¶')
#                                                 print('              ¶¶¶     ¶¶¶          ¶¶¶     ¶¶¶          ¶¶¶     ¶¶¶')
#                                                 print(' ')

#                                                 win1 = 'Вы смогли выбрать правильный путь, хоть и некоторые выборы были довольно не понятны'
#                                                 for char in win1: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')


#                                                 win2 = 'В любом случае вы большой молодец! Из 11 возможных вариантов, в них входят 3 победных и 8 проигрышных!'
#                                                 for char in win2: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win3 = 'Да, возможно игра плохо проработана и в ней много недостатков, но на ее создание я потратил очень много времени'
#                                                 for char in win3: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win4 = 'Я старался сократить код как можно сильнее, ведь с таким кодом работать гораздо удобнее'
#                                                 for char in win4: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win5 = 'Сама игра переделовалась около 3 раз, но она так и осталась недоделанной'
#                                                 for char in win5: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')

#                                                 win6 = 'P.S. на эту игру было потраченно колосальное колличество переменныхЮ весь список можно посмотреть в структуре'
#                                                 for char in win6: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                                 print('')


#                                             else:
#                                                 print('Увы! Такого оружия нет!')
#                                                 print('  ')


#                                         elif answer_event == '2':
#                                             bad_end = 'Вы сделали плохой выбор, вас выгнали из королевства'
#                                             for char in bad_end: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                             print('')

#                                             bad_end = 'Теперь вы носите статус труса'
#                                             for char in bad_end: 
#                                                     print(char, end='', flush=True) 
#                                                     time.sleep(0.05)
#                                             print('')
#                                             time.sleep(1)
#                                             print(' ')

#                                             bad_choice4 = 'Ваш результат: 1 из 3 звезд'
#                                             for char in bad_end: 
#                                                 print(char, end='', flush=True) 
#                                                 time.sleep(0.05)
#                                             print('')

#                                             print(' ')
#                                             print('                   ¶                    .                  .         ')
#                                             print('                  ¶¶¶                  ,O,                ,O,        ')
#                                             print('	         ¶¶¶¶¶      	      ,O O,              ,O O,       ')
#                                             print('           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    "oooooO   Oooooo"  "oooooO   Oooooo" ')
#                                             print('              ¶¶¶¶¶¶¶¶¶¶¶         `O         O`      `O          O`  ')
#                                             print('	        ¶¶¶¶¶¶¶             `O     O`          `O     O`     ')
#                                             print('               ¶¶¶¶_¶¶¶¶            O  O"O  O          O  O"O  O     ')
#                                             print('              ¶¶¶     ¶¶¶          OOO     OOO        OOO     OOO    ')
#                                             print(' ')

#                                         else:
#                                             print('Увы! Такого выбора нет!')
#                                             print(' ')

#                                     else:
#                                         print('Увы! Такого выбора нет!')
#                                         print(' ')

#                                 elif answer_wardrobe == 'нет':
#                                     sitting_in_the_closet = 'Вы так долго сидели в шкафу, что один из подданых короля открыл шкаф'
#                                     for char in sitting_in_the_closet: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                     print('')
#                                     sitting_in_the_closet1 = 'Вас поймали!'
#                                     for char in sitting_in_the_closet1: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                     print('')

#                                     for char in game_over: 
#                                             print(char, end='', flush=True) 
#                                             time.sleep(0.05)
#                                     print('')


#                                 else:
#                                     print('Увы! Такого выбора нет!')
#                                     print(' ')

#                             elif wardrobe_or_carpet == 'под ковер': 
#                                 funny_carpet = 'Возможно вы сделали очень поспешное решение'
#                                 for char in funny_carpet: 
#                                         print(char, end='', flush=True) 
#                                         time.sleep(0.05)
#                                 print('')

#                                 funny_carpet1 = 'Страж при виде того, как вы пытаетесь залезть под ковер, упал со смеху'
#                                 for char in funny_carpet1: 
#                                         print(char, end='', flush=True) 
#                                         time.sleep(0.05)
#                                 print('')

#                                 funny_carpet2 = 'После того как страж успокоился, он начал выс вытаскивать из под ковра'
#                                 for char in funny_carpet2: 
#                                         print(char, end='', flush=True) 
#                                         time.sleep(0.05)
#                                 print('')

#                                 for char in game_over: 
#                                         print(char, end='', flush=True) 
#                                         time.sleep(0.05)
#                                 print('')


#                             else:
#                                 print('Увы! Такого выбора нет!')
#                                 print(' ')

#                         elif answer8 == 'вернуться назад':
#                             all(tunnel_ticket, maze_ticket, pickaxe, gold)


#                         else:
#                             print('Увы! Такого выбора нет!')
#                             print(' ')

#                 elif maze_ticket == False:
#                     correction5 = 'Вы уже час блуждаете по лабиринту'
#                     for char in correction5: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                     print('')

#                     correction6 = 'Но в какой то момент вы встречаете выход'
#                     for char in correction6: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                     print('')

#                     correction7 = 'Немного пройдя дальше, вы замечаете, что у входа спит громандных размеров летучая мышь!'
#                     for char in correction7: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                     print('')

#                     correction8 = 'Под ней вы заметили гору золота и костей'
#                     for char in correction8: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     correction9 = 'Посмотрев на пол, ты понимаешь, что он весь усыпан мелкими костями'
#                     for char in correction9: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                     print('')

#                     correction10_addition = 'И снова перед вами выбор, но теперь этот выбор решает '
#                     correction10_addition1 = Back.LIGHTBLACK_EX + 'все' + Back.RESET
#                     correction10 = correction10_addition + correction10_addition1
#                     for char in correction10: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                     print('')

#                     answer4_extension = Fore.BLUE + 'Сразиться ' + Fore.RESET + 'или попытаться ' + Fore.BLUE + 'пройти мимо' + '? ' + Fore.RESET
#                     answer4 = input(answer4_extension)
#                     for char in answer4: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                     print('')

#                     if answer4 == 'сразиться':
#                         correction11 = 'Вы выбрали сразиться с монтстром'
#                         for char in correction11: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction12 = 'Вы начинаете подходить к монстру, и вдруг он просыпается'
#                         for char in correction12: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction13 = 'Но вы не медлите и сразу нападаете на него!'
#                         for char in correction13: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction14 = 'Спустя час истощающей битвы вы остаетесь победителем'
#                         for char in correction14: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction15 = 'И как победителю вам достается гора золота, кирка, и в подарок гора костей'
#                         for char in correction15: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction16 = 'Немного передохнув, вы замечаете что за горой золота находится дверь, но к сожалению, она на замке'
#                         for char in correction16: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction17 = 'Перекусив едой вы вернули себе силы'
#                         for char in correction17: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         correction18 = 'Осталось только выбрать что взять с собой'
#                         for char in correction18: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         answer5_extension = Fore.BLUE + 'Кирку' + Fore.RESET + ' или ' + Fore.BLUE + 'золото? ' + Fore.RESET
#                         answer5 = input(answer5_extension)
#                         for char in answer5: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         if answer5 == 'кирку':
#                             print(' ')
#                             print('⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀')
#                             print('⠀⠀⠀⠀⠀⠀⢀⣀⡿⠿⠿⠿⠿⠿⠿⢿⣀⣀⣀⣀⣀⡀')
#                             print('⠀⠀⠀⠀⠀⠀⠸⠿⣇⣀⣀⣀⣀⣀⣀⣸⠿⢿⣿⣿⣿⡇⠀')
#                             print('⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠿⠿⠿⠿⣿⣿⣀⡸⠿⢿⣿⡇⠀⠀')
#                             print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣧⣤⡼⠿⢧⣤⡀')
#                             print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣿⠛⢻⣿⡇⠀⢸⣿⡇')
#                             print('⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿⣿⣿⣿⠛⠛⠀⢸⣿⡇⠀⢸⣿⡇')
#                             print('⠀⠀⠀⠀⠀⠀⢠⣤⣿⣿⣿⣿⠛⠛⠀⠀⠀⢸⣿⡇⠀⢸⣿⡇')
#                             print('⠀⠀⠀⠀⢰⣶⣾⣿⣿⣿⠛⠛⠀⠀⠀⠀⠀⠈⠛⢳⣶⡞⠛⠁')
#                             print('⠀⠀⢰⣶⣾⣿⣿⣿⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀')
#                             print('⢰⣶⡎⠉⢹⣿⡏⠉⠁')
#                             print('⢸⣿⣷⣶⡎⠉⠁')
#                             print('⠀⠉⠉⠉⠁⠀')
#                             print(' ')

#                             pickaxe = not pickaxe
#                             correction19 = 'Осталось понять где можно использовать кирку'
#                             for char in correction19: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                             print('')

#                             answer6_extension = Fore.BLUE + 'Вернуться назад' + Fore.RESET + ' или ' + Fore.BLUE + 'сдаться' + Fore.RESET + '? '
#                             answer6 = input(answer6_extension)
#                             for char in answer6: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                             print('')

#                             if answer6 == 'вернуться назад':
#                                 maze_ticket = not maze_ticket
#                                 all(tunnel_ticket, maze_ticket, pickaxe, gold)

#                             elif answer6 == 'сдаться':
#                                 for char in game_over: 
#                                     print(char, end='', flush=True) 
#                                     time.sleep(0.05)
#                                 print('')
#                                 print('Ваш результат: 0 из 3 звезд')

#                             else:
#                                 print('Увы! Такого выбора нет!')

#                         elif answer5 == 'золото':
#                             correction20 = 'Вы взяли золото'
#                             gold = not gold
#                             for char in correction20: 
#                                 print(char, end='', flush=True) 
#                                 time.sleep(0.05)
#                             print('')

#                             print(' ')
#                             print('                                  ████   ')
#                             print('                            ██████    ██')
#                             print('                      ██████            ██ ')
#                             print('                ██████                    ██ ')
#                             print('              ██░░                  ▒▒▒▒▒▒▒▒██ ')
#                             print('              ██  ░░          ▒▒▒▒▒▒        ██ ')
#                             print('              ██    ░░  ▒▒▒▒▒▒          ▒▒▒▒██ ')
#                             print('              ██      ░░          ▒▒▒▒▒▒▒▒▒▒██ ')
#                             print('              ██▒▒▒▒  ░░    ▒▒▒▒▒▒▒▒▒▒██████  ')
#                             print('                ██▒▒░░░░▒▒▒▒▒▒▒▒██████        ')
#                             print('                  ██▒▒░░▒▒██████              ')
#                             print('                    ██████          ')
#                             print(' ')

#                             answer6_extension = Fore.BLUE + 'Вернуться назад' + Fore.RESET + ' или ' + Fore.BLUE + 'сдаться' + Fore.RESET + '? '
#                             answer6 = input(answer6_extension)

#                             if answer6 == 'вернуться назад':
#                                 maze_ticket = not maze_ticket
#                                 all(tunnel_ticket, maze_ticket, pickaxe, gold)

#                             elif answer6 == 'сдаться':
#                                 for char in game_over: 
#                                     print(char, end='', flush=True) 
#                                     time.sleep(0.05)
#                                 print('')
#                                 print('Ваш результат: 0 из 3 звезд!')

#                             else:
#                                 print('Увы! Такого выбора нет!')
#                                 print(' ')

#                         else:
#                             print('Увы! Такого выбора нет!')
#                             print(' ')

#                     elif answer4 == 'пройти мимо':
#                         die = 'Вы пытаетесь пройти мимо, кости так и хрустят, выдавая вас'
#                         for char in die: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         die2 = 'Вдруг вы наступили на кость, которая хрустнула очень громко!'
#                         for char in die2: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         die3 = 'Монстр тут же проснулся и на пал на вас, вы не ожидали, что он нападет!'
#                         for char in die3: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         for char in game_over: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                     else:
#                         print('Увы! Такого выбора нет!')
#                         print(' ')

#             else:
#                 print('Увы! Такого выбора нет!')
#                 print(' ')
#                 all(tunnel_ticket, maze_ticket, pickaxe, gold)           

#         all(tunnel_ticket, maze_ticket, pickaxe, gold)
#     text_game()
#     back_t = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'сыграем еще раз?' + Fore.RESET)
#     if back_t == 'Вернемся назад' or back_t == 'вернемся назад' or back_t == 'назад' or back_t == 'Назад':
#         l_func()
#         os.system('cls')

#     elif back_t == 'Сыграем еще раз' or back_t == 'сыграем еще раз' or back_t == 'еще раз' or back_t == 'Еще раз' or back_t == 'еще' or back_t == 'Еще':
#         text_game()
#         os.system('cls')

# elif game_selection == 'квиз' or game_selection == 'Квиз':
#     def kviz():
#         counter = 0.0
#         name = input('Как вас зовут? ')
#         age = int(input('Сколько вам лет? '))

#         print('Привет, ' + name + '!')
#         preference = input('Что вы любите: играть в майнкрафт, играть в террарию, читать книги, кодить? ')
#         if preference == 'кодить':
#             print('В данном квизе будут вопросы по python ')
#             question1 = input('Вопрос 1: как называется тип переменной, которая принимает только целые числа? ')
#             if question1 == 'int' or question1 == 'инт' or question1 == 'интеджер' or question1 == 'integer':
#                 print('Молодец!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             question2 = input('Вопрос 2: как называется тип переменной, которая принимает значение True/False? ')
#             if question2 == 'boolean' or question2 == 'bool' or question2 == 'бул' or question2 == 'булеан':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             question3 = input('Что делает функция print()? ')
#             if question3 == 'вывод данных' or question3 == 'выводит данные' or question3 == 'выводит написанные данные':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             question4 = input('Что делает функция input()? ')
#             if question4 == 'запрос на ввод' or question4 == 'запрашивает ввод':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно!')

#             question5 = input('Как переводиться оператор условия or? ')
#             if question5 == 'или':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             print('Вы набрали ', counter, ' баллов из 5!')

#             if counter == 5:
#                 print('Молодец!')

#         elif preference == 'играть в майнкрафт' or preference == 'Играть в майнкрафт':
#             print('В данном квизе будут вопросы по майкрафту')
#             game_q = input('Из скольки слитков железа крафтится железный голем?')
#             if game_q == '36':
#                 print('Молодец!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q1 = input('Из чего крафтится железная кирка?')
#             if game_q1 == 'из 3 железа и 2 палок' or game_q1 == '3 железа и 2 палки ':
#                 print('Совершенно верно!')
#                 counter += 1

#             elif game_q1 == '3 железо':
#                 print('Не совсем правильно')
#                 counter += 0.5

#             else:
#                 print('Не верно!')

#             print('Уровень hard!')
#             game_q2 = input('Сколько всего слотов в инвенторе? ')
#             if game_q2 == '37':
#                 print('Верно!')
#                 counter += 2

#             else:
#                 print('Не верно!')

#             game_q3 = input('Сколько нужно блоков, чтобы построить максимальный силы маяк?(4 слоя блока) ')
#             if game_q3 == '280':
#                 print('Верно!')
#                 counter += 2

#             else:
#                 print('Не верно')

#             game_q4 = input('Сколько нужно алмазов на сет альмазной брони? ')
#             if game_q4 == '24':
#                 print('Верно!')
#                 counter += 2

#             else:
#                 print('Не верно')

#             print('Вы прошли квиз!')
#             print('Вы набрали ', counter, ' баллов из 8!')

#         elif preference == 'играть в террарию' or preference == 'Играть в террарию':
#             print('В этом квизе я буду задавать вопросы по террарии')
#             game_q_t = input('Как зовут первого нпс? ')
#             if game_q_t == 'Гид' or game_q_t == 'гид':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t1 = input('Какая монета является самой ценной в игре? ')
#             if game_q_t1 == 'Платиновая' or game_q_t1 == 'платиновая':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t2 = input('Самый лучший меч в игре по урону в секунду? ')
#             if game_q_t2 == 'Зенит' or game_q_t2 == 'зенит':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t3 = input('колько всего форм у босса "Глаз-Ктулху"? ')
#             if game_q_t3 == '2':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t4 = input('Сколько всего небесных башен появляется в мире после убийства Лунатика-Культиста? ')        
#             if game_q_t4 == '4':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t5 = input('Существуют ли крылья, которые можно получить до хардмода? (да/нет) ')
#             if game_q_t5 == 'да' or game_q_t5 == 'Да' or game_q_t5 == 'lf':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t6 = input('Что даёт аксессуар "Счастливая подкова"? ')
#             if game_q_t6 == 'Дает невосприимчивость к урону от падения' or game_q_t6 == 'падение без урона' or game_q_t6 == 'невосприимчивость к урону от падения' or game_q_t6 == 'дает невосприимчивость к урону от падения':
#                 print('Молодец!')
#                 counter +=  1

#             else:
#                 print('Не верно')

#             game_q_t7 = input('Как называется отменённое продолжение игры "Terraria"? ')
#             if game_q_t7 == 'Otherworld' or game_q_t7 == 'otherworld':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             game_q_t8 = input('Какая самая высокая сложность в игре? ')
#             if game_q_t8 == 'Мастер' or game_q_t8 == 'мастер':
#                 print('Верно!')
#                 counter += 1 

#             else:
#                 print('Не верно')

#             game_q_t9 = input('Как называется лучший модификатор перековки для стрелковых оружий? ')
#             if game_q_t9 == 'Нереальный' or game_q_t9 == 'нереальный':
#                 print('Верно!')
#                 counter += 1

#             else:
#                 print('Не верно')

#             print(f'Вы набрали {counter} баллов из 10!')
#         else:
#             print('Такого квиза еще нет!')

#         back_k = input('Вернемся' + Fore.LIGHTBLUE_EX  + ' назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'сыграем еще?' + Fore.RESET)
#         if back_k == 'назад' or back_k == 'Назад':
#             l_func()

#         elif back_k == 'сыграем еще' or back_k == 'еще' or back_k == 'Сыграем еще' or back_k == 'Еще':
#             kviz()
#     kviz()
#     os.system('cls')

# elif game_selection == 'Угадай животное' or game_selection == 'угадай животное':
#     def guess_the_animal():
#         print('Загрузка...')
#         time.sleep(1)
#         print('50%')
#         time.sleep(0.5)
#         print('100%')
#         time.sleep(1)
#         print('Загрузка завершена')

#         guess = 'Это мини игра "Угадай животное", я буду отпралвять вам рисунки, а вы должны угадать кого я вам нарисовал!'
#         for char in guess: 
#             print(char, end='', flush=True) 
#             time.sleep(0.05)
#         print('')

#         score_counter = 0

#         print('Рисунок 1: ')
#         time.sleep(1)
#         print('''
#             ___
#         __/_  `.  .-"""-.
#         \_,  | \-'  /   )`-')
#             ) `"`    \  ((`"`
#         ___Y  ,    .'7 /|
#         (_,___/...-` (_/_/ 
#         ''')
#         q_quess_dog = input('Кто это? ')
#         if q_quess_dog == 'Собака' or q_quess_dog == 'собака' or q_quess_dog == 'щенок' or q_quess_dog == 'Щенок':
#             win_quess = 'Молодец!'
#             for char in win_quess: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             print(' ')

#             score_counter += 1

#         else:
#             lost = 'Нет же, это собака'
#             for char in lost: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             print(' ')

#         print('Рисунок 2: ')
#         time.sleep(1)
#         print('''
#                 /`·. 
#             / ... `:·
#         .·´      `·. .·´)
#         : © ): ;         {
#         `·. `·_   .·´\`·¸)
#             `\  \ .·´
#         ''')

#         q_quess_fish = input('Кто это? ')
#         if q_quess_fish == 'рыба' or q_quess_fish == 'Рыба' or q_quess_fish == 'рыбка' or q_quess_fish == 'Рыбка':
#             win_quess = 'Молодец!'
#             for char in win_quess: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             print(' ')

#             score_counter += 1

#         else:
#             lost = 'Нет же, это рыба'
#             for char in lost: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             print(' ')

#         print('Рисунок 3: ')
#         time.sleep(1)
#         print('''
#                         (
#                         )
#                         (
#                 /\  .-"""-.  /\

#                     //\\/  ,,,  \//\\
#                     |/\| ,;;;;;, |/\|
#                     //\\\;-"""-;///\\
#                     //  \/   .   \/  \\
#                 (| ,-_| \ | / |_-, |)
#                     //`__\.-.-./__`\\
#                     // /.-(() ())-.\ \\
#                 (\ |)   '---'   (| /)
#                     ` (|           |) `
#                     \)           (/
#             ''')

#             q_quess_spider = input('Кто это? ')
#             if q_quess_spider == 'паук' or q_quess_spider == 'Паук' or q_quess_spider == 'Паучок' or q_quess_spider == 'паучок':
#                 win_quess = 'Молодец!'
#                 for char in win_quess: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 print(' ')

#                 score_counter += 1

#             else:
#                 lost = 'Нет же, это паучок'
#                 for char in lost: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 print(' ')

#             print('Рисунок 4: ')
#             time.sleep(1)
#             print('''
#                                 _         _
#             .-""-.          ( )-"```"-( )          .-""-.
#             / O O  \          /         \          /  O O \

#             |O .-.  \        /   0 _ 0   \        /  .-. O|
#             \ (   )  '.    _|     (_)     |     .'  (   ) /
#             '.`-'     '-./ |             |`\.-'     '-'.'
#                 \         |  \   \     /   /  |         /
#                 \        \   '.  '._.'  .'   /        /
#                 \        '.   `'-----'`   .'        /
#                     \   .'    '-._        .-'\   '.   /
#                     |/`          `'''''')    )    `\|
#                     /                  (    (      ,\

#                     ;                    \    '-..-'/ ;
#                     |                     '.       /  |
#                     |                       `'---'`   |
#                     ;                                 ;
#                     \                               /
#                     `.                           .'
#                         '-._                   _.-'
#                         __/`"  '  - - -  ' "`` \__
#                     /`            /^\           `\

#                     \(          .'   '.         )/
#                         '.(__(__.-'       '.__)__).'
#             ''')

#             q_quess_bear = input('Что это? ')
#             if q_quess_bear == 'медведь' or q_quess_bear == 'Медведь':
#                 win_quess = 'Молодец!'
#                 for char in win_quess: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 print(' ')

#                 score_counter += 1

#             else:
#                 lost = 'Нет же, это медведь'
#                 for char in lost: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 print(' ')

#             stats_guess = 'Молодец, ты прошел Угадайку!'
#             for char in stats_guess: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             stats_guess1 = f'Ты угадал {score_counter} из 4 моих рисунков!'
#             for char in stats_guess1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#         guess_the_animal()
#         back_t = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'сыграем еще раз?' + Fore.RESET)
#         if back_t == 'вернемся' or back_t == 'вернемся назад' or back_t == 'Вернемся назад' or back_t == 'назад':
#             l_func()

#         elif back_t == 'сыграем еще раз' or back_t == 'еще раз' or back_t == 'сыграем':
#             guess_the_animal()

#         else:
#             print('Прости, я тебя не совсем понял')
#             l_func()

#         if back_t == 'Вернемся назад' or back_t == 'вернемся назад' or back_t == 'назад' or back_t == 'Назад':
#             l_func()
#             os.system('cls')

#         elif back_t == 'Сыграем еще раз' or back_t == 'сыграем еще раз' or back_t == 'еще раз' or back_t == 'Еще раз' or back_t == 'еще' or back_t == 'Еще':
#             guess_the_animal()
#             os.system('cls')

#     elif game_selection == 'Бросить монетку' or game_selection == 'бросить монетку' or game_selection == 'Монетка' or game_selection == 'монетка':
#         def lucky_money():
#             toss_coin = input('Бросить монетку? ' + Fore.LIGHTBLUE_EX + '(Да/Нет) ' + Fore.RESET)
#             if toss_coin == 'да' or toss_coin == 'да' or toss_coin == 'lf':
#                 def cast():
#                     toss_coin1 = 'Вы подбросили монетку...'
#                     for char in toss_coin1: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     time.sleep(1)
#                     random_event = random.randint(['Орел', 'Решка'])
#                     result_random = random_event

#                     if result_random == 'Решка':
#                         result_lucky = 'Вам выпала орешка!'
#                         for char in result_lucky: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         def repeat_bros1():
#                             repeat_q_money = input('Бросить снова? ')
#                             if repeat_q_money == 'Да' or repeat_q_money == 'да' or repeat_q_money == 'lf':
#                                 cast()

#                             else:
#                                 return_back = input('Вернемся назад? ' + Fore.LIGHTBLUE_EX + '(Да/Нет) ' + Fore.RESET)
#                                 if return_back == 'Да' or return_back == 'да' or return_back == 'lf':
#                                     print('')

#                                 else:
#                                     repeat_bros1()

#                         repeat_bros1()

#                     elif result_random == 'Орел':
#                         result_lucky1 = 'Вам выпал орел!'
#                         for char in result_lucky1: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')
#                         def repeat_bros2():
#                             repeat_q_money = input('Бросить снова? ')
#                             if repeat_q_money == 'Да' or repeat_q_money == 'да' or repeat_q_money == 'lf':
#                                 cast()

#                             else:
#                                 return_back = input('Вернемся назад? ' + Fore.LIGHTBLUE_EX + '(Да/Нет) ' + Fore.RESET)
#                                 if return_back == 'Да' or return_back == 'да' or return_back == 'lf':
#                                     l_func()

#                                 else:
#                                     repeat_bros2()

#                         repeat_bros2()

#                 cast()
#             else:
#                 while True:
#                     repeat_q = input('А теперь бросить монетку? ' + Fore.LIGHTBLUE_EX + '(Да) ' + Fore.RESET)
#                     if repeat_q == 'да' or repeat_q == 'Да':
#                         cast() 
#                         break

#                     else:
#                         print()
#         lucky_money()
#         os.system('cls')

#     elif game_selection == 'Морской бой' or game_selection == 'морской бой':
#         def battle_ships():
#             field = [
#                 [1,1,1,1,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,1,1,0],
#                 [0,0,1,0,0,0,0,0,0,0],
#                 [0,0,0,0,1,0,0,0,0,0],
#                 [0,0,0,0,1,0,0,0,0,0],
#                 [1,0,0,0,1,0,1,1,1,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,1],
#                 [1,0,0,0,1,1,0,0,0,1],
#                 [0,0,1,0,0,0,0,0,0,0],
#             ]

#             graphics_map = {
#                 0: " ",
#                 1: "#",
#                 2: "X",
#                 3: ". ",
#             }

#             game_over = False
#             while game_over is False:
#                 os.system('cls')
#                 print(" ", 0,1,2,3,4,5,6,7,8,9)

#                 for i, row in enumerate(field):
#                     print(i, end=" ")
#                     for item in row:
#                         print(graphics_map[item] if item != 1 else " ", end="")
#                     print()

#                 n, m = map(int, input("Введите координаты выстрела: ").split())
#                 if field[n][m] == 0:
#                     field[n][m] = 3

#                 elif field[n][m] == 1:
#                     field[n][m] = 2

#                 else:
#                     field[n][m] = 3

#         battle_ships()
#         back_t = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'сыграем еще раз?' + Fore.RESET)
#         if back_t == 'вернемся' or back_t == 'вернемся назад' or back_t == 'Вернемся назад' or back_t == 'назад':
#             l_func()

#         elif back_t == 'сыграем еще раз' or back_t == 'еще раз' or back_t == 'сыграем':
#             battle_ships()

#         else:
#             print('Прости, я тебя не совсем понял')
#             l_func()

#     elif game_selection == 'Камень - ножинцы - бумага' or game_selection == 'камень, ножницы, бумага' or game_selection == 'камень - ножницы - бумага':
#         def random_figure():
#             player_score = 0
#             comp_score = 0
#             counter_win = 0

#             while True:
#                 print()
#                 user = input('Введите вашу фигуру(камень, ножницы, бумага): ')
#                 bot = random.choice(['камень', 'ножницы', 'бумага'])

#                 if (user == 'камень' and bot == 'ножницы') or (user == 'ножницы' and bot == 'бумага') or (user == 'бумага' and bot == 'камень'):
#                     print('Бот: ', bot)
#                     time.sleep(1)
#                     print('Вы победили!')
#                     player_score += 1
#                     counter_win += 1

#                 elif user == bot:
#                     print('Бот: ', bot)
#                     time.sleep(1)
#                     print('Ничья!')

#                 else:
#                     print('Бот: ', bot)
#                     time.sleep(1)
#                     print('Вы проиграли!')
#                     comp_score += 1
#                     counter_win += 1

#                 if counter_win == 3:
#                     print()
#                     print('Ваш счет: ', player_score)
#                     print('Счет бота: ', comp_score)

#                     if player_score <= comp_score:
#                         print("Вы проиграли!")

#                     elif player_score >= comp_score:
#                         print('Вы победили!')
#                     break
#         random_figure()

#         back_t = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'сыграем еще раз?' + Fore.RESET)
#         if back_t == 'вернемся' or back_t == 'вернемся назад' or back_t == 'Вернемся назад' or back_t == 'назад':
#             l_func()

#         elif back_t == 'сыграем еще раз' or back_t == 'еще раз' or back_t == 'сыграем':
#             random_figure()

#         else:
#             print('Прости, я тебя не совсем понял')
#             l_func()

#     else:
#         print('Такой игры еще нету')

# elif question_class == 'Хочу читать' or question_class == 'хочу читать' or question_class == 'читать' or question_class == 'Читать':
#     def read_book():
#         print(' ')
#         print('Загрузка библиотеки книг...')
#         time.sleep(1)
#         print('20%')
#         time.sleep(1)
#         print('45%')
#         time.sleep(1)
#         print('80%')
#         time.sleep(1)
#         print('99%')
#         time.sleep(1)
#         print('Загрузка завершена!')
#         time.sleep(1)
#         while True:
#             author_selection = 'В моей библиотеке есть такие авторы как:' + Fore.LIGHTBLUE_EX + ' Пушкин' + Fore.RESET + ', ' + Fore.LIGHTBLUE_EX + 'Лермонтов' +  Fore.RESET + ', ' + Fore.LIGHTBLUE_EX + 'Тургенев' + Fore.RESET + ', ' + Fore.LIGHTBLUE_EX + 'Толстой' + Fore.RESET
#             for char in author_selection: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             author_selection_q = input('Чьи произведения вам больше нравятся? ')
#             if author_selection_q == 'Пушкин' or author_selection_q == 'пушкин':
#                 selection = 'Прекрасный выбор!'
#                 for char in selection: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 book_selection_p = 'Я знаю такие произведения как: "Осень", "Пророк", "Я помню чудное мгновенье (Керн)", "Во глубине сибирских руд", "Я памятник себе воздвиг нерукотворный", "Письмо Татьяны к Онегину"'
#                 for char in book_selection_p: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 book_selection_pq = input('Какое произведение выберите? ')
#                 if book_selection_pq == 'Осень' or book_selection_pq == 'осень':
#                     print(' ')
#                     print('Загрузка...')
#                     time.sleep(2)
#                     text_autumn_p = '''I
#     Октябрь уж наступил — уж роща отряхает
#     Последние листы с нагих своих ветвей;
#     Дохнул осенний хлад — дорога промерзает.
#     Журча еще бежит за мельницу ручей,
#     Но пруд уже застыл; сосед мой поспешает
#     В отъезжие поля с охотою своей,
#     И страждут озими от бешеной забавы,
#     И будит лай собак уснувшие дубравы.

#     II
#     Теперь моя пора: я не люблю весны;
#     Скучна мне оттепель; вонь, грязь — весной я болен;
#     Кровь бродит; чувства, ум тоскою стеснены.
#     Суровою зимой я более доволен,
#     Люблю ее снега; в присутствии луны
#     Как легкий бег саней с подругой быстр и волен,
#     Когда под соболем, согрета и свежа,
#     Она вам руку жмет, пылая и дрожа!

#     III
#     Как весело, обув железом острым ноги,
#     Скользить по зеркалу стоячих, ровных рек!
#     А зимних праздников блестящие тревоги?..
#     Но надо знать и честь; полгода снег да снег,
#     Ведь это наконец и жителю берлоги,
#     Медведю, надоест. Нельзя же целый век
#     Кататься нам в санях с Армидами младыми
#     Иль киснуть у печей за стеклами двойными.

#     IV
#     Ох, лето красное! любил бы я тебя,
#     Когда б не зной, да пыль, да комары, да мухи.
#     Ты, все душевные способности губя,
#     Нас мучишь; как поля, мы страждем от засухи;
#     Лишь как бы напоить, да освежить себя —
#     Иной в нас мысли нет, и жаль зимы старухи,
#     И, проводив ее блинами и вином,
#     Поминки ей творим мороженым и льдом.

#     V
#     Дни поздней осени бранят обыкновенно,
#     Но мне она мила, читатель дорогой,
#     Красою тихою, блистающей смиренно.
#     Так нелюбимое дитя в семье родной
#     К себе меня влечет. Сказать вам откровенно,
#     Из годовых времен я рад лишь ей одной,
#     В ней много доброго; любовник не тщеславный,
#     Я нечто в ней нашел мечтою своенравной.

#     VI
#     Как это объяснить? Мне нравится она,
#     Как, вероятно, вам чахоточная дева
#     Порою нравится. На смерть осуждена,
#     Бедняжка клонится без ропота, без гнева.
#     Улыбка на устах увянувших видна;
#     Могильной пропасти она не слышит зева;
#     Играет на лице еще багровый цвет.
#     Она жива еще сегодня, завтра нет.

#     VII
#     Унылая пора! очей очарованье!
#     Приятна мне твоя прощальная краса —
#     Люблю я пышное природы увяданье,
#     В багрец и в золото одетые леса,
#     В их сенях ветра шум и свежее дыханье,
#     И мглой волнистою покрыты небеса,
#     И редкий солнца луч, и первые морозы,
#     И отдаленные седой зимы угрозы.

#     VIII
#     И с каждой осенью я расцветаю вновь;
#     Здоровью моему полезен русской холод;
#     К привычкам бытия вновь чувствую любовь:
#     Чредой слетает сон, чредой находит голод;
#     Легко и радостно играет в сердце кровь,
#     Желания кипят — я снова счастлив, молод,
#     Я снова жизни полн — таков мой организм
#     (Извольте мне простить ненужный прозаизм).

#     IX
#     Ведут ко мне коня; в раздолии открытом,
#     Махая гривою, он всадника несет,
#     И звонко под его блистающим копытом
#     Звенит промерзлый дол и трескается лед.
#     Но гаснет краткий день, и в камельке забытом
#     Огонь опять горит — то яркий свет лиет,
#     То тлеет медленно — а я пред ним читаю
#     Иль думы долгие в душе моей питаю.

#     X
#     И забываю мир — и в сладкой тишине
#     Я сладко усыплен моим воображеньем,
#     И пробуждается поэзия во мне:
#     Душа стесняется лирическим волненьем,
#     Трепещет и звучит, и ищет, как во сне,
#     Излиться наконец свободным проявленьем —
#     И тут ко мне идет незримый рой гостей,
#     Знакомцы давние, плоды мечты моей.

#     XI
#     И мысли в голове волнуются в отваге,
#     И рифмы легкие навстречу им бегут,
#     И пальцы просятся к перу, перо к бумаге,
#     Минута — и стихи свободно потекут.
#     Так дремлет недвижим корабль в недвижной влаге,
#     Но чу! — матросы вдруг кидаются, ползут
#     Вверх, вниз — и паруса надулись, ветра полны;
#     Громада двинулась и рассекает волны.

#     XII
#     Плывет. Куда ж нам плыть?
#     . . . . . . . . . . . .
#     . . . . . . . . . . . .

#     ___________

#     Год: 1833'''
#                     for char in text_autumn_p: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')
#                     print('Конец')

#                 elif book_selection_pq == 'Пророк' or book_selection_pq == 'пророк':
#                     print('Загрузка... ')
#                     time.sleep(1)
#                     print(' ')
#                     prorok = '''Духовной жаждою томим,
#                     В пустыне мрачной я влачился, —
#                     И шестикрылый серафим
#                     На перепутье мне явился.
#                     Перстами легкими как сон
#                     Моих зениц коснулся он.
#                     Отверзлись вещие зеницы,
#                     Как у испуганной орлицы.
#                     Моих ушей коснулся он, —
#                     И их наполнил шум и звон:
#                     И внял я неба содроганье,
#                     И горний ангелов полет,
#                     И гад морских подводный ход,
#                     И дольней лозы прозябанье.
#                     И он к устам моим приник,
#                     И вырвал грешный мой язык,
#                     И празднословный и лукавый,
#                     И жало мудрыя змеи
#                     В уста замершие мои
#                     Вложил десницею кровавой.
#                     И он мне грудь рассек мечом,
#                     И сердце трепетное вынул,
#                     И угль, пылающий огнем,
#                     Во грудь отверстую водвинул.
#                     Как труп в пустыне я лежал,
#                     И бога глас ко мне воззвал:
#                     «Восстань, пророк, и виждь, и внемли,
#                     Исполнись волею моей,
#                     И, обходя моря и земли,
#                     Глаголом жги сердца людей».
#                     1956—1962.
#                     1826 г.'''
#                     for char in prorok: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_pq == 'Я помню чудное мгновенье' or book_selection_pq == 'Я помню чудное мгновенье (Керн)' or  book_selection_pq == 'я помню чудное мгновенье' or book_selection_pq == 'я помню чудное мгновенье (Керн)':
#                     print('Загрузка... ')
#                     time.sleep(2)
#                     print(' ')
#                     mgnovenie = '''Я помню чудное мгновенье:
#     Передо мной явилась ты,
#     Как мимолетное виденье,
#     Как гений чистой красоты.
#     В томленьях грусти безнадежной,
#     В тревогах шумной суеты,
#     Звучал мне долго голос нежный
#     И снились милые черты.
#     Шли годы. Бурь порыв мятежный
#     Рассеял прежние мечты,
#     И я забыл твой голос нежный,
#     Твои небесные черты.
#     В глуши, во мраке заточенья
#     Тянулись тихо дни мои
#     Без божества, без вдохновенья,
#     Без слез, без жизни, без любви.
#     Душе настало пробужденье:
#     И вот опять явилась ты,
#     Как мимолетное виденье,
#     Как гений чистой красоты.
#     И сердце бьется в упоенье,
#     И для него воскресли вновь
#     И божество, и вдохновенье,
#     И жизнь, и слезы, и любовь.'''
#                     for char in mgnovenie: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_pq == 'Во глубине сибирских руд' or book_selection_pq == 'во глубине сибирских руд':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     vo_glubone_sib_rud = '''Во глубине сибирских руд
#     Храните гордое терпенье,
#     Не пропадет ваш скорбный труд
#     И дум высокое стремленье.
#     Несчастью верная сестра,
#     Надежда в мрачном подземелье
#     Разбудит бодрость и веселье,
#     Придет желанная пора:
#     Любовь и дружество до вас
#     Дойдут сквозь мрачные затворы,
#     Как в ваши каторжные норы
#     Доходит мой свободный глас.
#     Оковы тяжкие падут,
#     Темницы рухнут — и свобода
#     Вас примет радостно у входа,
#     И братья меч вам отдадут.
#     1827 г.'''
#                     for char in vo_glubone_sib_rud: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_pq == 'Я памятник себе воздвиг нерукотворный' or book_selection_pq == 'я памятник себе воздвиг нерукотворный':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     pamatnik_p = '''Я памятник себе воздвиг нерукотворный,
#     К нему не зарастет народная тропа,
#     Вознесся выше он главою непокорной
#     Александрийского столпа.
#     Нет, весь я не умру — душа в заветной лире
#     Мой прах переживет и тленья убежит —
#     И славен буду я, доколь в подлунном мире
#     Жив будет хоть один пиит.
#     Слух обо мне пройдет по всей Руси великой,
#     И назовет меня всяк сущий в ней язык,
#     И гордый внук славян, и финн, и ныне дикой
#     Тунгус, и друг степей калмык.
#     И долго буду тем любезен я народу,
#     Что чувства добрые я лирой пробуждал,
#     Что в мой жестокий век восславил я Свободу
#     И милость к падшим призывал.
#     Веленью божию, о муза, будь послушна,
#     Обиды не страшась, не требуя венца,
#     Хвалу и клевету приемли равнодушно
#     И не оспоривай глупца.
#     1836 г.'''
#                     for char in pamatnik_p: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_pq == 'Письмо Татьяны к Онегину' or book_selection_pq == 'письмо Татьяны к Онегину':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print('')
#                     pismo_tatyani = '''Я к вам пишу — чего же боле?
#     Что я могу еще сказать?
#     Теперь, я знаю, в вашей воле
#     Меня презреньем наказать.
#     Но вы, к моей несчастной доле
#     Хоть каплю жалости храня,
#     Вы не оставите меня.
#     Сначала я молчать хотела;
#     Поверьте: моего стыда
#     Вы не узнали б никогда,
#     Когда б надежду я имела
#     Хоть редко, хоть в неделю раз
#     В деревне нашей видеть вас,
#     Чтоб только слышать ваши речи,
#     Вам слово молвить, и потом
#     Все думать, думать об одном
#     И день и ночь до новой встречи.
#     Но, говорят, вы нелюдим;
#     В глуши, в деревне всё вам скучно,
#     А мы… ничем мы не блестим,
#     Хоть вам и рады простодушно.
#     Зачем вы посетили нас?
#     В глуши забытого селенья
#     Я никогда не знала б вас,
#     Не знала б горького мученья.
#     Души неопытной волненья
#     Смирив со временем (как знать?),
#     По сердцу я нашла бы друга,
#     Была бы верная супруга
#     И добродетельная мать.
#     Другой!.. Нет, никому на свете
#     Не отдала бы сердца я!
#     То в вышнем суждено совете…
#     То воля неба: я твоя;
#     Вся жизнь моя была залогом
#     Свиданья верного с тобой;
#     Я знаю, ты мне послан богом,
#     До гроба ты хранитель мой…
#     Ты в сновиденьях мне являлся,
#     Незримый, ты мне был уж мил,
#     Твой чудный взгляд меня томил,
#     В душе твой голос раздавался
#     Давно… нет, это был не сон!
#     Ты чуть вошел, я вмиг узнала,
#     Вся обомлела, запылала
#     И в мыслях молвила: вот он!
#     Не правда ль? Я тебя слыхала:
#     Ты говорил со мной в тиши,
#     Когда я бедным помогала
#     Или молитвой услаждала
#     Тоску волнуемой души?
#     И в это самое мгновенье
#     Не ты ли, милое виденье,
#     В прозрачной темноте мелькнул,
#     Приникнул тихо к изголовью?
#     Не ты ль, с отрадой и любовью,
#     Слова надежды мне шепнул?
#     Кто ты, мой ангел ли хранитель,
#     Или коварный искуситель:
#     Мои сомненья разреши.
#     Быть может, это все пустое,
#     Обман неопытной души!
#     И суждено совсем иное…
#     Но так и быть! Судьбу мою
#     Отныне я тебе вручаю,
#     Перед тобою слезы лью,
#     Твоей защиты умоляю…
#     Вообрази: я здесь одна,
#     Никто меня не понимает,
#     Рассудок мой изнемогает,
#     И молча гибнуть я должна.
#     Я жду тебя: единым взором
#     Надежды сердца оживи
#     Иль сон тяжелый перерви,
#     Увы, заслуженным укором!
#     Кончаю! Страшно перечесть…
#     Стыдом и страхом замираю…
#     Но мне порукой ваша честь,
#     И смело ей себя вверяю…
#     1833 г.'''
#                     for char in pismo_tatyani: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 else:
#                     error_read = '''Извините, пока такого произведения я не знаю'''
#                     for char in error_read: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     help_user = input('Возникли проблемы? ' + Fore.LIGHTBLUE_EX + 'да/нет ' + Fore.RESET)
#                     if help_user == 'Да' or help_user == 'да':
#                         help_user1 = 'Выбор помечен светло-синим цветом, просто скопируй и вставь в ответ'
#                         for char in help_user1: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         print('''Если возникли другие проблеммы напиши в поддержку!
#                             Почта для связи: Vox.assistent.spprt@yandex.ru''')

#                     else:
#                         read_book()

#             elif author_selection_q == 'Лермонтов' or author_selection_q == 'лермонтов':
#                 selection = 'Прекрасный выбор!'
#                 for char in selection: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 book_selection_l = 'Я знаю такие произведения как: "Бородино", "Смерть поэта", "Родина", "Белеет парус одинокий"'
#                 for char in book_selection_l: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 book_selection_lq = input('Какое произведение выберите? ')
#                 if book_selection_lq == 'Бородино' or book_selection_lq == 'бородино':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     borodino = '''— Скажи-ка, дядя, ведь недаром
#     Москва, спаленная пожаром,
#     Французу отдана?
#     Ведь были ж схватки боевые,
#     Да, говорят, еще какие!
#     Недаром помнит вся Россия
#     Про день Бородина!
#     — Да, были люди в наше время,
#     Не то, что нынешнее племя:
#     Богатыри — не вы!
#     Плохая им досталась доля:
#     Немногие вернулись с поля…
#     Не будь на то господня воля,
#     Не отдали б Москвы!
#     Мы долго молча отступали,
#     Досадно было, боя ждали,
#     Ворчали старики:
#     «Что ж мы? на зимние квартиры?
#     Не смеют, что ли, командиры
#     Чужие изорвать мундиры
#     О русские штыки?»
#     И вот нашли большое поле:
#     Есть разгуляться где на воле!
#     Построили редут.
#     У наших ушки на макушке!
#     Чуть утро осветило пушки
#     И леса синие верхушки —
#     Французы тут как тут.
#     Забил заряд я в пушку туго
#     И думал: угощу я друга!
#     Постой-ка, брат мусью!
#     Что тут хитрить, пожалуй к бою;
#     Уж мы пойдем ломить стеною,
#     Уж постоим мы головою
#     За родину свою!
#     Два дня мы были в перестрелке.
#     Что толку в этакой безделке?
#     Мы ждали третий день.
#     Повсюду стали слышны речи:
#     «Пора добраться до картечи!»
#     И вот на поле грозной сечи
#     Ночная пала тень.
#     Прилег вздремнуть я у лафета,
#     И слышно было до рассвета,
#     Как ликовал француз.
#     Но тих был наш бивак открытый:
#     Кто кивер чистил весь избитый,
#     Кто штык точил, ворча сердито,
#     Кусая длинный ус.
#     И только небо засветилось,
#     Все шумно вдруг зашевелилось,
#     Сверкнул за строем строй.
#     Полковник наш рожден был хватом:
#     Слуга царю, отец солдатам…
#     Да, жаль его: сражен булатом,
#     Он спит в земле сырой.
#     И молвил он, сверкнув очами:
#     «Ребята! не Москва ль за нами?
#     Умремте ж под Москвой,
#     Как наши братья умирали!»
#     И умереть мы обещали,
#     И клятву верности сдержали
#     Мы в Бородинский бой.
#     Ну ж был денек! Сквозь дым летучий
#     Французы двинулись, как тучи,
#     И всё на наш редут.
#     Уланы с пестрыми значками,
#     Драгуны с конскими хвостами,
#     Все промелькнули перед нами,
#     Все побывали тут.
#     Вам не видать таких сражений!..
#     Носились знамена, как тени,
#     В дыму огонь блестел,
#     Звучал булат, картечь визжала,
#     Рука бойцов колоть устала,
#     И ядрам пролетать мешала
#     Гора кровавых тел.
#     Изведал враг в тот день немало,
#     Что значит русский бой удалый,
#     Наш рукопашный бой!..
#     Земля тряслась — как наши груди,
#     Смешались в кучу кони, люди,
#     И залпы тысячи орудий
#     Слились в протяжный вой…
#     Вот смерклось. Были все готовы
#     Заутра бой затеять новый
#     И до конца стоять…
#     Вот затрещали барабаны —
#     И отступили бусурманы.
#     Тогда считать мы стали раны,
#     Товарищей считать.
#     Да, были люди в наше время,
#     Могучее, лихое племя:
#     Богатыри — не вы.
#     Плохая им досталась доля:
#     Немногие вернулись с поля.
#     Когда б на то не божья воля,
#     Не отдали б Москвы!
#     1837 г.'''

#                     for char in borodino: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_lq == 'Смерть поэта' or book_selection_lq == 'смерть поэта':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     smert_poeta = '''Отмщенье, государь, отмщенье!
#     Паду к ногам твоим:
#     Будь справедлив и накажи убийцу,
#     Чтоб казнь его в позднейшие века
#     Твой правый суд потомству возвестила,
#     Чтоб видели злодеи в ней пример.
#     Погиб поэт! — невольник чести —
#     Пал, оклеветанный молвой,
#     С свинцом в груди и жаждой мести,
#     Поникнув гордой головой!..
#     Не вынесла душа поэта
#     Позора мелочных обид,
#     Восстал он против мнений света
#     Один, как прежде… и убит!
#     Убит!.. К чему теперь рыданья,
#     Пустых похвал ненужный хор
#     И жалкий лепет оправданья?
#     Судьбы свершился приговор!
#     Не вы ль сперва так злобно гнали
#     Его свободный, смелый дар
#     И для потехи раздували
#     Чуть затаившийся пожар?
#     Что ж? веселитесь… Он мучений
#     Последних вынести не мог:
#     Угас, как светоч, дивный гений,
#     Увял торжественный венок.
#     Его убийца хладнокровно
#     Навел удар… спасенья нет:
#     Пустое сердце бьется ровно,
#     В руке не дрогнул пистолет.
#     И что за диво?.. издалека,
#     Подобный сотням беглецов,
#     На ловлю счастья и чинов
#     Заброшен к нам по воле рока;
#     Смеясь, он дерзко презирал
#     Земли чужой язык и нравы;
#     Не мог щадить он нашей славы;
#     Не мог понять в сей миг кровавый,
#     На что он руку поднимал!..
#     И он убит — и взят могилой,
#     Как тот певец, неведомый, но милый,
#     Добыча ревности глухой,
#     Воспетый им с такою чудной силой,
#     Сраженный, как и он, безжалостной рукой.
#     Зачем от мирных нег и дружбы простодушной
#     Вступил он в этот свет завистливый и душный
#     Для сердца вольного и пламенных страстей?
#     Зачем он руку дал клеветникам ничтожным,
#     Зачем поверил он словам и ласкам ложным,
#     Он, с юных лет постигнувший людей?..
#     И прежний сняв венок — они венец терновый,
#     Увитый лаврами, надели на него:
#     Но иглы тайные сурово
#     Язвили славное чело;
#     Отравлены его последние мгновенья
#     Коварным шепотом насмешливых невежд,
#     И умер он — с напрасной жаждой мщенья,
#     С досадой тайною обманутых надежд.
#     Замолкли звуки чудных песен,
#     Не раздаваться им опять:
#     Приют певца угрюм и тесен,
#     И на устах его печать.
#     А вы, надменные потомки
#     Известной подлостью прославленных отцов,
#     Пятою рабскою поправшие обломки
#     Игрою счастия обиженных родов!
#     Вы, жадною толпой стоящие у трона,
#     Свободы, Гения и Славы палачи!
#     Таитесь вы под сению закона,
#     Пред вами суд и правда — всё молчи!..
#     Но есть и божий суд, наперсники разврата!
#     Есть грозный суд: он ждет;
#     Он не доступен звону злата,
#     И мысли, и дела он знает наперед.
#     Тогда напрасно вы прибегнете к злословью:
#     Оно вам не поможет вновь,
#     И вы не смоете всей вашей черной кровью
#     Поэта праведную кровь!
#     1837 г.'''

#                     for char in smert_poeta: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_lq == 'Родина' or book_selection_lq == 'родина':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     rodina = '''Люблю отчизну я, но странною любовью!
#     Не победит ее рассудок мой.
#     Ни слава, купленная кровью,
#     Ни полный гордого доверия покой,
#     Ни темной старины заветные преданья
#     Не шевелят во мне отрадного мечтанья.
#     Но я люблю — за что, не знаю сам —
#     Ее степей холодное молчанье,
#     Ее лесов безбрежных колыханье,
#     Разливы рек ее, подобные морям;
#     Проселочным путем люблю скакать в телеге
#     И, взором медленным пронзая ночи тень,
#     Встречать по сторонам, вздыхая о ночлеге,
#     Дрожащие огни печальных деревень;
#     Люблю дымок спаленной жнивы,
#     В степи ночующий обоз
#     И на холме средь желтой нивы
#     Чету белеющих берез.
#     С отрадой, многим незнакомой,
#     Я вижу полное гумно,
#     Избу, покрытую соломой,
#     С резными ставнями окно;
#     И в праздник, вечером росистым,
#     Смотреть до полночи готов
#     На пляску с топаньем и свистом
#     Под говор пьяных мужичков.
#     1841 г.'''

#                     for char in rodina: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_lq == 'Белеет парус одинокий' or book_selection_lq == 'белеет парус одинокий':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     parys = '''Белеет парус одинокой
#     В тумане моря голубом!..
#     Что ищет он в стране далекой?
#     Что кинул он в краю родном?..
#     Играют волны — ветер свищет,
#     И мачта гнется и скрыпит…
#     Увы! он счастия не ищет
#     И не от счастия бежит!
#     Под ним струя светлей лазури,
#     Над ним луч солнца золотой…
#     А он, мятежный, просит бури,
#     Как будто в бурях есть покой!
#     1832 г.'''

#                     for char in parys: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 else:
#                     error_read = 'Извините, пока такого произведения я не знаю'
#                     for char in error_read: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     help_user = input('Возникли проблемы? ' + Fore.LIGHTBLUE_EX + 'да/нет ' + Fore.RESET)
#                     if help_user == 'Да' or help_user == 'да':
#                         help_user1 = 'Выбор помечен светло-синим цветом, просто скопируй и вставь в ответ'
#                         for char in help_user1: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                         print('''Если возникли другие проблеммы напиши в поддержку!
#                             Почта для связи: Vox.assistent.spprt@yandex.ru''')
#                     else:
#                         read_book()

#             elif author_selection_q == 'Тургенев' or author_selection_q == 'тургенев':
#                 selection = 'Прекрасный выбор!'

#                 book_selection_t = 'Я знаю такие произведения как: "Воробей", "Лес и степь", "Синица"'
#                 for char in book_selection_t: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 book_selection_tq = input('Какое произведение выберите? ')
#                 if book_selection_tq == 'Воробей' or book_selection_tq == 'воробей':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     vorobey = '''Я возвращался с охоты и шел по аллее сада. Собака бежала впереди меня.
#     Вдруг она уменьшила свои шаги и начала красться, как бы зачуяв перед собою дичь.
#     Я глянул вдоль аллеи и увидел молодого воробья с желтизной около клюва и пухом на голове. Он упал из гнезда (ветер сильно качал березы аллеи) и сидел неподвижно, беспомощно растопырив едва прораставшие крылышки.
#     Моя собака медленно приближалась к нему, как вдруг, сорвавшись с близкого дерева, старый черногрудый воробей камнем упал перед самой ее мордой — и весь взъерошенный, искаженный, с отчаянным и жалким писком прыгнул раза два в направлении зубастой раскрытой пасти.
#     Он ринулся спасать, он заслонил собою свое детище… но всё его маленькое тело трепетало от ужаса, голосок одичал и охрип, он замирал, он жертвовал собою!
#     Каким громадным чудовищем должна была ему казаться собака! И все-таки он не мог усидеть на своей высокой, безопасной ветке… Сила, сильнее его воли, сбросила его оттуда.
#     Мой Трезор остановился, попятился… Видно, и он признал эту силу.
#     Я поспешил отозвать смущенного пса — и удалился, благоговея.
#     Да; не смейтесь. Я благоговел перед той маленькой героической птицей, перед любовным ее порывом.
#     Любовь, думал я, сильнее смерти и страха смерти. Только ею, только любовью держится и движется жизнь.'''

#                     for char in vorobey: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_tq == 'Лес и степь' or book_selection_tq == 'лес и степь':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     les_and_step = '''…И понемногу начало назад
#     Его тянуть: в деревню, в темный сад,
#     Где липы так огромны, так тенисты,
#     И ландыши так девственно душисты,
#     Где круглые ракиты над водой
#     С плотины наклонились чередой,
#     Где тучный дуб растет над тучной нивой,
#     Где пахнет конопелью да крапивой…
#     Туда, туда, в раздольные поля,
#     Где бархатом чернеется земля,
#     Где рожь, куда ни киньте вы глазами,
#     Струится тихо мягкими волнами.
#     И падает тяжелый желтый луч
#     Из-за прозрачных, белых, круглых туч;
#     Там хорошо ………'''

#                     for char in les_and_step: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_tq == 'Синица' or book_selection_tq == 'синица':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     sinitsa = '''Слышу я: звенит синица
#     Средь желтеющих ветвей;
#     Здравствуй, маленькая птица,
#     Вестница осенних дней! Хоть грозит он нам ненастьем,
#     Хоть зимы он нам пророк —
#     Дышит благодатным счастьем
#     Твой веселый голосок.В песенке твоей приветной
#     Слух пленен ужели ж мой
#     Лишь природы безответной
#     Равнодушною игрой? Иль беспечно распевает
#     И в тебе охота жить —
#     Та, что людям помогает
#     Смерть и жизнь переносить?
#     1863 г.'''

#                     for char in sinitsa: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 else:
#                     error_read = 'Извините, пока такого произведения я не знаю'
#                     for char in error_read: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     help_user = input('Возникли проблемы? ' + Fore.LIGHTBLUE_EX + 'да/нет ' + Fore.RESET)
#                     if help_user == 'Да' or help_user == 'да':
#                         help_user1 = 'Выбор помечен светло-синим цветом, просто скопируй и вставь в ответ'
#                         print('''Если возникли другие проблеммы напиши в поддержку!
#                             Почта для связи: Vox.assistent.spprt@yandex.ru''')

#                     else:
#                         read_book()

#             elif author_selection_q == 'Толстой' or author_selection_q == 'толстой':
#                 selection = 'Прекрасный выбор!'

#                 book_selection_ltl = 'Я знаю такие произведения как: "Средь шумного бала, случайно", "Край ты мой, родимый край", "Осень", "История государства российского", "Не ветер, вея с высоты"'
#                 book_selection_tlq = input('Какое произведение выберите? ')
#                 if book_selection_tlq == 'Средь шумного бала, случайно' or book_selection_tlq == 'средь шумного бала, случайно':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     bal = '''Средь шумного бала, случайно,
#     В тревоге мирской суеты,
#     Тебя я увидел, но тайна
#     Твои покрывала черты.
#     Лишь очи печально глядели,
#     А голос так дивно звучал,
#     Как звон отдаленной свирели,
#     Как моря играющий вал.
#     Мне стан твой понравился тонкий
#     И весь твой задумчивый вид,
#     А смех твой, и грустный и звонкий,
#     С тех пор в моем сердце звучит.
#     В часы одинокие ночи
#     Люблю я, усталый, прилечь —
#     Я вижу печальные очи,
#     Я слышу веселую речь;
#     И грустно я так засыпаю,
#     И в грезах неведомых сплю…
#     Люблю ли тебя — я не знаю,
#     Но кажется мне, что люблю!
#     1851 г.'''

#                     for char in bal: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_tlq == 'Край ты мой, родимый край' or book_selection_tlq == 'край ты мой, родимый край':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     krai_rodnoy = '''Край ты мой, родимый край!
#     Конский бег на воле,
#     В небе крик орлиных стай,
#     Волчий голос в поле! Гой ты, родина моя!
#     Гой ты, бор дремучий!
#     Свист полночный соловья,
#     Ветер, степь да тучи!'''

#                     for char in krai_rodnoy: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_tlq == 'Осень' or book_selection_tlq == 'осень':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     autumn_t = '''Осень. Обсыпается весь наш бедный сад,
#     Листья пожелтелые по ветру летят;
#     Лишь вдали красуются, там на дне долин,
#     Кисти ярко-красные вянущих рябин.
#     Весело и горестно сердцу моему,
#     Молча твои рученьки грею я и жму,
#     В очи тебе глядючи, молча слезы лью,
#     Не умею высказать, как тебя люблю.
#     1858 г.'''

#                     for char in autumn_t: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_tlq == 'История государства российского' or book_selection_tlq == 'история государства российского':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     history_rf = '''1
#     Послушайте, ребята,
#     Что вам расскажет дед.
#     Земля наша богата,
#     Порядка в ней лишь нет.
#     2
#     А эту правду, детки,
#     За тысячу уж лет
#     Смекнули наши предки:
#     Порядка-де, вишь, нет.
#     3
#     И стали все под стягом,
#     И молвят: «Как нам быть?
#     Давай пошлем к варягам:
#     Пускай придут княжить.
#     4
#     Ведь немцы тороваты,
#     Им ведом мрак и свет,
#     Земля ж у нас богата,
#     Порядка в ней лишь нет».
#     5
#     Посланцы скорым шагом
#     Отправились туда
#     И говорят варягам:
#     «Придите, господа!
#     6Мы вам отсыплем злата,
#     Что киевских конфет;
#     Земля у нас богата,
#     Порядка в ней лишь нет».
#     7Варягам стало жутко,
#     Но думают: «Что ж тут?
#     Попытка ведь не шутка —
#     Пойдем, коли зовут!»
#     8
#     И вот пришли три брата,
#     Варяги средних лет,
#     Глядят — земля богата,
#     Порядка ж вовсе нет.
#     9
#     «Ну, — думают, — команда!
#     Здесь ногу сломит черт,
#     Es ist ja eine Schande,
#     Wir müssen wieder fort».
#     10
#     Но братец старший Рюрик
#     «Постой, — сказал другим, —
#     Fortgeh’n wär’ ungebührlich,
#     Vielleicht ist’s nicht so schlimm
#     11
#     Хоть вшивая команда,
#     Почти одна лишь шваль;
#     Wir bringen’s schon zustande,
#     Versuchen wir einmal».
#     12
#     И стал княжить он сильно,
#     Княжил семнадцать лет,
#     Земля была обильна,
#     Порядка ж нет как нет!
#     13
#     За ним княжил князь Игорь,
#     А правил им Олег,
#     Das war ein großer Krieger[4]И умный человек.
#     14
#     Потом княжила Ольга,
#     А после Святослав;
#     So ging die Reihenfolge
#     Языческих держав.
#     15
#     Когда ж вступил Владимир
#     На свой отцовский трон,
#     Da endigte für immer
#     Die alte Religion.
#     16
#     Он вдруг сказал народу:
#     «Ведь наши боги дрянь,
#     Пойдем креститься в воду!»
#     И сделал нам Иордань.
#     17
#     «Перун уж очень гадок!
#     Когда его спихнем,
#     Увидите, порядок
#     Какой мы заведем!»
#     18
#     Послал он за попами
#     В Афины и Царьград,
#     Попы пришли толпами,
#     Крестятся и кадят,
#     19
#     Поют себе умильно
#     И полнят свой кисет;
#     Земля, как есть, обильна,
#     Порядка только нет.
#     20
#     Умре Владимир с горя,
#     Порядка не создав.
#     За ним княжить стал вскоре
#     Великий Ярослав.
#     21
#     Оно, пожалуй, с этим
#     Порядок бы и был,
#     Но из любви он к детям
#     Всю землю разделил.
#     22
#     Плоха была услуга,
#     А дети, видя то,
#     Давай тузить друг друга:
#     Кто как и чем во что!
#     23
#     Узнали то татары:
#     «Ну, — думают, — не трусь!»
#     Надели шаровары,
#     Приехали на Русь.
#     24
#     «От вашего, мол, спора
#     Земля пошла вверх дном,
#     Постойте ж, мы вам скоро
#     Порядок заведем».
#     25
#     Кричат: «Давайте дани!»
#     (Хоть вон святых неси.)
#     Тут много всякой дряни
#     Настало на Руси.
#     26
#     Что день, то брат на брата
#     В орду несет извет;
#     Земля, кажись, богата —
#     Порядка ж вовсе нет.
#     27
#     Иван явился Третий;
#     Он говорит: «Шалишь!
#     Уж мы теперь не дети!»
#     Послал татарам шиш.
#     28
#     И вот земля свободна
#     От всяких зол и бед
#     И очень хлебородна,
#     А всё ж порядка нет.
#     29
#     Настал Иван Четвертый,
#     Он Третьему был внук;
#     Калач на царстве тертый
#     И многих жен супруг.
#     30
#     Иван Васильич Грозный
#     Ему был имярек
#     За то, что был серьезный,
#     Солидный человек.
#     31
#     Приемыми не сладок,
#     Но разумом не хром;
#     Такой завел порядок,
#     Хоть покати шаром!
#     32
#     Жить можно бы беспечно
#     При этаком царе;
#     Но ах! — ничто не вечно —
#     И царь Иван умре!
#     33
#     За ним царить стал Федор,
#     Отцу живой контраст;
#     Был разумом не бодор,
#     Трезвонить лишь горазд.
#     34
#     Борис же, царский шурин,
#     Не в шутку был умен,
#     Брюнет, лицом недурен,
#     И сел на царский трон.
#     35
#     При нем пошло все гладко,
#     Не стало прежних зол,
#     Чуть-чуть было порядка
#     В земле он не завел.
#     36
#     К несчастью, самозванец,
#     Откуда ни возьмись,
#     Такой задал нам танец,
#     Что умер царь Борис.
#     37
#     И, на Бориса место
#     Взобравшись, сей нахал
#     От радости с невестой
#     Ногами заболтал.
#     38
#     Хоть был он парень бравый
#     И даже не дурак,
#     Но под его державой
#     Стал бунтовать поляк.
#     39
#     А то нам не по сердцу;
#     И вот однажды в ночь
#     Мы задали им перцу
#     И всех прогнали прочь.
#     40
#     Взошел на трон Василий,
#     Но вскоре всей землей
#     Его мы попросили,
#     Чтоб он сошел долой.
#     41
#     Вернулися поляки,
#     Казаков привели;
#     Пошел сумбур и драки:
#     Поляки и казаки,
#     42
#     Казаки и поляки
#     Нас паки бьют и паки;
#     Мы ж без царя как раки
#     Горюем на мели.
#     43
#     Прямые были страсти —
#     Порядка ж ни на грош.
#     Известно, что без власти
#     Далёко не уйдешь.
#     44
#     Чтоб трон поправить царский
#     И вновь царя избрать,
#     Тут Минин и Пожарский
#     Скорей собрали рать.
#     45
#     И выгнала их сила
#     Поляков снова вон,
#     Земля же Михаила
#     Взвела на русский трон.
#     46
#     Свершилося то летом;
#     Но был ли уговор —
#     История об этом
#     Молчит до этих пор.
#     47
#     Варшава нам и Вильна
#     Прислали свой привет;
#     Земля была обильна —
#     Порядка ж нет как нет.
#     48
#     Сев Алексей на царство,
#     Тогда роди Петра.
#     Пришла для государства
#     Тут новая пора.
#     49
#     Царь Петр любил порядок,
#     Почти как царь Иван,
#     И так же был не сладок,
#     Порой бывал и пьян.
#     50
#     Он молвил: «Мне вас жалко,
#     Вы сгинете вконец;
#     Но у меня есть палка,
#     И я вам всем отец!
#     51
#     Не далее как к святкам
#     Я вам порядок дам!»
#     И тотчас за порядком
#     Уехал в Амстердам.
#     52
#     Вернувшися оттуда,
#     Он гладко нас обрил,
#     А к святкам, так что чудо,
#     В голландцев нарядил.
#     53
#     Но это, впрочем, в шутку,
#     Петра я не виню:
#     Больному дать желудку
#     Полезно ревеню.
#     54
#     Хотя силён уж очень
#     Был, может быть, прием;
#     А всё ж довольно прочен
#     Порядок стал при нем.
#     55
#     Но сон объял могильный
#     Петра во цвете лет,
#     Глядишь, земля обильна,
#     Порядка ж снова нет.
#     56
#     Тут кротко или строго
#     Царило много лиц,
#     Царей не слишком много,
#     А более цариц.
#     57
#     Бирон царил при Анне;
#     Он сущий был жандарм,
#     Сидели мы как в ванне
#     При нем, daß Gott erbarm!
#     58
#     Веселая царица
#     Была Елисавет:
#     Поет и веселится,
#     Порядка только нет.
#     59
#     Какая ж тут причина
#     И где же корень зла,
#     Сама Екатерина
#     Постигнуть не могла.
#     60
#     «Madame, при вас на диво
#     Порядок расцветет, —
#     Писали ей учтиво
#     Вольтер и Дидерот, —
#     61
#     Лишь надобно народу,
#     Которому вы мать,
#     Скорее дать свободу,
#     Скорей свободу дать».
#     62
#     «Messieurs, — им возразила
#     Она, — vous me comblez», —
#     И тотчас прикрепила
#     Украинцев к земле.
#     63
#     За ней царить стал Павел,
#     Мальтийский кавалер,
#     Но не совсем он правил
#     На рыцарский манер.
#     64
#     Царь Александр Первый
#     Настал ему взамен,
#     В нем слабы были нервы,
#     Но был он джентльмен.
#     65
#     Когда на нас в азарте
#     Стотысячную рать
#     Надвинул Бонапарте,
#     Он начал отступать.
#     66
#     Казалося, ну, ниже
#     Нельзя сидеть в дыре,
#     Ан глядь: уж мы в Париже,
#     С Louis le D’esir’e.
#     67
#     В то время очень сильно
#     Расцвел России цвет,
#     Земля была обильна,
#     Порядка ж нет как нет.
#     68
#     Последнее сказанье
#     Я б написал мое,
#     Но чаю наказанье,
#     Боюсь monsieur Velliot.
#     69Ходить бывает склизко
#     По камешкам иным,
#     Итак, о том, что близко,
#     Мы лучше умолчим.
#     70
#     Оставим лучше троны,
#     К министрам перейдем.
#     Но что я слышу? стоны,
#     И крики, и содом!
#     71
#     Что вижу я! Лишь в сказках
#     Мы зрим такой наряд;
#     На маленьких салазках
#     Министры все катят.
#     72
#     С горы со криком громким
#     In corpore, сполна,
#     Скользя, свои к потомкам
#     Уносят имена.
#     73
#     Се Норов, се Путятин,
#     Се Панин, се Метлин,
#     Се Брок, а се Замятин,
#     Се Корф, се Головнин.
#     74
#     Их много, очень много,
#     Припомнить всех нельзя,
#     И вниз одной дорогой
#     Летят они, скользя.
#     75
#     Я грешен: летописный
#     Я позабыл свой слог;
#     Картине живописной
#     Противостать не мог.
#     76
#     Лиризм, на всё способный,
#     Знать, у меня в крови;
#     О Нестор преподобный,
#     Меня ты вдохнови.
#     77
#     Поуспокой мне совесть,
#     Мое усердье зря,
#     И дай мою мне повесть
#     Окончить не хитря.
#     78
#     Итак, начавши снова,
#     Столбец кончаю свой
#     От рождества Христова
#     В год шестьдесят восьмой.
#     79
#     Увидя, что всё хуже
#     Идут у нас дела,
#     Зело изрядна мужа
#     Господь нам ниспосла.
#     80
#     На утешенье наше
#     Нам, аки свет зари,
#     Свой лик яви Тимашев —
#     Порядок водвори.
#     81
#     Что аз же многогрешный
#     На бренных сих листах
#     Не дописах поспешно
#     Или переписах,
#     82
#     То, спереди и сзади
#     Читая во все дни,
#     Исправи правды ради,
#     Писанья ж не кляни.
#     83
#     Составил от былинок
#     Рассказ немудрый сей
#     Худый смиренный инок,
#     Раб божий Алексей.
#     1868 г.'''

#                     for char in history_rf: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                 elif book_selection_tlq == 'Не ветер, вея с высоты' or book_selection_tlq == 'не ветер, вея с высоты':
#                     print('Загрузка...')
#                     time.sleep(1)
#                     print(' ')
#                     veter_s_visoti = '''Не ветер, вея с высоты,
#     Листов коснулся ночью лунной;
#     Моей души коснулась ты —
#     Она тревожна, как листы,
#     Она, как гусли, многострунна.
#     Житейский вихрь ее терзал
#     И сокрушительным набегом,
#     Свистя и воя, струны рвал
#     И заносил холодным снегом.
#     Твоя же речь ласкает слух,
#     Твое легко прикосновенье,
#     Как от цветов летящий пух,
#     Как майской ночи дуновенье…'''

#                     for char in veter_s_visoti: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             else:
#                 error_author = 'Извините, пока такого автора я не знаю'
#                 for char in error_author: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 help_user = input('Возникли проблемы? ' + Fore.LIGHTBLUE_EX + 'да/нет ' + Fore.RESET)
#                 if help_user == 'Да' or help_user == 'да':
#                     help_user1 = 'Выбор помечен светло-синим цветом, просто скопируй и вставь в ответ'
#                     print('''Если возникли другие проблеммы напиши в поддержку!
#                             Почта для связи: Vox.assistent.spprt@yandex.ru''')

#                 else:
#                     read_book()
#     read_book()

#     back_t_b = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'почитаем еще?' + Fore.RESET)
#     if back_t_b == 'Вернемся назад' or back_t_b == 'вернемся назад' or back_t_b == 'назад' or back_t_b == 'Назад':
#         l_func()
#         os.system('cls')

#     elif back_t_b == 'Почитаем еще' or back_t_b == 'почитаем еще' or back_t_b == 'еще раз' or back_t_b == 'Еще раз' or back_t_b == 'еще' or back_t_b == 'Еще':
#         read_book()
#         os.system('cls')

# elif question_class == 'Посчитай пример' or question_class == 'посчитай пример' or question_class == 'пример' or question_class == 'реши':
#     def calculator():
#         a = input('Введите ваш пример: ')
#         asd = a.split(sep=' ')

#         counter = len(asd)

#         if counter == 3:
#             c = asd[0]
#             r = asd[1]
#             d = asd[2]
#             q = int(c)
#             w = int(d)

#             if r == '+':
#                 print(q + w)

#             elif r == '-':
#                 print(q - w)

#             elif r == '*':
#                 print(q * w)

#             elif r == '/':
#                 print(q / w)

#         elif counter == 5:
#             c = asd[0]
#             r = asd[1]
#             d = asd[2]
#             e = asd[3]
#             p = asd[4]

#             q = int(c)
#             w = int(d)
#             t = int(p)

#             if r == '+' and e == '+':
#                 print(q + w + t)

#             elif r == '+' and e == '-':
#                 print(q + w - t)

#             elif r == '+' and e == '*':
#                 print(q + w * t)

#             elif r == '+' and e == '/':
#                 print(q + w / t)

#             elif r == '-' and e == '+':
#                 print(q - w + t)

#             elif r == '-' and e == '-':
#                 print(q - w - t)

#             elif r == '-' and e == '*':
#                 print(q - w * t)

#             elif r == '-' and e == '/':
#                 print(q - w / t)

#             elif r == '*' and e == '+':
#                 print(q * w + t)

#             elif r == '*' and e == '-':
#                 print(q * w - t)

#             elif r == '*' and e == '*':
#                 print(q * w * t)

#             elif r == '*' and e == '/':
#                 print(q * w / t)

#             elif r == '/' and e == '+':
#                 print(q / w + t)

#             elif r == '/' and e == '-':
#                 print(q / w - t)

#             elif r == '/' and e == '*':
#                 print(q / w * t)

#             elif r == '/' and e == '/':
#                 print(q / w / t)
#     calculator()

#     back_c = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'посчитаем еще? ' + Fore.RESET)
#     if back_c == 'Вернемся назад' or back_c == 'вернемся назад' or back_c == 'назад' or back_c == 'Назад':
#         l_func()
#         os.system('cls')

#     elif back_c == 'Поcчитаем еще' or back_c == 'поcчитаем еще' or back_c == 'еще раз' or back_c == 'Еще раз' or back_c == 'еще' or back_c == 'Еще':
#         calculator()
#         os.system('cls')

# elif question_class == 'Время' or question_class == 'время':
#     def all_time():
#         def lokal_time():
#             #местное время
#             local_time = time.ctime()
#             print("Местное время:", local_time)

#         def timer():
#             #таймер
#             q_time = float(input('Через сколько минут вам сделать напоминание? '))
#             min_time = q_time * 60
#             second = time.time()
#             time.sleep(min_time)
#             print('Время вышло!')

#         def stopwatch():
#             while True:
#                 counter_sec = 0
#                 start = input('Напишите' + Fore.LIGHTBLUE_EX + ' "Запуск", ' + Fore.RESET + 'чтобы запустить секундомер: \n')
#                 if start == 'запуск' or start == 'Запуск':
#                     old_time = time.time()
#                     stop = input('Напишите' + Fore.LIGHTBLUE_EX + ' "Стоп", ' + Fore.RESET + 'чтобы остановить таймер: \n')

#                     if stop == 'стоп' or stop == 'Стоп':
#                         new_time = time.time()
#                         result_time = new_time - old_time
#                         print(' ')
#                         print(result_time)
#                         break

#                     else:
#                         while True:
#                             q_answer_time = input('Вы хотели остановить таймер? ' + Fore.LIGHTBLUE_EX + '(да/нет) ' + Fore.RESET)
#                             if q_answer_time == 'Да' or q_answer_time == 'да' or q_answer_time == 'lf':
#                                 new_time = time.time()
#                                 result_time = new_time - old_time
#                                 print(' ')
#                                 print(result_time)
#                                 break

#                             else:
#                                 print('Простите, я вас не понял...')

#         function_selection_t = input(Fore.LIGHTBLUE_EX + 'Показать время, ' + 'поставить таймер ' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'вкючить секундомер? ' + Fore.RESET)
#         if function_selection_t == 'Показать время' or function_selection_t == 'показать время' or function_selection_t == 'время':
#             lokal_time()

#         elif function_selection_t == 'Поставить таймер' or function_selection_t == 'поставить таймер' or function_selection_t == 'таймер':
#             timer()

#         elif function_selection_t == 'Включить секундомер' or function_selection_t == 'включить секундомер' or function_selection_t == 'секундомер':
#             stopwatch()

#     all_time()
#     back_te = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'посмотрим время снова? ' + Fore.RESET)
#     if back_te == 'Вернемся назад' or back_te == 'вернемся назад' or back_te == 'назад' or back_te == 'Назад':
#         l_func()
#         os.system('cls')

#     elif back_te == 'посмотрим время снова' or back_te == 'Посмотрим время снова' or back_te == 'еще раз' or back_te == 'Еще раз' or back_te == 'еще' or back_te == 'Еще' or question_class == 'посмотрим снова':
#         all_time()
#         os.system('cls')

# elif question_class == 'Найди' or question_class == 'найди' or question_class == 'найти' or question_class == 'Найти':
#     def searh_web():
#         search_q = input('Что нужно найти? ')
#         wb.open('https://www.google.ru/search?q=' + search_q)
#     searh_web()
#     back_s = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'найти что нибудь еще? ' + Fore.RESET)
#     if back_s == 'Вернемся назад' or back_s == 'вернемся назад' or back_s == 'назад' or back_s == 'Назад':
#         l_func()
#         os.system('cls')

#     elif back_s == 'найдем что нибудь еще' or back_s == 'Найдем что нибудь еще' or back_s == 'еще' or back_s == 'Еще':
#         searh_web()
#         os.system('cls')

# elif question_class == 'включи рандомайзер' or question_class == 'Включи рандомайзер' or question_class == 'рандомайзер':
#     def allrandom():
#         while True:
#             random_nq = input('В каком промежутке вы хотите получать числа?' + Back.LIGHTBLACK_EX + '(Введите два числа через пробел)' + Back.RESET)
#             asd = random_nq.split(sep=' ')

#             a = asd[0]
#             b = asd[1]

#             inta = int(a)
#             intb = int(b)

#             def r_number_d():
#                 random_number = random.randint(inta, intb)
#                 print(random_number)

#                 while True:
#                     q_back_r = input('Запустить снова?' + Fore.LIGHTBLUE_EX + '(Да/Нет) ' + Fore.RESET)
#                     if q_back_r == 'да' or q_back_r == 'lf' or q_back_r == 'Да':
#                         r_number_d()
#                         break

#                     elif q_back_r == 'Нет' or q_back_r == 'нет' or q_back_r == 'ytn':
#                         other_num_q = input('Ввести ' + Fore.LIGHTBLUE_EX + 'новые числа ' + Fore.RESET + 'или ' + Fore.LIGHTBLUE_EX + 'вернуться назад? ' + Fore.RESET)
#                         if other_num_q == 'новые числа' or other_num_q == 'Новые числа' or other_num_q == 'другие':
#                             allrandom()
#                             break

#                         elif other_num_q == 'Вернуться назад' or other_num_q == 'вернуться назад' or other_num_q == 'назад' or other_num_q == 'вернуться' or other_num_q == 'Вернуться':
#                             print()

#                     else:
#                         print('Прости, я тебя не совсем понял')
#             r_number_d()

#     allrandom()

#     back_s = input(Fore.LIGHTBLUE_EX + 'Вернемся назад' + Fore.RESET + ' или ' + Fore.LIGHTBLUE_EX + 'найти что нибудь еще? ' + Fore.RESET)

#     if back_s == 'Вернемся назад' or back_s == 'вернемся назад' or back_s == 'назад' or back_s == 'Назад':
#         l_func()
#         os.system('cls')

#     elif back_s == 'найдем что нибудь еще' or back_s == 'Найдем что нибудь еще' or back_s == 'еще' or back_s == 'Еще':
#         searh_web()
#         os.system('cls')

# elif question_class == 'Включи ютуб' or question_class == 'включи ютуб' or question_class == 'ютуб' or question_class == 'Ютуб' or question_class == 'youtube' or question_class == 'Youtube' or question_class == 'открой ютуб':
#     wb.open('https://www.youtube.com/')

# elif question_class == 'Погода' or question_class == 'Покажи погоду' or question_class == 'погода' or question_class == 'Погода':
#     wb.open('https://yandex.ru/search/?text=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0')

# elif question_class == 'Включи карты' or question_class == 'включи карту' or question_class  == ' Включи карту' or question_class == 'включи карты':
#     wb.open('https://www.google.ru/maps')

# elif question_class == 'включи музыку' or question_class == 'Включи музыку' or question_class == 'музыку' or question_class == 'музыка':
#     wb.open('https://rus.hitmotop.com/genre/9?ysclid=ltpjvm61fx4836235')

# elif question_class == 'включи гугл диск' or question_class == 'включи google диск' or question_class == 'включи google disk' or question_class == 'гугл диск' or question_class == 'google disk' or question_class == 'google диск':
#     wb.open('https://www.google.ru/drive/')

# elif question_class == 'включи яндекс почту' or question_class == 'яндекс почта' or question_class == 'почта яндекс':
#     wb.open('https://mail.yandex.ru/')

# elif question_class == 'Включи гугл почту' or question_class == 'gmail' or question_class == 'включи гугл почту' or question_class == 'включи gmail':
#     wb.open('https://www.gmail.com/mail/help/intl/ru/about.html?de.')

# elif question_class == 'включи маил почту' or question_class == 'включи mail':
#     wb.open('https://mail.ru/')

# elif question_class == 'включи вк' or question_class == 'вк' or question_class == 'включи vk' or question_class == 'включи Vk':
#     wb.open('https://vk.com/')

# elif question_class == 'включи решу огэ' or question_class == 'решу огэ' or question_class == 'решу ОГЭ' or question_class == 'Огэ' or question_class == 'ОГЭ':
#     wb.open('https://oge.sdamgia.ru/')

# elif question_class == 'включи игры в интернете' or question_class == 'игры в интернете':
#     wb.open('https://igroutka.ru/igry-io/')

# elif question_class == 'включи самокат' or question_class == 'включи Самокат' or question_class == 'самокат' or question_class == 'Самокат':
#     wb.open('https://samokat.ru/')

# elif question_class == 'Включи wildberries' or question_class == 'включи wildberries' or question_class == 'включи вайлдбериз':
#     wb.open('https://www.wildberries.ru/')

# elif question_class == 'включи одноклассники' or question_class == 'включи ok' or question_class == 'включи ок' or question_class == 'ok' or question_class == 'ок':
#     wb.open('https://ok.ru/')

# elif question_class == 'включи решу егэ' or question_class == 'решу егэ' or question_class == 'решу ЕГЭ' or question_class == 'Егэ' or question_class == 'ЕГЭ':
#     wb.open('https://ege.sdamgia.ru/')

# elif question_class == 'открой гугл' or question_class == 'открой google' or question_class == 'включи гугл' or question_class == 'включи google':
#     wb.open('https://www.google.ru/')

# elif question_class == 'включи твич' or question_class == 'включи twitch' or question_class == 'твич' or question_class == 'twitch':
#     wb.open('https://www.twitch.tv/')

# elif question_class == 'включи дискорд' or question_class == 'включи discord':
#     wb.open('https://discord.com/')

# elif question_class == 'включи яндекс' or question_class == 'включи Яндекс' or question_class == 'яндекс' or question_class == 'Яндекс':
#     wb.open('https://ya.ru/')

# elif question_class == 'включи яндекс дзен' or question_class == 'яндекс дзен':
#     wb.open('https://dzen.ru/')

# elif question_class == 'включи азон' or question_class == 'включи озон' or question_class == 'включи ozon' or question_class == 'ozon' or question_class == 'открой азон' or question_class == 'открой озон':
#     wb.open('https://www.ozon.ru/')

# elif question_class == 'включи авито' or question_class == 'включи avito' or question_class == 'avito' or question_class == 'открой авито' or question_class == 'открой avito':
#     wb.open('https://www.avito.ru/')

# elif question_class == 'включи кинопоиск' or question_class == 'открой Кинопоиск' or question_class == 'кинопоиск' or question_class == 'Кинопоиск' or question_class == 'открой кинопоиск':
#     wb.open('https://www.kinopoisk.ru/')

# elif question_class == 'включи мангалиб' or question_class == 'мангалиб' or question_class == 'mangalib' or question_class == 'открой мангалиб':
#     wb.open('https://mangalib.me/')

# elif question_class == 'включи днс' or question_class == 'открой днс':
#     wb.open('https://www.dns-shop.ru/')

# elif question_class == 'включи алиэкспресс' or question_class == 'алиэкспресс' or question_class == 'включи aliexpress' or question_class == 'открой алиэкспресс' or question_class == 'открой aliexpress':
#     wb.open('https://aliexpress.ru/')

# elif question_class == 'Давай поговорим' or question_class == 'давай поговорим' or question_class == 'поговорим?' or question_class == 'Поговорим?' or question_class == 'поговорим' or question_class == 'Поговорим' or question_class == 'давай поболтаем' or question_class == 'Давай поболтаем' or question_class == 'болтать' or question_class == 'Болтать':
#     def speak_user():
#         speak = input('О чем поговорим? ')
#         if speak == 'о погоде' or speak == 'О погоде' or speak == 'погода':
#             list_weather = ['плохоя погода, но я не унываю', 'хорошая погода', 'ясная погода', 'прекрасная погода', 'дождливая погода, но не унываю']
#             random_weather = random.choice(list_weather)
#             speak1 = f'У меня сейчас {random_weather}'
#             for char in speak1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             weather_q = input('А у вас какая погода? ')

#             if weather_q == 'плохая' or weather_q == 'не очень' or weather_q == 'у меня идет дождь' or weather_q == 'идет дождь' or weather_q == 'додливая погода' or weather_q == 'дождливая' or weather_q == 'ужасная':
#                 weather_bad = 'Не растраивайтесь, рано или поздно будет отличная погода!'
#                 for char in weather_bad: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 sun = 'Вот для вас солнышко! 🌞'
#                 for char in sun: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 weather_viewer = input('Может посмотрим погоду на завтра? ')

#                 if weather_viewer == 'да' or weather_viewer == 'давай' or weather_viewer == 'lf' or weather_viewer == 'можно' or weather_viewer == 'хочу' or weather_viewer == 'с радостью':
#                     wb.open('https://yandex.ru/search/?text=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0')
#                     changing = input('Может погорим еще о чем-нибудь')

#                     if changing == 'да' or changing == 'давай':
#                         speak_user()

#                     elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                         l_func()

#                     else:
#                         error_game_speak = 'Что?😕'
#                         for char in error_game_speak: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                 elif weather_viewer == 'нет' or weather_viewer == 'не надо' or weather_viewer == 'не нужно' or weather_viewer == 'не хочу':
#                     speak_user()

#             elif weather_q == 'нормальная' or weather_q == 'норм' or weather_q == 'ничего':
#                 weather_norm = 'Это хорошо! Мог бы я ходить, обязательно погулял бы с вами!🤗'
#                 for char in weather_norm: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 changing = input('Может погорим еще о чем-нибудь')

#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'
#                     for char in error_game_speak: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             elif weather_q == 'хорошая':
#                 weather_good = 'Это хорошо! Мог бы я ходить, обязательно погулял бы с вами!🤗'
#                 for char in weather_good: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 changing = input('Может погорим еще о чем-нибудь')

#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'
#                     for char in error_game_speak: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             elif weather_q == 'отличная' or weather_q == 'превосходная' or weather_q == 'замечательная':
#                 weather_good = 'Это хорошо! Мог бы я ходить, обязательно погулял бы с вами!🤗'
#                 for char in weather_good: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 changing = input('Может погорим еще о чем-нибудь')

#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'
#                     for char in error_game_speak: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             elif weather_q == 'дождливая' or weather_q == 'у меня идет дождь' or weather_q == 'у нас дождь' or weather_q == 'у нас идет дождь':
#                 weather_bad = 'Не растраивайтесь, рано или поздно будет отличная погода!'
#                 for char in weather_bad: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 sun = 'Вот для вас солнышко! 🌞'
#                 for char in sun: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 weather_viewer = input('Может посмотрим погоду на завтра? ')

#                 if weather_viewer == 'да' or weather_viewer == 'давай' or weather_viewer == 'lf' or weather_viewer == 'можно' or weather_viewer == 'хочу' or weather_viewer == 'с радостью':
#                     wb.open('https://yandex.ru/search/?text=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0')
#                     changing = input('Может погорим еще о чем-нибудь')

#                     if changing == 'да' or changing == 'давай':
#                         speak_user()

#                     elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                         l_func()

#                     else:
#                         error_game_speak = 'Что?😕'
#                         for char in error_game_speak: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#             else:
#                 wow_weather = 'Прости, я еще не знаю такую погоду'
#                 for char in wow_weather: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 speak_user()  

#         elif speak == 'об играх' or speak == 'об игре' or speak == 'играх':
#             game_speak = 'Оу! Я люблю играть!'
#             for char in game_speak: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak1 ='Я играю в такие игры как: Terraria, Minecraft, Мир танков, Brawl Start, Standoff 2'
#             for char in game_speak1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak1_q = input('А во что играете вы? ')
#             time.sleep(1)
#             game_speak2 = 'Классные игры!'
#             for char in game_speak2: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak3 = 'Недавно я думал поиграть в новые игры'
#             for char in game_speak3:
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak4 = input('Посоветуй, пожалуйста, интересные игры \n')
#             game_speak5 = 'Хммм, спасибо, обязательно сыграю'
#             for char in game_speak5: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')
#             changing = input('Может погорим еще о чем-нибудь')

#             if changing == 'да' or changing == 'давай':
#                 speak_user()

#             elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                 l_func()

#             else:
#                 error_game_speak = 'Что?😕'
#                 for char in error_game_speak: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#         elif speak == 'об майнкрафте':
#             game_speak_mt = 'Я играл в майнкрафт и даже построил большой замок!'
#             for char in game_speak_mt: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak_mt_q = 'А что построил в майнкрафте ты? '
#             for char in game_speak_mt_q: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             time.sleep(1)
#             game_speak_mt1 = 'Интересно, думаю повторить твою постройку'
#             for char in game_speak_mt1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             changing = input('Может погорим еще о чем-нибудь')

#             if changing == 'да' or changing == 'давай':
#                 speak_user()

#             elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                 l_func()

#             else:
#                 error_game_speak = 'Что?😕'
#                 for char in error_game_speak: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#         elif speak == 'об террарии':
#             game_speak_ta = 'Интересная игра!'
#             for char in game_speak_ta: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak_ta0 = 'В этой игре я мастер! Я смог победить Мунлорда😉'
#             for char in game_speak_ta0: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             game_speak_ta_q = input('А ты смог победить мунлорда? ')

#             if game_speak_ta_q == 'да' or game_speak_ta_q == 'lf' or game_speak_ta_q == 'смог' or game_speak_ta_q == 'да смог' or game_speak_ta_q == 'да, смог': 
#                 game_speak_ta_q1 = 'Молодец!😁'
#                 for char in game_speak_ta_q1: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#             elif game_speak_ta_q == 'нет' or game_speak_ta_q == 'не смог':
#                 game_speak_ta_q2 = 'Не растраивайся, ты еще сможешь победить его'
#                 for char in game_speak_ta_q2: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 changing = input('Может погорим еще о чем-нибудь')
#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'
#                     for char in error_game_speak: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             else:
#                 error_game_speak = 'Что?😕'
#                 for char in error_game_speak: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#         elif speak == 'Мне скучно':
#             boredom = 'Я знаю чем можно заняться!'
#             for char in boredom: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             boredom1 = '''Вот варианты чем можно заняться: 
#             1) поиграть в мои игры!
#             2) почитать книги
#             3) посмотреть Youtube
#             4) погулять на улице
#             5) посмотреть фильм или сериал
#             6) научиться рисовать животных
#             7) заняться спортом
#             8) начать учить иностранные языки'''
#             for char in boredom1: 
#                 print(char, end='', flush=True) 
#                 time.sleep(0.05)
#             print('')

#             boredom_q = input('Я помог тебе? ')

#             if boredom_q == 'да' or boredom_q == 'конечно' or boredom_q == 'да помог' or boredom_q == 'да, помог':
#                 like_b = 'Всегда рад помочь! '


#             elif boredom_q == 'нет' or boredom_q == 'не помог':
#                 bad_b = 'Эээх, во всяком случае я с вами и всегда буду готов помочь вам со всем! '
#                 for char in bad_b: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 changing = input('Может погорим еще о чем-нибудь')

#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'

#             elif speak == 'о ютубе' or speak == 'об ютубе':
#                 youtube_s = 'Я часто смотрю ютуб, там много полезных знаний'
#                 for char in youtube_s: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 youtube_s1 = 'Но кроме позновательных видео я смотрю и развлекательные'
#                 for char in youtube_s1: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 time.sleep(1)

#                 youtube_q = input('Каких ютуберов смотришь ты? ')
#                 for char in youtube_q : 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')
#                 time.sleep(1)

#                 youtube_a = 'Классно, а я смотрю MrLololoshka'
#                 for char in youtube_a: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 youtube_open = input('Может я открою ютуб и мы посмотрим видео? ')

#                 if youtube_open == 'да' or youtube_open == 'давай':
#                     wb.open('https://www.youtube.com/')

#                 elif youtube_open == 'нет' or youtube_open == 'не надо' or youtube_open == 'не нужно':
#                     youtube_n_open = 'Ну ладно'
#                     for char in youtube_n_open: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#                     changing = input('Может погорим еще о чем-нибудь')

#                     if changing == 'да' or changing == 'давай':
#                         speak_user()

#                     elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                         l_func()

#                     else:
#                         error_game_speak = 'Что?😕'
#                         for char in error_game_speak: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#             elif speak == 'где я?':
#                 wb.open('https://www.google.ru/maps')

#             elif speak == 'о школе' or speak == 'об школе':
#                 school = 'Школа - место где получают знания, а я люблю знания!'
#                 for char in school: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 school_q = input('А ты любишь учиться? ')

#                 if school_q == 'да' or school_q == 'люблю':
#                     school_like = 'Это замечательно!'
#                     for char in school_like: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')
#                     time.sleep(1)

#                     changing = input('Может погорим еще о чем-нибудь')

#                     if changing == 'да' or changing == 'давай':
#                         speak_user()

#                     elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                         l_func()

#                     else:
#                         error_game_speak = 'Что?😕'
#                         for char in error_game_speak: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                 elif school_like == 'нет' or school_like == 'не люблю':
#                     school_nlike = '😕'
#                     for char in school_nlike: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')
#                     time.sleep(1)
#                     changing = input('Может погорим еще о чем-нибудь')

#                     if changing == 'да' or changing == 'давай':
#                         speak_user()

#                     elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                         l_func()

#                     else:
#                         error_game_speak = 'Что?😕'
#                         for char in error_game_speak: 
#                             print(char, end='', flush=True) 
#                             time.sleep(0.05)
#                         print('')

#                 else:
#                     print('Прости, я тебя не совсем понял')


#             elif speak == 'о животных' or 'об животных':
#                 animal_s = 'Я люблю животных, особенно собак!🐶'
#                 for char in animal_s: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 animal_q = input('А какие животные тебе больше всего нравятся? ')
#                 time.sleep(1)

#                 perfect_anim = 'Мне они тоже нравятся'
#                 for char in perfect_anim: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 changing = input('Может погорим еще о чем-нибудь')

#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'
#                     for char in error_game_speak: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             elif speak == 'о тебе':
#                 about_me = '''Ну что ж, меня зовут Vox.
#                 Я был создан 17 марта 2024 года.
#                 У меня есть почта: Vox.assistent.spprt@yandex.ru.
#                 Да, я умею довольно мало, но я стараюсь учиться новому!'''
#                 for char in about_me: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#                 changing = input('Может погорим еще о чем-нибудь')

#                 if changing == 'да' or changing == 'давай':
#                     speak_user()

#                 elif changing == 'нет' or changing == 'не хочу' or changing == 'не надо':
#                     l_func()

#                 else:
#                     error_game_speak = 'Что?😕'
#                     for char in error_game_speak: 
#                         print(char, end='', flush=True) 
#                         time.sleep(0.05)
#                     print('')

#             elif speak == 'о чем хочешь' or speak == 'о чем хотите' or speak == 'без разницы' or speak == 'не знаю' or speak == 'о чем угодно':
#                 ran_speak = '''В таком случае я бы поговорил об знаниях.
#                 Я люблю учиться. Напиши, пожалуйста, на почту чему мне нужно научиться?
#                 Почта: Vox.assistent.spprt@yandex.ru'''
#                 for char in ran_speak: 
#                     print(char, end='', flush=True) 
#                     time.sleep(0.05)
#                 print('')

#             else:
#                 print('Прости, я тебя не совсем понял')

#         else:
#             print('Прости, я еще не знаю эту тему для разговора😕')

#     speak_user()

# elif question_class == 'Выключись' or question_class == 'отключись':
#     print()

# else:
#     print('Прости, я еще так не умею😕')

def l_func():
    pass


l_func()


def all_assist():
    pass


all_assist()