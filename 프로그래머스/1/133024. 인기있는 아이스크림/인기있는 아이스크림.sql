-- 총주문량을 기준으로 내림차순 정렬하고 총주문량이 같다면 출하 번호를 기준으로 오름차순 정렬하여 조회
SELECT FLAVOR
FROM FIRST_HALF 
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC
