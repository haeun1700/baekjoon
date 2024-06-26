-- 재구매한 회원 ID와 재구매한 상품 ID를 출력
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC