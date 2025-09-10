-- public.users definition

-- Drop table

-- DROP TABLE users;

CREATE TABLE users (
	id int4 GENERATED ALWAYS AS IDENTITY NOT NULL,
	"name" varchar NULL,
	email varchar NOT NULL,
	CONSTRAINT users_pk PRIMARY KEY (id),
	CONSTRAINT users_unique UNIQUE (email)
);


-- sample insert
insert into users (name,email) values ('AAA','aaa.xxx@somecompany.org');
insert into users (name,email) values ('BBB','bbb.xxx@somecompany.org');
insert into users (name,email) values ('CCC','ccc.xxx@somecompany.org');