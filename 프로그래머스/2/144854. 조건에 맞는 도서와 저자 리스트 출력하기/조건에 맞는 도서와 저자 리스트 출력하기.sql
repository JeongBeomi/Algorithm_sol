-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") FROM BOOK a
JOIN AUTHOR b ON a.AUTHOR_ID = b.AUTHOR_ID
WHERE CATEGORY = "경제"
ORDER BY PUBLISHED_DATE