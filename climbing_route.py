class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


def sort_by_length(routes: list[ClimbingRoute]) -> list[ClimbingRoute]:
    def length(r: ClimbingRoute):
        return r.length
    return sorted(routes, key=length, reverse=True)


def sort_by_difficulty(routes: list[ClimbingRoute]) -> list[ClimbingRoute]:
    def grade_length(r: ClimbingRoute):
        return r.grade, r.length

    return sorted(routes, key=grade_length, reverse=True)


if __name__ == "__main__":
    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")

    routes = [r1, r2, r3]
    for route in sort_by_difficulty(routes):
        print(route)
