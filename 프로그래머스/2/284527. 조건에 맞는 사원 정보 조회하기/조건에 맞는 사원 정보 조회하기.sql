SELECT SCORE, he.EMP_NO, EMP_NAME, POSITION, EMAIL
FROM HR_EMPLOYEES as he JOIN (SELECT EMP_NO, sum(SCORE) as SCORE
                        FROM HR_GRADE
                        GROUP BY EMP_NO) AS hg
on he.emp_no=hg.emp_no
order by score desc
limit 1