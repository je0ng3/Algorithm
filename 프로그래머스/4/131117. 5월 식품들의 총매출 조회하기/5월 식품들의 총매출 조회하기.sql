with indate as (
    select product_id, amount
    from food_order
    where year(produce_date)='2022' and month(produce_date)='05'
)
select fp.PRODUCT_ID, PRODUCT_NAME, counts*price as TOTAL_SALES
from food_product fp join (select product_id, sum(amount) as counts
                            from indate
                            group by product_id) as id
on fp.product_id = id.product_id
order by counts*price desc, fp.product_id asc
