import datetime as dt
from datetime import timedelta as td


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


today = dt.date.today()
mon = today + dt.timedelta(days=-today.weekday(), weeks=1)
mon_list = [custom_strftime('%B {S}, %Y', mon)] * 6

query = """- [[school]]
    - [[SYDE543]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[SYDE543]] [[Weekly Plan: {}]]{{not: [[query]]}}}} }}}}
    - [[ECE484]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[ECE484]] [[Weekly Plan: {}]]{{not: [[query]]}}}} }}}}
    - [[KIN255]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[KIN255]] [[Weekly Plan: {}]]{{not: [[query]]}}}} }}}}
    - [[ECE457A]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[ECE457A]] [[Weekly Plan: {}]]{{not: [[query]]}}}} }}}}
    - [[PHIL226]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[PHIL226]] [[Weekly Plan: {}]]{{not: [[query]]}}}} }}}}
    - [[MTE481]]
        - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[MTE481]] [[Weekly Plan: {}]]{{not: [[query]]}}}} }}}}""".format(*mon_list)

print(query)
