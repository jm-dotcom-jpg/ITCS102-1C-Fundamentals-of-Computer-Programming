import os

print("\nWelcome to Mangago!!")
print("\nWhat genre do you prefer?")
print("Shonen - 1")
print("Josei - 2")
print("Seinen - 3")
genre_choice = input("\nSelect a number from the genre (1/2/3):")
os.system('cls')

if genre_choice == "1":
    genre1 = 'Shonen'
    print("You selected:", genre1)

    print("\nChoose a year")
    print("\n1999 - 2005  (a)")
    print("2005 - 2010  (b)")
    print("2010 - 2025 (c)")
    year = input("\nFrom what year?:").lower()
    os.system('cls')
    

    if year == 'a':
        print("\nWhat kind of series do you want? (long/short):")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year ",year, "and length", length)
            print("\nOne Piece")
            print("Naruto")
            print("Bleach")
            print("Prince of Tennis")
            print("Eyeshield")
            print("Zatchbell!")
            print("Shaman King")
            print("Hunter x Hunter")
            print("\nThank You for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year",year,"and length", length)
            print("\nFull Metal Alchemist")
            print("Hikaru No Go")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please restart and choose long/short.")

    elif year == 'b':
        print("\nWhat kind of series do you want? (long/short):")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year", year, "and length", length)
            print("Gintama")
            print("Fairy Tail")
            print("Katekyo Hitman reborn")
            print("Toriko")
            print("D.Gray-man")
            print("\nThank you for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year", year,"and length", length)
            print("\nDeathnote")
            print("Bakuman")
            print("Soul Eater")
            print("Beelzebub")
            print("Blue Exorcist")
            print("\nThank you for using Mangago!!!")

        else: 
            print("\nInvalid Selection. Please restart and choose long/short.")

    elif year == 'c':
        print("What kind of series do you want?(long/short)")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from year", year,"and length", length)
            print("\nMy Hero Academia")
            print("Black Clover")
            print("The Seven Deadly Sins")
            print("Fire Force")
            print("Tokyo Revengers")
            print("Jujutsu Kaisen")
            
        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year", year, "and length",length)
            print("\nDemon Slayer: Kimetsu no Yaiba")
            print("Dr.Stone")
            print("Chainsaw Man")
            print("Spy x Family")
            print("Mashle: Magic and Muscles")
            print("Kaiju No.8")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please restart and choose long/short.")

    else:
        print("\nInvalid Selection. Please restart and choose a/b/c")

elif genre_choice == "2":
    genre2 = 'Josei'
    print("You selected:",genre2)

    print("\nChoose a year")
    print("\n1999 - 2005  (a)")
    print("2005 - 2010  (b)")
    print("2010 - 2025 (c)")
    year = input("\nFrom what year?:").lower()
    os.system('cls')
    
    if year == 'a':
        print("\nWhat kind of series do you want? (long/short):")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year", year, "and length", length)
            print("\nNana")
            print("Tramps like Us (Kimi wa Pet)")
            print("Boys Be...L Co-op")
            print("\nThank you for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year", year, "and length", length)
            print("\nParadise Kiss")
            print("Hataraki Man")
            print("Happy Mania")
            print("Gokusen")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please restart and choose long/short.")

    elif year == 'b':
        print("\nWhat kind of series do you want? (long/short):")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year", year, "and length", length)
            print("\nHoney and Clover ")
            print("Nodame Cantabile")
            print("07 - Ghost")
            print("\nThank you for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year", year, "and length", length)
            print("\nButterflies, Flowers (Chou yo Hana yo)")
            print("Otomen")
            print("Himitsu - The Top Secret")
            print("A Thousand Years of Snow (Sennen no Yuki)")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please restart and choose long/short")

    elif year == 'c':
        print("What kind of series do you want?(long/short)")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from year", year,"and length", length)
            print("\nChihayafuru")
            print("Kurahagime (Princess Jellyfish)")
            print("Perfect World")
            print("\nThank you for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from year", year,"and length", length)
            print("\nTokyo Tarareba Girls")
            print("My Androgynous Boyfriend")
            print("Will You Marry Me Again If You Are Reborn?")
            print("An Incurable Case of Love (Koi wa Tsuzuku yo Doko Made mo)")
            print("A Condition Called Love (Hananoi-kun to Koi no Yamai)")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please Restart and choose long/short.")

    else:
        print("\nInvalid Selection. Please restart and enter a/b/c.")

elif genre_choice == "3":
    genre3 = 'Seinen'
    print("You selected:", genre3)

    print("\nChoose a year:")
    print("\n1999 - 2005 (a)")
    print("2005 - 2010 (b)")
    print("2010 - 2025 (c)")
    year = input("\nFrom what year?:").lower()
    os.system('cls')

    if year == 'a':
        print("\nWhat kind of series do you want?(long/short):")
        length = input("Enter the length that you want:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year",year,"and length",length)
            print("\nVagabond")
            print("20th Century Boys")
            print("Gantz")
            print("Berserk (continued)")
            print("Homunculus")
            print("\nThank you for using Mangago!!!")
            
        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year",year,"and length",length)
            print("\nMonster (ended 2001)")
            print("Planetes")
            print("Battle Royal")
            print("Old Boy")
            print("Ikigami: The Ultimate Limit")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please restart and choose long/short.")

    elif year == 'b':
        print("\nWhat kind of series do you want?(long/short):")
        length = input("Enter the length that you want:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year",year,"and length",length)
            print("\nVinland Saga")
            print("Zetman")
            print("Higanjima")
            print("Black Lagoon")
            print("\nThank you for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year",year,"and length",length)
            print("\nEden it's an Endless World! (Ended 2008)")
            print("Solanin")
            print("Bokurano")
            print("Mushishi (ended 2008)")
            print("Alive: The Final Evolution")
            print("\nThank you for using Mangago!!!")

        else:
            print("\nInvalid Selection. Please restart and choose long/short.")

    elif year == 'c':
        print("What kind of series do you want?(long/short)")
        length = input("Enter the length that you want.:").lower()
        os.system('cls')

        if length == 'long':
            print("\nHere are the manga recommendations for you from the year",year,"and length",length)
            print("\nKingdom")
            print("Golden Kamuy")
            print("Terra Formars")
            print("Ajin: Demi-Human")
            print("Blue Giant")
            print("\nThank you for using Mangago!!!")

        elif length == 'short':
            print("\nHere are the manga recommendations for you from the year",year,"and length",length)
            print("\nInuyashiki")
            print("Goodnight Punpun (Oyasumi Punpun)")
            print("I Am a Hero")
            print("Fire punch")
            print("Blood on the tracks (Chi no Wadachi)")
            print("\nThank you for using Mangago!!!")

        else:
            print("Invalid Selection. Please restart and choose long/short.")

    else:
        print("\nInvalid Selection, Please restart and choose a/b/c.")

else:
    print("\nInvalid Selection. Please restart and Enter 1/2/3")