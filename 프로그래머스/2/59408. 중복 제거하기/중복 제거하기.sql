-- 코드를 입력하세요
SELECT count(distinct name) as count
FROM animal_ins
WHERE name is not null