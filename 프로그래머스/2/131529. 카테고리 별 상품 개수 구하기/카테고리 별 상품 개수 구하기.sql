with ca as(
    select left(product_code, 2) as category, product_id
    from product
)
select category, count(product_id) as products
from ca
group by category
order by category