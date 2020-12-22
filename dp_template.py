import datetime as dt
from datetime import timedelta as td


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


today = custom_strftime('%B {S}, %Y', dt.date.today())

query = """- ## Daily Plan::
    - {{{{[[query]]: {{and: {{or: [[TODO]] [[DONE]]}} [[{}]]{{not: [[query]]}}}} }}}}
- ## Productivity::
    - {{{{[[table]]}}}}
        - **Task**
            - **Start Time**
                - **End Time**
- ## Journal::""".format(today)

print(query)
