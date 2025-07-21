-- 코드를 작성해주세요
with g as (
    select emp_no, case when avg(score) >= 96 then 'S'
                        when avg(score) >= 90 then 'A'
                        when avg(score) >= 80 then 'B'
                        else 'C' end as grade
    from hr_grade
    group by emp_no
)
select h.EMP_NO, EMP_NAME, GRADE, case when grade like 'S' then sal*0.2
                                    when grade like 'A' then sal*0.15
                                    when grade like 'B' then sal*0.1
                                    else 0 end as BONUS
from hr_employees h join g on h.emp_no=g.emp_no
order by h.emp_no asc