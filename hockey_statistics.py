import json


class FileReader:

    @staticmethod
    def read_data() -> dict:
        file_name = input("file name: ")
        with open(file_name) as fp:
            return json.loads(fp.read())


class HockeyApp:
    def __init__(self, players: list[dict]) -> None:
        self.__players = players
        self.__menu()
        self.__run()

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

    def __run(self):
        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            self.__process(command)

    def __process(self, command: str):
        if command == "1":
            self.__search_for_player()
        elif command == "2":
            self.__teams()
        elif command == "3":
            self.__countries()
        elif command == "4":
            self.__players_in_team()
        elif command == "5":
            self.__players_from_country()
        elif command == "6":
            self.__most_points()
        elif command == "7":
            self.__most_goals()

    def __formatted_player(self, p: dict) -> str:
        return f"{p['name']:21}{p['team']:5}{p['goals']:2} + " \
            f"{p['assists']:2} = {p['goals'] + p['assists']:3}"

    def __search_for_player(self):
        name = input("name: ")
        try:
            p = [p for p in self.__players if p["name"] == name][0]  # player
            print(self.__formatted_player(p))
        except:
            pass

    def __teams(self):
        teams = sorted(list(set([p["team"] for p in self.__players])))
        for team in teams:
            print(team)

    def __countries(self):
        countries = sorted(
            list(set([p["nationality"] for p in self.__players])))
        for country in countries:
            print(country)

    def __display(self, players: list):
        sorted_players = sorted(
            players, key=lambda p: p["assists"] + p["goals"], reverse=True)
        print()
        for player in sorted_players:
            print(self.__formatted_player(player))

    def __players_in_team(self):
        team = input("team: ")
        players = [p for p in self.__players if p["team"] == team]
        self.__display(players)

    def __players_from_country(self):
        country = input("country: ")
        players = [p for p in self.__players if p["nationality"] == country]
        self.__display(players)

    def __most_points(self):
        nb = int(input("how many: "))
        sorted_players = sorted(
            self.__players,
            key=lambda p: (p["assists"] + p["goals"], p["goals"]),
            reverse=True)
        for player in sorted_players[0: nb]:
            print(self.__formatted_player(player))

    def __most_goals(self):
        nb = int(input("how many: "))
        sorted_players = sorted(
            self.__players, key=lambda p: (p["goals"], -p["games"]),
            reverse=True)
        for player in sorted_players[0: nb]:
            print(self.__formatted_player(player))


if __name__ == "__main__":
    players = FileReader().read_data()
    print(f"read the data of {len(players)} players")
    HockeyApp(players)
