-- 코드를 작성해주세요
with f as (
select dept_id, sum(sal)/count(sal) as avg_sal
from hr_employees
group by dept_id
)
select f.dept_id as DEPT_ID, DEPT_NAME_EN, round(avg_sal,0) as AVG_SAL
from hr_department join f on hr_department.dept_id = f.dept_id
order by avg_sal desc