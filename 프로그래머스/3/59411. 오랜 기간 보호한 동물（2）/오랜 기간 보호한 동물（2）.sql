select i.animal_id, i.name
from animal_ins i join animal_outs o 
on i.animal_id = o.animal_id and i.animal_type=o.animal_type and i.name = o.name
order by datediff(i.datetime, o.datetime)
limit 2
