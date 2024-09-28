with a as (
    select YEAR(ym) as year, pm_val1, pm_val2
    from air_pollution
    where location1 like "경기도" and location2 like "수원"
)
select YEAR, round(avg(pm_val1),2) as "PM10", round(avg(pm_val2),2) as "PM2.5"
from a
group by year
order by year asc