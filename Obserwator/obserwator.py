class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' "\
               f"has data = {self._data}"

    @ property
    def data(self):
        return self._data

    @ data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print(f'Error: {e}')
        else:
            self.notify()


class HexFormatterObs:
    def notify(self, publisher):
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")


class BinaryFormatterObs:
    def notify(self, publisher):
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now bin data = {value}")


class OctFormatterObs:                                                                  #formater ósemkowy
    def notify(self, publisher):
        value = oct(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now oct data = {value}")

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


class Roman:                                                                              #formater liczb rzymskich
    def notify(self, publisher):
        value = int_to_roman(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now Roman data = {value}")


def main():
    nazwa = input("Wprowadź nazwę DefaultFormatter ")

    df = DefaultFormatter(nazwa)
    print(df)

    print()
    obshex = input("Czy dołączyć obserwator hex? T/N ")
    if obshex in 'Tt':
        hf = HexFormatterObs()
        df.add(hf)
        datahex = input("Podaj wartość data dla hex ")
        df.data = datahex
        print(df)

    print()
    obsbin = input("Czy dołączyć obserwator bin? T/N ")
    if obsbin in 'Tt':
        bf = BinaryFormatterObs()
        df.add(bf)
        databin = input("Podaj wartość data dla bin ")
        df.data = databin
        print(df)

    print()
    obsoct = input("Czy dołączyć obserwator oct? T/N ")
    if obsoct in 'Tt':
        of = OctFormatterObs()
        df.add(of)
        dataoct = input("Podaj wartość data dla oct ")
        df.data = dataoct
        print(df)

    print()
    obsrom = input("Czy dołączyć obserwator Roman? T/N ")
    if obsrom in 'Tt':
        rf = Roman()
        df.add(rf)
        datarom = input("Podaj wartość data dla rom ")
        df.data = datarom
        print(df)

    print()
    obshexusun = input("Czy usunąć obserwator hex? T/N ")
    if obshexusun in 'Tt':
        df.remove(hf)
        df.data = 40
        print(df)

    print()
    obshexusun2 = input("Czy usunąć obserwator hex? T/N ")
    if obshexusun2 in 'Tt':
        df.remove(hf)
    print()
    obshexdod = input("Czy dołączyć obserwator bin? T/N ")
    if obshexdod in 'Tt':
        df.add(bf)

    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()
