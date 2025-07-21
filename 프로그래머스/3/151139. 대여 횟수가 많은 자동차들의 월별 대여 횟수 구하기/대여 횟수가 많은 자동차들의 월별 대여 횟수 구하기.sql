with filtered as (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where '20220801'<=start_date and start_date<'20221101'
    group by car_id
    having count(history_id)>=5
)
select month(start_date) as MONTH, CAR_ID, count(history_id) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where '20220801'<=start_date and start_date<'20221101'
    and car_id in (select * from filtered) 
group by month(start_date), car_id
having count(history_id) > 0
order by month(start_date) asc, car_id desc