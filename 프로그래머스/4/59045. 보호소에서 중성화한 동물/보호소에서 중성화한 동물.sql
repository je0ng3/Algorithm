-- 코드를 입력하세요
SELECT animal_id, animal_type, name
from animal_ins
where sex_upon_intake like "Intact%"
    and animal_id not in (select i.animal_id
                       from animal_outs i
                       where i.sex_upon_outcome like "Intact%") 
order by animal_id