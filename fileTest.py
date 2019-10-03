import fileClassTAD as fc
import fileClass as fcl

'''day = fc.Data_day('25','2')

#criando horas para test
for id_hours in range(5,10,2):
    day.add_hours_reserved(fc.Data_hours(f'{id_hours}', None))
for id_hours in range(0,8):
    day.add_hours_reserved(fc.Data_hours(f'{id_hours}', None))

day.print_day()
day.sort_hours_reserved() #Teste de ordenação
day.print_day()

#Teste get_hours_reserved_by_id()
for h in day.get_hours_reserved_by_id('7'):
    print(h, end=' ')

print()

#Teste get_hours_reserved_by_interval()
for h in day.get_hours_reserved_by_interval('5', '7'):
    print(h, end=' ')

print()

#Teste day
print(day.name)

print("\n\n")

month = fc.Date_month('3')

month.add_day(fc.Data_day('15','2'))

print(month.get_days_by_week(3))'''

client = fcl.Client(1, "Talita")
doctor1 = fcl.Doctor(1, "João")
doctor2 = fcl.Doctor(2, "Paulo")
evt1 = fcl.Event(2, doctor1, client, "10-31/7-15")
evt2 = fcl.Event(55, doctor2, client, "10-30/6-15")
evt3 = fcl.Event(14, doctor2, client, "7-5/6-15")
evt4 = fcl.Event(4, doctor2, client, "1-9/6-15")

agenda = fc.Agenda(2019)
agenda.add_event(evt1)
agenda.add_event(evt2)
agenda.add_event(evt3)
agenda.add_event(evt4)


for evt in agenda.get_events_by_client(1):
    print(evt)








