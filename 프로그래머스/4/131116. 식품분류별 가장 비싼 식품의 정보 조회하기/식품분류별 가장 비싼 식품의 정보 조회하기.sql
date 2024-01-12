select category, price as max_price, product_name
from food_product
where (category, price) in (select e.category, max(e.price)
                            from food_product e
                            where e.category in ('과자','국','김치','식용유')
                            group by e.category)
order by price desc