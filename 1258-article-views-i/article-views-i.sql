# Write your MySQL query statement below
select
case when author_id = viewer_id then author_id 
end as id

from Views
group by id
having id is not null
order by id asc