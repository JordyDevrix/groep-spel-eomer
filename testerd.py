import json


def main():
    file = open("charact.json")

    data = json.load(file)
    enter_key = "loc1"

    def verhalen(entered_key):
        for i in range(len(data)):
            if entered_key in data[i]:
                if not data[i].get(entered_key).get('eind'):
                    verhaal = data[i].get(entered_key).get('verhaal')
                    optie1 = data[i].get(entered_key).get('opties').get('optie1')[0]
                    optie2 = data[i].get(entered_key).get('opties').get('optie2')[0]
                    optie3 = data[i].get(entered_key).get('opties').get('optie3')[0]
                    print(verhaal)
                    print(f"maak een keuze:\n"
                          f"optie 1: {optie1}\n"
                          f"optie 2: {optie2}\n"
                          f"optie 3: {optie3}")
                    keuze = int(input())
                    if keuze == 1:
                        entered_key = data[i].get(entered_key).get('opties').get('optie1')[1]
                        return verhalen(entered_key), data[i].get(entered_key).get('eind')
                    elif keuze == 2:
                        entered_key = data[i].get(entered_key).get('opties').get('optie2')[1]
                        return verhalen(entered_key), data[i].get(entered_key).get('eind')
                    elif keuze == 3:
                        entered_key = data[i].get(entered_key).get('opties').get('optie3')[1]
                        return verhalen(entered_key), data[i].get(entered_key).get('eind')
                else:
                    print(data[i].get(entered_key).get('verhaal'))

    us = verhalen(enter_key)
    print(us)


if __name__ == '__main__':
    main()