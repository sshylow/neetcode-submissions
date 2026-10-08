-- Write your query below

select s.name
FROM sales_person s
LEFT JOIN orders o
    ON s.sales_id = o.sales_id
LEFT JOIN company c
    ON o.com_id = c.com_id
GROUP BY s.sales_id, s.name
having sum(case when c.name ='CRIMSON' then 1 else 0 end) = 0
