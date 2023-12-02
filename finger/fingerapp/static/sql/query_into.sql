create database finger;

create table finger.users(
fingerid varchar(255) primary key, uuid  varchar(255) unique, entrytime timestamp
);

create table finger.employee(
employee_id varchar(50) primary key,  uuid varchar(255), user_name varchar(255), email varchar(255),
phoneNo varchar(10), address text,
foreign key(uuid) references users(uuid)
);

create table finger.empwrktm(
	id int primary key auto_increment,
	employee_id varchar(50) , user_name varchar(255), 
    mail varchar(255), phoneNo varchar(50),
    inTime timestamp, outTime timestamp, 
    today_date date,
    foreign key(employee_id) references employee(employee_id)
);


select e.employee_id, e.user_name, e.email, sum(timestampdiff(minute, t.inTime, t.outTime)) as hours_of_work 
from finger.empwrktm as t
right join finger.employee as e on t.employee_id = e.employee_id
group by e.employee_id, e.user_name, e.email;


-- salary
select *,
case when hours_of_work is not null then hours_of_work * 1.04
	else 0
end as salary
 from (
select e.employee_id, e.user_name, e.email,
sum(timestampdiff(minute, t.inTime, t.outTime)) as hours_of_work, t.today_date
from finger.empwrktm as t
right join finger.employee as e on t.employee_id = e.employee_id
group by e.employee_id, t.today_date, e.user_name, e.email) as tar
;
;
