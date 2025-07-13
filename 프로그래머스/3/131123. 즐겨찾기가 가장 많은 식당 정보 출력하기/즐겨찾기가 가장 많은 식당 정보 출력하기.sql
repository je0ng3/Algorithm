with a as (
    select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
    from rest_info
    order by food_type desc, favorites desc
    LIMIT 18446744073709551615
)
select *
from a
group by food_type