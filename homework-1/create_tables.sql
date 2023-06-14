-- SQL-команды для создания таблиц
>psql -U postgres
password... 

createdb -U postgres north
password...

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(150),
	title varchar(200),
	birth_date date,
	notes varchar(2000)
);

CREATE TABLE customers
(
	customer_id	text PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(150)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id text references customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(100)
);
