with hour as(
    select animal_id, substring(datetime,12,13)-'0' as h
    from animal_outs
)
select h as HOUR, count(animal_id) as COUNT
from hour
where h between 9 and 20
group by h
order by h