select member_id, member_name, gender, substring_index(date_of_birth, ' ', 1) as date_of_birth
from member_profile
where gender like 'W' and tlno is not null and substring_index(date_of_birth,' ',1) like '%-03-%'
order by member_id asc