-- 코드를 작성해주세요
with q as (
    select id, case when month(DIFFERENTIATION_DATE)<4 then '1Q'
            when month(DIFFERENTIATION_DATE)<7 then '2Q'
            when month(DIFFERENTIATION_DATE)<10 then '3Q'
            else '4Q' end as QUARTER
    from ECOLI_DATA
)
select QUARTER, count(id) as ECOLI_COUNT
from q
group by quarter
order by quarter asc