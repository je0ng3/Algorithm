select count(id) as FISH_COUNT
from fish_info
where fish_type in (select o.fish_type
                    from fish_name_info o
                    where o.fish_name like "BASS" or o.fish_name like "SNAPPER")