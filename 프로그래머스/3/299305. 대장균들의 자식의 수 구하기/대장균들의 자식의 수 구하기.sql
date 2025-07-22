select e.ID, (select count(d.id) from ecoli_data d 
            where d.parent_id=e.id) as CHILD_COUNT
from ecoli_data e

