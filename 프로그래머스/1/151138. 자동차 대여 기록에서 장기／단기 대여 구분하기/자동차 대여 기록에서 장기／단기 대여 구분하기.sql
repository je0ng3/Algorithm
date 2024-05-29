SELECT HISTORY_ID, CAR_ID, substring(start_date,1,10) as START_DATE, substring(end_date,1,10) as END_DATE,
       CASE 
           WHEN DATEDIFF(end_date, start_date)+1 >= 30 THEN '장기 대여' 
           ELSE '단기 대여' 
       END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date like "2022-09%"
ORDER BY HISTORY_ID DESC;