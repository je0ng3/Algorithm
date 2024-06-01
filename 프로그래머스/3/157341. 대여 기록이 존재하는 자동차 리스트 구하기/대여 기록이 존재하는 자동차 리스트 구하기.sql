select c.car_id
from CAR_RENTAL_COMPANY_CAR a join CAR_RENTAL_COMPANY_RENTAL_HISTORY c
on a.car_id = c.car_id
where car_type = '세단' and start_date like "%-10-%"
group by c.car_id
order by c.car_id desc