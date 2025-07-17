select year(sales_date) as YEAR, month(sales_date) as MONTH, GENDER, count(distinct o.user_id) as USERS
from online_sale o join user_info u on o.user_id = u.user_id
where gender is not null
group by year, month, gender
order by convert(year, UNSIGNED), convert(month, UNSIGNED), convert(gender, UNSIGNED)