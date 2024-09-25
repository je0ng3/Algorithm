with average as (
    select car_id, TIMESTAMPDIFF(day, start_date, end_date)+1 as diff
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)
select CAR_ID, round(avg(diff),1) as AVERAGE_DURATION
from average
group by car_id
having round(avg(diff),1)>7
order by round(avg(diff),1) desc, car_id desc