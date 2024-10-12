-- 코드를 작성해주세요
with a as (
    select id, FISH_TYPE, case when length is null then 10
                                else length end as length
    from FISH_INFO
)
select count(id) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE
from a
group by fish_type
having avg(length)>=33
order by fish_type asc
