from game_pvp import play_pvp
def show_menu():
    print("====Game mode selection====")
    print("1. Player vs Player")
    print("2. Settings")
    print("3. Exit")

def choose_mode():
    while True:
        show_menu()
        game_mode = input("Choose game mode: ")
        if game_mode == "1":
            play_pvp()
            break
        elif game_mode == "2":
            print("Settings are not completed, yet.")
            input("Press enter to get back to menu: ")
            pass
        elif game_mode == "3":
            exit()
        else:
            print("Invalid choice, try again.")
            input("Press Enter to continue: ")
    
if __name__ == "__main__":
    choose_mode()
