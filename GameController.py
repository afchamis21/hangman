from Game import Game


class GameController:
    def __init__(self, game: Game):
        self.__player_name = ""
        self.game = game

    def __get_player_name(self):
        while True:
            name = input("Whats your name? ")
            name = name.strip()
            if not name:
                print("Please type a valid name")
                continue

            self.__player_name = name
            return

    def start(self) -> None:
        if not self.__player_name:
            self.__get_player_name()

        message = self.game.run()
        print(message)

        if input(f"\n{self.__player_name}, if you wish to play again type [Y]: ").upper() == "Y":
            self.start()
