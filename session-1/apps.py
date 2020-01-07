from datetime import date

if __name__ == "__main__":
    today = date.today()
    print("Today is: {}".format(today.strftime("%d-%m-%Y")))