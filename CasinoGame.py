import random

class CasinoGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.balance = 10000
        self.numbers = [str(i) for i in range(31)] + ['00']
        self.green_numbers = {'0', '00', '7'}

    def get_color(self, number):
        if number in self.green_numbers:
            return 'green'
        elif number.isdigit() and int(number) % 2 == 0:
            return 'black'
        else:
            return 'red'

    def place_bet(self, bet_type, bet_value, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return

        # Adjust probability for color bet to be close to 50-50
        if bet_type == 'color':
            outcome_color = random.choices(['red', 'black'], weights=[1, 1])[0]
            outcome = random.choice([n for n in self.numbers if self.get_color(n) == outcome_color])
        else:
            outcome = random.choice(self.numbers)

        outcome_color = self.get_color(outcome)

        print(f"The wheel spins... and lands on {outcome} ({outcome_color})!")

        if bet_type == 'number' and bet_value == outcome:
            winnings = amount * 100
        elif bet_type == 'color' and bet_value == outcome_color:
            winnings = amount * 1.2
        elif bet_type == 'green' and outcome_color == 'green':
            winnings = amount * 10000
        else:
            winnings = -amount

        self.balance += winnings
        if winnings > 0:
            print(f"Congratulations, {self.player_name}! You won ${winnings:.2f}.")
        else:
            print(f"Sorry, {self.player_name}, you lost ${-winnings:.2f}.")

        print(f"{self.player_name}, your current balance is: ${self.balance:.2f}")

        if self.balance <= 0:
            print("Ohh better luck next time!!")
            while True:
                add_funds = input(f"{self.player_name}, would you like to add more money to continue playing? (yes/no): ").lower()
                if add_funds in ['yes', 'no']:
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")

            if add_funds == 'yes':
                while True:
                    try:
                        additional_amount = int(input("Enter the amount to add: "))
                        if additional_amount > 0:
                            break
                        else:
                            print("Please enter a positive amount.")
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                self.balance += additional_amount
                print(f"Your new balance is: ${self.balance:.2f}")
            else:
                print(f"Thanks for playing, {self.player_name}! Goodbye.")
                exit()

    def start_game(self):
        print(f"Welcome to the Casino Game, {self.player_name}!")
        while True:
            print("\nChoose your bet type:")
            print("1. Bet on a number")
            print("2. Bet on a color (red/black)")
            print("3. Bet on green")

            while True:
                choice = input("Enter 1, 2, or 3: ")
                if choice in ['1', '2', '3']:
                    break
                print("Invalid choice. Please enter 1, 2, or 3.")

            if choice == '1':
                while True:
                    bet_value = input("Enter the number you want to bet on (0-30, or 00): ")
                    if bet_value in self.numbers:
                        break
                    print("Invalid number. Please enter a number between 0-30 or '00'.")
                bet_type = 'number'
            elif choice == '2':
                while True:
                    bet_value = input("Enter the color you want to bet on (red/black): ").lower()
                    if bet_value in ['red', 'black']:
                        break
                    print("Invalid color. Please enter 'red' or 'black'.")
                bet_type = 'color'
            elif choice == '3':
                bet_value = 'green'
                bet_type = 'green'

            while True:
                try:
                    amount = int(input("Enter the amount you want to bet: "))
                    if amount > 0 and amount <= self.balance:
                        break
                    elif amount > self.balance:
                        print(f"Insufficient balance. You have ${self.balance:.2f} available.")
                    else:
                        print("Please enter a positive amount.")
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            self.place_bet(bet_type, bet_value, amount)

            while True:
                exit_choice = input(f"{self.player_name}, continue playing???? (yes/no): ").lower()
                if exit_choice in ['yes', 'no']:
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")

            if exit_choice == 'no':
                print(f"Thanks for playing, {self.player_name}! Goodbye.")
                break

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = CasinoGame(player_name)
    game.start_game()
