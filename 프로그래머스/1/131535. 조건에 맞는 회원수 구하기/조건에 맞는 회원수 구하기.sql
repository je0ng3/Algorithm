select count(user_id) as users
from user_info
where age>=20 and age<=29 and substring(joined,1,4)='2021'