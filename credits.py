from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts: list[CourseAttempt]) -> int:
    return reduce(lambda total, attempt: total + attempt.credits, attempts, 0)


def sum_of_passed_credits(attempts: list[CourseAttempt]) -> int:
    filtered = filter(lambda ca: ca.grade >= 1, attempts)
    return reduce(lambda total, attempt: total + attempt.credits, filtered, 0)


def average(attempts: list[CourseAttempt]) -> float:
    filtered = list(filter(lambda ca: ca.grade >= 1, attempts))
    return reduce(
        lambda total, attempts: total + attempts.grade, filtered, 0
    ) / len(filtered)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
