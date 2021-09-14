class birthday():
    def __init__(self, content = [], name_birth = [], month = ""):
        self.content = []
        self.name_birth = []
        self.month = ""


    def open_archive(self, archive):
        with open(archive) as f:
            self.content = f.readlines()
            self.main(self.content)

    def main(self, archive):
        self.name_birth = [line.strip() for line in archive]
        without_new_lines = lambda x: not x == ''
        self.name_birth = [line for line in self.name_birth if without_new_lines(line)]
        self.name_birth.remove('Nome, Aniversário')
        self.name_birth.sort()
        #print(name_birth)
        print('\n')

        message = '{} was born in {}, and makes her/his birthday in {}.'

        for i in range(len(self.name_birth)):
            name, d = self.name_birth[i].split(', ')
            if d[0].isnumeric():
                month_d = int(d[3:5])
                self.month = self.dates(month_d)
            else:
                self.month = '<date not find>'
            print(message.format(name, d[6:8], self.month))

        print('\n')

    def dates(self, d):
        if d == 1:
            self.month = 'January'
        elif d == 2:
            self.month = 'February'
        elif d == 3:
            self.month = 'March'
        elif d == 4:
            self.month = 'April'
        elif d == 5:
            self.month = 'May'
        elif d == 6:
            self.month = 'June'
        elif d == 7:
            self.month = 'July'
        elif d == 8:
            self.month = 'August'
        elif d == 9:
            self.month = 'September'
        elif d == 10:
            self.month = 'October'
        elif d == 11:
            self.month = 'November'
        elif d == 12:
            self.month = 'December'
        return self.month


b_day = birthday()
b_day.open_archive("movimento_bdays")
