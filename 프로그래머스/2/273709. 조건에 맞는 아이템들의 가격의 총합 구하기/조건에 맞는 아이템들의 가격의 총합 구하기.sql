select sum(price) as total_price
from item_info
where rarity like "LEGEND"
group by rarity
