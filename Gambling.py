import random


def gamble_game():
    coins = 500  # Startbedrag aan munten
    wins = 0  # Totaal aantal overwinningen
    losses = 0  # Totaal aantal verliezen
    total_bets = 0  # Totaal ingezette bedragen

    print("Welkom bij het Nummer Gamble-spel!")  # Welkomstbericht
    print(f"Je begint met {coins} munten.")  # Laat het beginbedrag zien

    while True:
        if coins <= 0:  # Controleer of de speler nog munten heeft
            print("Je hebt geen munten meer! Spel afgelopen.")  # Einde van het spel
            break

        while True:
            # Vraag de speler om een inzet
            bet = int(input(f"Hoeveel wil je inzetten? (Je hebt {coins} munten): "))
            if 0 < bet <= coins:  # Controleer of de inzet geldig is
                break
            else:
                print(f"Ongeldige inzet! Voer een waarde in tussen 1 en {coins}.")  # Foutmelding

        player_number = int(input("Kies een nummer tussen 1 en 10: "))  # Vraag de speler om een nummer te kiezen

        if player_number < 1 or player_number > 10:  # Controleer of het gekozen nummer geldig is
            print("Ongeldig nummer! Kies een nummer tussen 1 en 10.")  # Foutmelding
            continue  # Ga opnieuw naar de start van de while-lus

        random_number = random.randint(1, 10)  # Genereer een willekeurig nummer
        print(f"Het willekeurige nummer is: {random_number}")  # Laat het willekeurige nummer zien

        # Jackpot-functie
        if player_number == random_number and random.random() < 0.1:  # 10% kans op jackpot
            jackpot_amount = 500  # Bepaal het jackpotbedrag
            coins += jackpot_amount  # Voeg jackpotbedrag toe aan munten
            print("JACKPOT! Je hebt de jackpot gewonnen!")  # Jackpotbericht
            print(f"Je hebt {jackpot_amount} munten gewonnen! Je huidige saldo is: {coins} munten.")
        elif player_number == random_number:  # Speler wint
            coins += bet  # Voeg inzetbedrag toe aan munten
            wins += 1  # Verhoog het aantal overwinningen
            print("Gefeliciteerd! Je wint!")  # Winbericht
            print(f"Je hebt {bet} munten gewonnen. Je huidige saldo is: {coins} munten.")
        else:  # Speler verliest
            coins -= bet  # Verlies de inzet
            losses += 1  # Verhoog het aantal verliezen
            total_bets += bet  # Voeg inzet toe aan totaal ingezette bedragen
            print("Sorry, je verliest. Meer geluk de volgende keer!")  # Verliesbericht
            print(f"Je hebt {bet} munten verloren. Je huidige saldo is: {coins} munten.")

            # Bonus na 3 opeenvolgende verliezen
            if losses % 3 == 0:  # Controleer of de speler 3 keer achter elkaar heeft verloren
                bonus = 135  # Bepaal het bonusbedrag
                coins += bonus  # Voeg bonusbedrag toe aan munten
                print(f"Je hebt een bonus van {bonus} munten ontvangen voor je verliesreeks!")  # Bonusbericht
                print(f"Je huidige saldo is: {coins} munten.")  # Laat het nieuwe saldo zien

        # Vraag de speler of hij opnieuw wil spelen
        play_again = input("Wil je opnieuw spelen? (ja/nee): ").strip().lower()
        if play_again != 'ja':  # Controleer de reactie van de speler
            print("Bedankt voor het spelen! Hier is je definitieve samenvatting:")  # Einde van het spel
            print(f"Eindbalans: {coins} munten.")  # Laat de eindbalans zien
            print(f"Totaal aantal overwinningen: {wins}, Totaal aantal verliezen: {losses}, Totaal ingezette bedragen: {total_bets} munten.")
            break  # Verlaat de while-loop en beëindig het spel


gamble_game()  # Start het spel
