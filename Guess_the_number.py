import random

def main():
    GUESSES = int(input("Hur många chanser vill du ha?\n"))
    print(f"Du har {GUESSES} försök på dig.")
    NUMBER = random.randint(1, 100)

    for _ in range(GUESSES):
        GUESS = int(input("Gissa numret mellan 1-100\n"))
        if NUMBER == GUESS:
            print("Du hade rätt!")
            break
        elif GUESS > NUMBER:
            print("Numret är lägre!")
        else:
            print("Numret är större!")
    print(f"Numret var {NUMBER}")
    CONTINUE = input("Vill du fortsätta?\n").lower()
    main() if CONTINUE == "ja" else quit()

main() if __name__ == "__main__" else print("Filen skall ej importeras, utan köras direkt.")
