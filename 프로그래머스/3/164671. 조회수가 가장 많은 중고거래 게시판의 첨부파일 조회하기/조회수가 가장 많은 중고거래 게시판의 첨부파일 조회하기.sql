-- 코드를 입력하세요
with a as(
    SELECT * 
    from USED_GOODS_BOARD
    order by views desc
    limit 1
)
select concat('/home/grep/src/', a.BOARD_ID, '/', file_id,file_name,file_ext)
from a join USED_GOODS_FILE
on a.BOARD_ID = USED_GOODS_FILE.BOARD_ID
order by FILE_ID desc