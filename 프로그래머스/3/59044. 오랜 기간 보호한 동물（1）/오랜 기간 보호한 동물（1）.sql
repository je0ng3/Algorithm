-- 코드를 입력하세요
SELECT name, datetime
from animal_ins
where animal_id not in (select i.animal_id from animal_outs i)
order by datetime
limit 3