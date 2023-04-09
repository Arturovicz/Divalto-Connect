create database erp215;
use erp215;
show tables;


create table if not exists main_articles(
	order_id int,
    prod_ref varchar(50),
    prod_id int,
    prod_label varchar(100),
    order_number int,
    order_date date,
    order_quantity int,
    order_price float,
    delivery_number int,
    delivery_date date,
    delivery_quantity int
);

create table if not exists main_plot(
	prod_id int,
    prod_label varchar(100),
    stock_date date,
    stock_quantity int,
    stock_reserved int
    foreign key (prod_id) references main_articles(prod_id)
);


create table if not exists auth_user(
    id int primary key,
    password varchar(150),
    last_login date,
    is_superuser tinyint(1),
    username varchar(150),
    first_name varchar(150),
    last_name varchar(150),
    email varchar(255),
    is_staff tinyint(1),
    is_active tinyint(1),
    date_joined datetime
);



select * from main_articles ORDER BY order_id desc limit 200;
select * from main_plot ORDER BY stock_date desc limit 500;
select * from main_articles;
select * from main_plot;
drop table main_articles, main_plot;


SELECT prod_id, COUNT(*) AS count
FROM after_corr2
GROUP BY prod_label;

SELECT *
FROM after_corr1
JOIN after_corr2 ON after_corr1.prod_label = after_corr2.prod_label
LIMIT 100;

SELECT *
FROM after_corr1
JOIN after_corr2 ON after_corr1.prod_label = after_corr2.prod_label
ORDER BY prod_ref DESC
LIMIT 100;



select * from after_corr2 where prod_id=1075;
select * from after_corr2 where prod_label="Bicycle Frame";


create table after_corr1(
	order_id int,
    prod_ref varchar(50),
    prod_label varchar(100),
    company varchar(50),
    order_number int,
    order_date date,
    order_quantity int,
    order_price float,
    delivery_number int,
    delivery_date date,
    delivery_quantity int
);

drop table main_table1, main_table2;
create table after_corr2(
	prod_id int,
    prod_ref varchar(50),
    prod_label varchar(100),
    prod_cost int,
    company varchar(10),
    stock_date date,
    stock_quantity int,
    stock_reserved int,
    still_in_stock int
);