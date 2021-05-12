import datetime as dt
import random


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


today = dt.date.today()
mon = today + dt.timedelta(days=-today.weekday(), weeks=1)
week_list = []
for i in range(8):
    t = mon + dt.timedelta(days=i)
    week_list.append(t.strftime('%Y-%m-%d'))

mon, tues, wed, thurs, fri, sat, sun, next_mon = week_list
msg_ppl = [
'Maddie Lee',
'Bernard Tung',
'Katie Li',
'Kenta Morris',
'Janakan Chandrakumar',
'Marco Gao',
'Ivan Leung',
'Ethan Liong',
'Eric Fung',
'Jason Ho-Shue',
'Kevin Widjaja',
'Henry Ngan',
'Philip So',
'Elvis Ho',
'James Allen Yu',
'Arjun Nair',
'Jessica Wong',
'Jonah Yang',
'Bryan Widjaja',
'Nikki Wong' ]
rand_pers = random.choice(msg_ppl)

query = """tags: #WeeklyPlan
## Top Weekly Goals
### Misc
- [ ] Create [[Weekly Plan - {next_mon}]] [[{sun}]]
- [ ] Clear 5 items from my inbox [[{fri}]]
- [ ] Message / Hangout with this person: [[{rand_pers}]]
## Daily Goals
### Monday [[{mon}]]
```query
line:(("- [ ]" OR "- [x]") [[{mon}]] -"line:(")
```
### Tuesday [[{tues}]]
```query
line:(("- [ ]" OR "- [x]") [[{tues}]] -"line:(")
```
### Wednesday [[{wed}]]
```query
line:(("- [ ]" OR "- [x]")[[{wed}]] -"line:(")
```
### Thursday [[{thurs}]]
```query
line:(("- [ ]" OR "- [x]") [[{thurs}]] -"line:(")
```
### Friday [[{fri}]]
```query
line:(("- [ ]" OR "- [x]") [[{fri}]] -"line:(")
```
### Saturday [[{sat}]]
```query
line:(("- [ ]" OR "- [x]") [[{sat}]] -"line:(")
```
### Sunday [[{sun}]]
```query
line:(("- [ ]" OR "- [x]") [[{sun}]] -"line:(")
```""".format(mon=mon, tues=tues, wed=wed, thurs=thurs, fri=fri, sat=sat, sun=sun, next_mon=next_mon, rand_pers=rand_pers)

print(query)