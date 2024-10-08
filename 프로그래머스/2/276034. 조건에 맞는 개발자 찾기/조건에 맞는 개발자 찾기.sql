-- DEVELOPERS 테이블에서 Python이나 C# 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회
SELECT DISTINCT(D.ID), D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN SKILLCODES AS S ON D.SKILL_CODE & S.CODE
WHERE NAME='C#' OR NAME='Python'
ORDER BY ID

# SELECT DISTINCT(ID), EMAIL, FIRSTNAME, LASTNAME
# FROM DEVELOPERS JOIN SKILLCODES ON DEVELOPERS.SKILL_CODE & SKILLCODES.CODE
# WHERE NAME="C#" OR NAME="Python"
# ORDER BY ID