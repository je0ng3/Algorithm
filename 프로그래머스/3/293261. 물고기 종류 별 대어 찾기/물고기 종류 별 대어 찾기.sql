with bigfish as (
    select id, fish_type, length
    from fish_info
    where (fish_type, length) in (select c.fish_type, max(c.length)
                                from fish_info c
                                group by c.fish_type)
)
select id, fish_name, length
from fish_name_info a join bigfish b on a.fish_type=b.fish_type
order by id asc