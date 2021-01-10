import datetime as dt
from datetime import timedelta as td


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


today = dt.date.today()
mon = today + dt.timedelta(days=-today.weekday(), weeks=1)
week_list = []
for i in range(8):
    week_list.append(custom_strftime('%B {S}, %Y', mon + dt.timedelta(days=i)))

mon, tues, wed, thurs, fri, sat, sun, next_mon = week_list
query = """- ## Top Weekly Goals
    - Misc
        - {{{{[[TODO]]}}}} Create [[Weekly Plan: {next_mon}]]
        - {{{{[[TODO]]}}}} Clear 5 items from my inbox
- ## Daily Goals
    - Monday [[{mon}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{mon}]]{{not: [[query]]}}}} }}}}
    - Tuesday [[{tues}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{tues}]]{{not: [[query]]}}}} }}}}
    - Wednesday [[{wed}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{wed}]]{{not: [[query]]}}}} }}}}
    - Thursday [[{thurs}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{thurs}]]{{not: [[query]]}}}} }}}}
    - Friday [[{fri}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{fri}]]{{not: [[query]]}}}} }}}}
    - Saturday [[{sat}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{sat}]]{{not: [[query]]}}}} }}}}
    - Sunday [[{sun}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{sun}]]{{not: [[query]]}}}} }}}}
- Tags:: #[[Weekly Plan]]""".format(mon=mon, tues=tues, wed=wed, thurs=thurs, fri=fri, sat=sat, sun=sun, next_mon=next_mon)

print(query)
