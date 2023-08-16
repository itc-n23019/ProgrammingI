class Person:
    def  __init__(self,
                  name = '',
                  nationality = '',
                  birth = '',
                  address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributs(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいる所:", self.address)


