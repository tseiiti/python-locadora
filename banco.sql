-- Active: 1692452936450@@127.0.0.1@5432@oscar@public
drop table if exists alugar;
drop table if exists cliente;
drop table if exists dupla;
drop table if exists fita;
drop table if exists atuar;
drop table if exists ator;
drop table if exists filme;
drop table if exists categoria;

create table categoria (
	id						serial, 
	nome					varchar(255) not null, 
	constraint categoria_pk primary key (id)
);

create table filme (
	id						serial, 
	titulo				varchar(255) not null, 
	categoria_id	int not null, 
	constraint filme_pk primary key (id), 
	constraint categoria_fk foreign key (categoria_id) references categoria(id)
);

create table ator (
	id						serial, 
	nome_real			varchar(255), 
	data_nasc			date, 
	constraint ator_pk primary key (id)
);

create table atuar (
	filme_id			int not null, 
	ator_id				int not null, 
	personagem		varchar(255) not null, 
	estrela				boolean, 
	constraint atuar_pk primary key (filme_id, ator_id), 
	constraint filme_fk foreign key (filme_id) references filme(id), 
	constraint ator_fk foreign key (ator_id) references ator(id)
);

create table fita (
	id						serial, 
	filme_id			int not null, 
	constraint fita_pk primary key (id), 
	constraint filme_fk foreign key (filme_id) references filme(id)
);

create table dupla (
	fita_id_1			int not null, 
	fita_id_2			int not null, 
	constraint dupla_pk primary key (fita_id_1, fita_id_2), 
	constraint fita_fk_1 foreign key (fita_id_1) references fita(id), 
	constraint fita_fk_2 foreign key (fita_id_2) references fita(id)
);

create table cliente (
	id						serial, 
	nome					varchar(255) not null, 
	sobrenome			varchar(255) not null, 
	telefone			varchar(255) not null, 
	endereco			varchar(255) not null, 
	constraint cliente_pk primary key (id)
);

create table alugar (
	fita_id				int not null, 
	cliente_id		int not null, 
	constraint alugar_pk primary key (fita_id, cliente_id), 
	constraint fita_fk foreign key (fita_id) references fita(id), 
	constraint cliente_fk foreign key (cliente_id) references cliente(id), 
	unique(fita_id)
);




-- Dados iniciais de exemplo:

insert into categoria (nome) values ('Ação');
insert into categoria (nome) values ('Comédia');
insert into categoria (nome) values ('Drama');
insert into categoria (nome) values ('Ficção científica');

insert into filme (titulo, categoria_id) values ('Mad Max: A estrada da fúria', 1);
insert into filme (titulo, categoria_id) values ('Mulheres à Beira de um Ataque de Nervos', 2);
insert into filme (titulo, categoria_id) values ('Central do Brasil', 3);
insert into filme (titulo, categoria_id) values ('Matrix', 4);

insert into ator (nome_real, data_nasc) values ('Tom Hardy', '1977-09-15');
insert into ator (nome_real, data_nasc) values ('Charlize Theron', '1975-08-07');
insert into ator (nome_real, data_nasc) values ('Carmen Maura', '1945-09-15');
insert into ator (nome_real, data_nasc) values ('Antonio Banderas', '1960-08-10');
insert into ator (nome_real, data_nasc) values ('Fernanda Montenegro', '1929-10-16');
insert into ator (nome_real, data_nasc) values ('Vinícius de Oliveira', '1985-07-18');
insert into ator (nome_real, data_nasc) values ('Keanu Reeves', '1964-09-02');
insert into ator (nome_real, data_nasc) values ('Carrie-Anne Moss', '1967-08-21');
insert into ator (nome_real, data_nasc) values ('Laurence Fishburne', '1961-07-30');

insert into atuar (filme_id, ator_id, personagem, estrela) values (1, 1, 'Max Rockatansky', true);
insert into atuar (filme_id, ator_id, personagem, estrela) values (1, 2, 'Imperator Furiosa', false);
insert into atuar (filme_id, ator_id, personagem, estrela) values (2, 3, 'Pepa', true);
insert into atuar (filme_id, ator_id, personagem, estrela) values (2, 4, 'Carlos', false);
insert into atuar (filme_id, ator_id, personagem, estrela) values (3, 5, 'Dora', true);
insert into atuar (filme_id, ator_id, personagem, estrela) values (3, 6, 'Josué', false);
insert into atuar (filme_id, ator_id, personagem, estrela) values (4, 7, 'Neo', true);
insert into atuar (filme_id, ator_id, personagem, estrela) values (4, 8, 'Trinity', false);
insert into atuar (filme_id, ator_id, personagem, estrela) values (4, 9, 'Morpheus', false);

insert into fita (filme_id) values (1);
insert into fita (filme_id) values (1);
insert into fita (filme_id) values (2);
insert into fita (filme_id) values (2);
insert into fita (filme_id) values (2);
insert into fita (filme_id) values (3);
insert into fita (filme_id) values (3);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);
insert into fita (filme_id) values (4);

insert into dupla (fita_id_1, fita_id_2) values (8, 9);
insert into dupla (fita_id_1, fita_id_2) values (10, 11);
insert into dupla (fita_id_1, fita_id_2) values (12, 13);
insert into dupla (fita_id_1, fita_id_2) values (14, 15);

insert into cliente (nome, sobrenome, telefone, endereco) values ('oscar', 'teste', '11-99999-9999', 'rua tal, 54 jardims');
insert into cliente (nome, sobrenome, telefone, endereco) values ('joao', 'teste', '11-88888-8888', 'rua tal, 88 jardims');
insert into cliente (nome, sobrenome, telefone, endereco) values ('paulo', 'teste', '11-77777-7777', 'rua tal, 77 jardims');
insert into cliente (nome, sobrenome, telefone, endereco) values ('josé', 'teste', '11-66666-6666', 'rua tal, 66 jardims');

insert into alugar (fita_id, cliente_id) values (8, 1);
insert into alugar (fita_id, cliente_id) values (9, 1);
insert into alugar (fita_id, cliente_id) values (1, 1);
insert into alugar (fita_id, cliente_id) values (3, 1);
