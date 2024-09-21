with year_max as (
    select year, max(SIZE_OF_COLONY) as _max
    from (select year(DIFFERENTIATION_DATE) as year, id, SIZE_OF_COLONY
        from ECOLI_DATA) as a
    group by year
)
select year as YEAR, _max-SIZE_OF_COLONY as YEAR_DEV, ID
from year_max join ECOLI_DATA
where year(DIFFERENTIATION_DATE)=year
order by year asc, YEAR_DEV asc