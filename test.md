测试语句：

SELECT name,age FROM staff_table WHERE age > 22
SELECT  * FROM staff_table WHERE dept = 'IT'
SELECT * FROM staff_table WHERE enroll_date LIKE '2013'
INSERT INFO staff_table VALUES ('Alex Zhou','18','13789456129','IT','2016-01-01')
DELETE FROM staff_table staff_id = '2'
UPDATE staff_table SET dept = 'Market' WHERE dept = 'IT'

=================================================================================================

测试结果：

>>SELECT name,age FROM staff_table WHERE age > 22
--------------------------------------------------
Alex Zhou     26
Alex Wang     30
Alex Liu      28
Bo Li         25
--------------------------------------------------
共计：4 条
>>SELECT  * FROM staff_table WHERE dept = 'IT'
--------------------------------------------------
1 Alex Zhou 26 13789456123 IT 2016-01-01
4 Alex Liu 28 13789456123 IT 2016-01-08
--------------------------------------------------
共计：2 条
>>SELECT * FROM staff_table WHERE enroll_date LIKE '2013'
--------------------------------------------------
2 Alex Li 20 13789456123 Market 2013-01-01
3 Alex Wang 30 13789456123 HR 2013-01-08
5 Bo Li 25 13789456123 Market 2013-01-02
--------------------------------------------------
共计：3 条
>>INSERT INFO staff_table VALUES ('Alex Zhou','18','13789456129','IT','2016-01-01')
Add success
>>DELETE FROM staff_table staff_id = '2'
Delete success
>>UPDATE staff_table SET dept = 'Market' WHERE dept = 'IT'
Update success
>>q

Process finished with exit code 0
