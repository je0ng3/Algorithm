select item_id, item_name, rarity
from item_info
where item_id in (
    select t.item_id as pi
    from item_tree t
    where t.parent_item_id in (select i.item_id as ri
                            from item_info i
                            where rarity like "RARE")
    ) 
order by item_id desc