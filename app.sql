drop table if exists tickets;
create table tickets (
	id serial,
	class_name text,
	supporter_name text,
	gender text,
	stadium_name text,
	ticket_price text,
	match_name text,
	time_info time,
	date_info date
);

insert into tickets (class_name, supporter_name, gender, stadium_name, ticket_price, match_name, time_info, date_info) 
values
	('Economy', 'Agam', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('VVIP', 'Jose', 'male', 'Jakarta International Stadium', 500000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('VVIP', 'Malik', 'male', 'Jakarta International Stadium', 500000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('VVIP', 'Yoze', 'female', 'Jakarta International Stadium', 500000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Ahmad', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Regular', 'Ammar', 'male', 'Jakarta International Stadium', 250000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Bani', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Regular', 'Furki', 'female', 'Jakarta International Stadium', 250000 , 'Indonesia vs Argentina', '19:00', '2024-10-03'),
	('Economy', 'Busaeri', 'male', 'Jakarta International Stadium', 150000 , 'Indonesia vs Argentina', '19:00', '2024-10-03')
	;
