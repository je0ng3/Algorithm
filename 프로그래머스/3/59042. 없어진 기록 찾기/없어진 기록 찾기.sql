SELECT a.animal_id, a.name
FROM animal_outs a
LEFT JOIN animal_ins b ON a.animal_id = b.animal_id AND a.name = b.name
WHERE b.animal_id IS NULL and a.name is not null;
