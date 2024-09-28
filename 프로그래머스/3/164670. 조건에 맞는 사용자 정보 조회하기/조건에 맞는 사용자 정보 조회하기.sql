-- 코드를 입력하세요
with a as (
    SELECT b.WRITER_ID as user_id, count(b.WRITER_ID) as c, NICKNAME, concat(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) as address, TLNO
    from USED_GOODS_BOARD b join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
    group by b.WRITER_ID
)
select user_id, nickname, address as 전체주소, CONCAT(SUBSTR(tlno, 1, 3), '-', SUBSTR(tlno, 4, 4), '-', SUBSTR(tlno, 8, 4)) as 전화번호
from a
where c>=3
order by user_id desc