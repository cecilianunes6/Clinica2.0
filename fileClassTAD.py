import operator

#Formato da data é mm-dd/r-hh

# mm : Mês
# dd : dia / rr : referencia ao dia da semana
# hh : hora


class Data_hours:
    def __init__(self, id, event):
        self.id = id
        self.event = event
    def __str__(self):
        return str(self.id)


class Data_day:
    def __init__(self, id_prin, id_sec):
        dict_days = {
            1 : 'Domingo',
            2 : 'Segunda',
            3 : 'Terça',
            4 : 'Quarta',
            5 : 'Quinta',
            6 : 'Sexta',
            7 : 'Sábado'
        }
        self.id_princ = id_prin
        self.id_secund = id_sec
        self.name = dict_days[self.id_secund]
        self.hours_reserved = list()

    def add_hours_reserved(self, h):
        if (len(self.hours_reserved) <= 24):
            self.hours_reserved.append(h)
            self.sort_hours_reserved()
            return 0
        return -1

    def sort_hours_reserved(self):
        self.hours_reserved.sort(key=operator.attrgetter('id'))

    def count_hours_reserved(self):
        return len(self.hours_reserved)

    def get_hours_reserved_by_id(self, id):
        id = int(id)
        return list(filter(lambda hours: hours.id == id, self.hours_reserved))

    def get_hours_reserved_by_interval(self, start, stop):
        start = int(start)
        stop = int(stop)
        return list(filter(lambda hours: hours.id >= start and hours.id <= stop, self.hours_reserved))

    def print_day(self):
        for hours in self.hours_reserved:
            print(hours, end=" ")
        print()

    def is_exist_hours(self, str_hours):
        int(str_hours)
        return str_hours in [hours.id for hours in self.hours_reserved]

class Date_month:
    def __init__(self, id):
        dict_month = {
            1 : 'Jeneiro',
            2 : 'Fevereiro',
            3 : 'Março',
            4 : 'Abril',
            5 : 'Maio',
            6 : 'Junho',
            7 : 'Julho',
            8 : 'Agosto',
            9 : 'Setembro',
            10 : 'Outubro',
            11 : 'Novembro',
            12 : 'Dezembro'
        }

        self.id = id
        self.nome = dict_month[id]
        self.days = list()

    def add_day(self, d):
        if len(self.days) <= self.days_limit():
            self.days.append(d)
            self.sort_days()
            return 0
        return -1

    def sort_days(self):
        self.days.sort(key=operator.attrgetter('id_princ'))

    def days_limit(self):
        if self.id in [1, 3, 5, 7,8, 10, 12]: return 31
        elif self.id in [4,6, 9, 11]: return 30
        else: return 28

    def get_days_by_week(self, id_week):
        id_week = int(id_week)
        return list(filter(lambda day: day.id_princ > (id_week - 1) * 7 and day.id_princ < id_week * 7, self.days))

    def get_days_by_id(self, id):
        id = int(id)
        for day in self.days:
            if day.id_princ == id : return day
        return  -1

    def count_days(self):
        return len(self.days)

    def is_exist_day(self, day):
        day = int(day)
        return day in [day_w.id_princ for day_w in self.days]


class Agenda:
    def __init__(self, year):
        self.year = year
        self.month = list()

    def is_exist_month(self, int_month):
        int_month = int(int_month)
        return int_month in [month.id for month in self.month]

    def get_month_by_id(self, int_month):
        int_month = int(int_month)
        for month in self.month:
            if month.id == int_month : return month
        return  -1

    def add_month(self, month):
        self.month.append(month)
        self.sort_month()

    def sort_month(self):
        self.month.sort(key=operator.attrgetter('id'))

    def create_day(self, id_princ, id_sec):
        id_princ = int(id_princ)
        id_sec = int(id_sec)
        return Data_day(id_princ, id_sec)

    def create_hours(self, id, event):
        id = int(id)
        return Data_hours(id, event)

    def create_month(self, id):
        id = int(id)
        return Date_month(id)

    def get_events_by_client(self, id_client):
        list_events = list()
        for month in self.month:
            for day in month.days:
                for hours in day.hours_reserved:
                    if hours.event.client.id == id_client:
                        list_events.append(hours.event)
        return list_events


    def add_event(self, event):
        data = str(event.data).split('-') #mm-dd/rr-hh
        if self.is_exist_month(data[0]):
            month = self.get_month_by_id(data[0])
            dd, rr = data[1].split('/')
            if month.is_exist_day(dd):
                day = month.get_days_by_id(dd)
                day.add_hours_reserved(self.create_hours(data[2], event))
            else:
                day = self.create_day(dd, rr)
                month.add_day(day)
                day.add_hours_reserved(self.create_hours(data[2], event))
        else:
            month = self.create_month(data[0])
            self.add_month(month)
            dd, rr = data[1].split('/')
            day = self.create_day(dd, rr)
            month.add_day(day)
            hours = self.create_hours(data[2], event)
            day.add_hours_reserved(hours)