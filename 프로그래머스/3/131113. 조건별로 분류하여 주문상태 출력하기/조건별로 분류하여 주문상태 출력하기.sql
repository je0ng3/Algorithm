with isout as(
    select order_id, substring(out_date, 6, 7)-'0' as _check1, substring(out_date, 9, 10)-'0' as _check2
    from food_order
)
select food_order.order_id, product_id, left(out_date,10), case 
    when _check1<5 or (_check1=5 and _check2=1) then "출고완료"
    when _check1 is null then "출고미정"
    else "출고대기" end as "출고여부"
from food_order join isout on food_order.order_id = isout.order_id
order by food_order.order_id asc