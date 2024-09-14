with rest as (
    SELECT rest_id, rest_name, food_type, favorites, address
    from rest_info i 
    where address like "서울%"
)
select r.rest_id, rest_name, food_type, favorites, address, round(avg(r.review_score),2) as score
from rest_review as r join rest on r.rest_id = rest.rest_id
group by r.rest_id
order by score DESC, favorites DESC


