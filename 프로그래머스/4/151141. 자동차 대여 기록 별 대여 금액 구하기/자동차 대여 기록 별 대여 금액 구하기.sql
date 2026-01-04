# # 대여된 트럭 정보
# select car_id, daily_fee
# from car_rental_company_car
# where car_type like "트럭"

with a as (
    # 트럭 대여 일자
    select history_id, datediff(end_date, start_date)+1 as dd, daily_fee
    from car_rental_company_rental_history h join (select car_id, daily_fee
        from car_rental_company_car
        where car_type="트럭") as t on h.car_id=t.car_id
),
b as (
    # 기간에 따른 할인 비용
    select cast(left(duration_type, char_length(duration_type)-4) as unsigned) as duration, discount_rate
    from car_rental_company_discount_plan
    where car_type like "트럭"
    order by duration_type desc
)
select history_id, floor(daily_fee*dd*(100-ifnull(discount_rate,0))/100) as fee
from a left join b
on b.duration = (select max(duration) from b b2 where a.dd >= b2.duration)
order by fee desc, history_id desc