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
select DISTINCT st.s_name "姓名",
(select s.s_score from course c where s.c_id=c.c_id and c.c_id = 01) "语文",
(select s.s_score from course c where s.c_id=c.c_id and c.c_id = 02) "数学",
(select s.s_score from course c where s.c_id=c.c_id and c.c_id = 03) "英语"
from student st
left join score s
on st.s_id = s.s_id;

# GROUP_CONCAT方式
select s.s_id, GROUP_CONCAT(s.s_score separator ',')
from score s
group by s.s_id;

