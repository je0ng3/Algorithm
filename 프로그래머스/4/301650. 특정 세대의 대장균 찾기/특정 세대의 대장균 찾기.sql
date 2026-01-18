-- 코드를 작성해주세요
with a as (
    select id
    from ecoli_data
    where parent_id is NULL
),
b as (
    select distinct e.id
    from ecoli_data e join a
    on e.parent_id=a.id
)
select distinct c.id
from ecoli_data c join b
on c.parent_id=b.id
order by c.id asc