from datetime import date


def getNumbers(num1, num2):
    results = num1 * num2
    return results

def getDate(y, m, d):
    year = date.year(y)
    month = date.month(m)
    day = date.day(d)
    dateToday = month + '-' + day + '-' + year
    return dateToday
    


if __name__ == "__main__":
    pass
