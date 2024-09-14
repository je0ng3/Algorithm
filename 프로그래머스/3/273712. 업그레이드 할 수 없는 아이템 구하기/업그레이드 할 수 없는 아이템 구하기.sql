with unupgradable as (
    select b.item_id as id
    from item_tree b 
    where b.item_id not in 
        (select distinct a.parent_item_id 
         from item_tree as a 
         where a.parent_item_id is not null)
)
select i.item_id, i.item_name, i.rarity
from item_info i join unupgradable u on u.id = i.item_id
order by item_id desc