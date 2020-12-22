import datetime as dt
from datetime import timedelta as td


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


today = dt.date.today()
mon = today + dt.timedelta(days=-today.weekday(), weeks=1)
week_list = []
for i in range(7):
    week_list.append(custom_strftime('%B {S}, %Y', mon + dt.timedelta(days=i)))
    week_list.append(custom_strftime('%B {S}, %Y', mon + dt.timedelta(days=i)))

week_list.insert(0, custom_strftime('%B {S}, %Y', mon + dt.timedelta(days=7)))

query = """- ## Top Weekly Goals
    - Misc
        - {{{{[[TODO]]}}}} Create [[Weekly Plan: {}]]
- ## Daily Goals
    - Monday [[{}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
    - Tuesday [[{}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
    - Wednesday [[{}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
    - Thursday [[{}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
    - Friday [[{}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
    - Saturday [[{}]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
    - Sunday [[{}]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
- Tags:: #[[Weekly Plan]]""".format(*week_list)

print(query)
