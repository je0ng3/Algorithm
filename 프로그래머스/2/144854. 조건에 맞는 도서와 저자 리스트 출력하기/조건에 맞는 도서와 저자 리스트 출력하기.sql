select book_id, author.author_name, substring(published_date,1,10)
from book join author on book.author_id = author.author_id
where category like "경제"
order by published_date asc