class FileReader:
    def __init__(self, file_name) -> None:
        pass

    def read_data(self) -> dict:
        pass  # TODO


class HockeyApp:
    def __init__(self) -> None:
        file_name = input("file name: ")
        self.__players = FileReader(file_name).read_data()
        self.__menu()

    def __menu(self):
        print("""
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals
              """)


if __name__ == "__main__":
    HockeyApp()
