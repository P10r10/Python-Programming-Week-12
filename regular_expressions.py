import re


def is_dotw(my_string: str) -> bool:
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    return False


def all_vowels(my_string: str) -> bool:
    if re.search("^[aeiou]+$", my_string):
        return True
    return False


def time_of_day(my_string: str) -> bool:
    if re.search("^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$", my_string):
        return True
    return False


if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("23:55:59"))
    print(time_of_day("16:34:56"))
    print(time_of_day("19:zz:04"))
