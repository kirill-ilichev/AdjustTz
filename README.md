# Home task for Adjust company

## Installation
1. `git clone https://github.com/kirill-ilichev/AdjustTz.git`
2. `cd AdjustTz`
3. Create virtualenv in any way you want (e.g. `python3 -m venv .venv` or `virtualenv -p python3 .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. `python manage.py runserver`

Voila you have working version of app

# Common API use-cases:
> Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
>
> http://127.0.0.1:8000/api/metrics/?sum=impressions,clicks&date_to=2017-06-01&group_by=channel,country&ordering=-clicks

> Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
>
> http://127.0.0.1:8000/api/metrics/?sum=installs&date_from=2017-05-01&date_to=2017-06-01&os=ios&group_by=date&ordering=date

> Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
>
> http://127.0.0.1:8000/api/metrics/?sum=revenue&date=2017-06-01&country=US&group_by=os&ordering=-revenue

> Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
>
> http://127.0.0.1:8000/api/metrics/?sum=cpi,spend&country=CA&group_by=channel&ordering=-cpi

