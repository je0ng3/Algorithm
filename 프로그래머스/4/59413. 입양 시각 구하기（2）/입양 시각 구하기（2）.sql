with recursive hours as(
    select 0 as hour
    union all
    select hour +1
    from hours
    where hour < 23
)
SELECT hour as HOUR, count(animal_id) as COUNT
from hours h left join animal_outs
on hour=hour(datetime)
group by hour
order by hour 