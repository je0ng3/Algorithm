select a.AUTHOR_ID, AUTHOR_NAME,
    CATEGORY, sum(sales*price) as TOTAL_SALES
from book b join book_sales s on b.book_id = s.book_id
    join author a on a.author_id=b.author_id
where '2021-12-31' < sales_date and sales_date< '2022-02-01'
group by author_id, category
order by author_id asc, category desc