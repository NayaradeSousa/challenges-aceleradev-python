"""
Codenation's Aceleradev Python Challenge 01.
Software responsible for charging calls, it receives a report with the calls and calculates the invoice value of
each customer, based on the day or night charging rules.

Pricing:
Daytime - between 6:00 am and 10:00 pm:
     * Permanent charge: R $ 0.36 (fixed charges that are used to pay the cost of the connection);
     * Call rate / minute: R $ 0.09 (there is no fractional charge. * The charge applies to each completed cycle of 60
seconds) *.
Night - between 10 pm and 6 am:
     * Permanent fee: R $ 0.36
     * Call rate / minute: R $ 0.00
The software sorts calls by source number and groups them with the total value of calls made by that number.
Important:

-The calculation is made considering the time of each minute, for example, the same call may have different rates if
it starts during the day and ends at night, that is, each minute must be charged according to its initial time.
-For this challenge, only consider connections that start and end on the same day.
-The data for this challenge uses a timestamp with a timezone from Brazil / East.
"""
from datetime import datetime
import pytz
import pprint as pp

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

PERMANENT_FEE = 0.36
DAY_RATE = 0.09
START_TIME_DAY_RATE = 6
FINAL_TIME_DAY_RATE = 22


def convert_time(start, end):
    beginning = datetime.fromtimestamp(start, tz=pytz.timezone('Brazil/East'))
    finish = datetime.fromtimestamp(end, tz=pytz.timezone('Brazil/East'))
    return beginning, finish


def calculation_minutes(beginning, finish):
    duration_seconds = (finish - beginning).total_seconds()
    return int(duration_seconds / 60)


def calculate_call_price(start, end):
    beginning, finish = convert_time(start, end)
    duration_minutes = calculation_minutes(beginning, finish)

    if START_TIME_DAY_RATE <= beginning.hour < FINAL_TIME_DAY_RATE:
        if finish.hour < FINAL_TIME_DAY_RATE:
            call_price = (duration_minutes * DAY_RATE) + PERMANENT_FEE
        else:
            night_call = beginning.replace(hour=22, minute=00, second=00)
            duration_minutes_night_call = calculation_minutes(night_call, finish)
            call_price = (abs(duration_minutes - duration_minutes_night_call) * DAY_RATE) + PERMANENT_FEE
    else:
        if START_TIME_DAY_RATE <= finish.hour < FINAL_TIME_DAY_RATE:
            day_call = beginning.replace(hour=6, minute=00, second=00)
            duration_minutes_day_call = calculation_minutes(day_call, finish)
            call_price = (duration_minutes_day_call * DAY_RATE) + PERMANENT_FEE
        else:
            call_price = PERMANENT_FEE

    return round(call_price, 2)


def classify_by_phone_number(records):
    bills = []

    for record in records:
        phone_number = record['source']
        call_price = round(calculate_call_price(record['start'], record['end']), 2)
        new_bill = 0

        # Checking if the phone number is repeated and writing in 'bills'
        for bill in bills:
            if phone_number in bill.values():
                total_call_price = bill['total'] + call_price
                bill['total'] = round(total_call_price, 2)
                new_bill = 0
                break
            else:
                new_bill = {'source': phone_number, 'total': call_price}

        # Writing phone number and invoice total if 'bills' list is empty
        if not bills:
            new_bill = {'source': phone_number, 'total': call_price}
        if new_bill != 0:
            bills.append(new_bill)

    return sorted(bills, key=lambda i: i['total'], reverse=True)


if __name__ == '__main__':
    pp.pprint(classify_by_phone_number(records))
