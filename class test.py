class Kandidat:
    _name: str
    _age: int
    _sex: str
    _edu: int

    def __init__(self, name='Kien'):
        self._name = name
        self._age = 25
        self._sex = 'man'
        self._edu = 1

    def set_age(self, age):
        self._age = age

    def set_sex(self, sex):
        self._sex = sex

    def set_edu(self, edu):
        self._edu = edu

    def get_info(self):
        return self._name + ': ' + str(self._age) + self._sex + str(self._edu)


class Komandir(Kandidat):
    _xperiens = 100
    def __init__(self, name='kien'):
        super().__init__(name)
    def set_xp(self, xp):
        self._xperiens = xp
    def get_xp(self):
        return self._name + str(self._xperiens)

Kan_1 = Kandidat('Khalif')
Kan_2 = Kandidat('Romanoff')
Kan_3 = Kandidat('Maximoff')

see_info = Kandidat('Khiu')
print(see_info.get_info())


kom_1 = Komandir('Saganov')





