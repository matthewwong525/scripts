import datetime as dt
from datetime import timedelta as td


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


today = dt.date.today()
mon = today + dt.timedelta(days=-today.weekday(), weeks=1)
mon_list = [custom_strftime('%B {S}, %Y', mon)] * 6

classes_a = ['SYDE543', 'ECE484', 'KIN255', 'ECE457A', 'PHIL226', 'MTE481']
classes_b = ['SYDE544', 'ENGL335', 'MTE546', 'ME598', 'FYDP']

query = "- [[school]]"

for c in classes_b:
    query += "\n    - [[{c}]]\n        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{c}]] [[Weekly Plan: {d}]]{{not: [[query]]}}}} }}}}".format(c = c, d = custom_strftime('%B {S}, %Y', mon))

print(query)
