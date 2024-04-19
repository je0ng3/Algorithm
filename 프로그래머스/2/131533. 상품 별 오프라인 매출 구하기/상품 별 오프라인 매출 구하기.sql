select product_code, price*sum(sales_amount) as sales
from product p join offline_sale o on p.product_id=o.product_id
group by product_code, p.product_id
order by sales desc, product_code asc