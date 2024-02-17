select title, u.board_id, reply_id, r.writer_id, r.contents, substring_index(r.created_date,' ',1)
from used_goods_board u join used_goods_reply r on u.board_id = r.board_id
where u.created_date like "2022-10%"
order by  r.created_date, title