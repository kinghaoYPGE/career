# 查询每个学生学的课程与每门成绩
select stu.s_name "学生名", c.c_name "课程名", s.s_score "分数"
from student stu left JOIN score s
on stu.s_id = s.s_id
left JOIN course c
on s.c_id = c.c_id;

# 行转列(group by和case语句方式)
select st.s_name "姓名",
max(case c.c_id when 01 then s.s_score else 0 end) "语文",
max(case c.c_id when 02 then s.s_score else 0 end)	"数学",
max(case c.c_id when 03 then s.s_score else 0 end)	"英语"
from student st 
left join score s
on st.s_id = s.s_id
left join course c
on s.c_id = c.c_id
GROUP BY st.s_id;

# 行转列(子查询)
select DISTINCT (select s_name from student s where s.s_id = st.s_id) "姓名",
ifnull((select s_score from score ss where ss.s_id = s.s_id and ss.c_id = 01), 0) "语文",
ifnull((select s_score from score ss where ss.s_id = s.s_id and ss.c_id = 02), 0) "数学",
ifnull((select s_score from score ss where ss.s_id = s.s_id and ss.c_id = 03), 0) "英语"
from score s
RIGHT JOIN student st
on s.s_id = st.s_id;

# GROUP_CONCAT方式
select s.s_id, GROUP_CONCAT(s.s_score separator ',')
from score s
group by s.s_id;

