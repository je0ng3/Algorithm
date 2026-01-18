-- 코드를 작성해주세요
with temp as (
    select id, ntile(4) over (order by size_of_colony desc) as group_num
    from ECOLI_DATA
    order by id asc
)
select ID, case when group_num = 1 then 'CRITICAL'
            when group_num = 2 then 'HIGH'
            when group_num = 3 then 'MEDIUM'
            else 'LOW' end as COLONY_NAME
from temp