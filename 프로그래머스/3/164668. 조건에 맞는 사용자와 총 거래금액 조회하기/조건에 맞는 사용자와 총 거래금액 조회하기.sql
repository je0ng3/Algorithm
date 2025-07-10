select USER_ID, NICKNAME, sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD b join USED_GOODS_USER u
on b.WRITER_ID=u.USER_ID
where `STATUS`="DONE"
group by WRITER_ID
having sum(PRICE)>=700000
order by sum(PRICE) asc