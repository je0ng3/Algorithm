-- 코드를 입력하세요
SELECT p.MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(review_date, "%Y-%m-%d") as REVIEW_DATE
from member_profile p join rest_review r on p.member_id=r.member_id
where p.member_id like (
    select member_id
    from rest_review
    group by member_id
    order by count(review_id) desc
    limit 1
)
order by review_date asc, review_text asc