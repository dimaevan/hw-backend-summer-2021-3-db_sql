# INFO
# Вывести топ 5 самых коротких по длительности перелетов
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
SELECT flight_no, (scheduled_arrival - scheduled_departure) as duration
FROM flights 
WHERE (scheduled_arrival - scheduled_departure) is not null
ORDER BY 2 LIMIT 5;
"""
#  flight_no | duration 
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
SELECT flight_no, count(1) as count
FROM flights
GROUP BY flight_no 
HAVING count(flight_no) < 50
ORDER BY 2 DESC 
LIMIT 3; 
"""
#  flight_no | count 
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# INFO
# Вывести число перелетов внутри одной таймзоны 
# Нузно вывести 1 значение в колонке count
TASK_3_QUERY = """
SELECT count(1)
FROM flights
INNER JOIN airports_data as one 
ON flights.arrival_airport = one.airport_code 
INNER JOIN airports_data as two 
ON flights.departure_airport = two.airport_code 
WHERE one.timezone = two.timezone;
"""
#  count  
# --------
#  16824

