-- 코드를 작성해주세요
select distinct ID, EMAIL, FIRST_NAME, LAST_NAME
from developers d join skillcodes s
on skill_code & code = code
where name in ('Python', 'C#')
order by id asc