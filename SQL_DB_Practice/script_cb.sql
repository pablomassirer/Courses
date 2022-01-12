-- CREATE DATABASE database_name; 	Cria uma banco de dados

-- DROP DATABASE database_name;	  	Exclui uma banco de dados

-- USE DATABASE database_name;    	Seleciona o banco de dados a ser utilizado

-- SHOW DATABASES;					Mostra os bancos de dados já criados

-- SELECT DATABASE();				Mostra o banco de dados selecionado

-- CREATE TABLE table_name(			Cria uma tabela no banco de dados selecionado
-- 	
--  first_column datatype,
--  second_column datatype	
--	...
-- );

-- SHOW TABLES;															Mostra as tabelas já criadas

-- SHOW COLUMNS FROM table_name; || DESC table_name						Mostra com mais detalhes a tabela escolhida na query

-- INSERT INTO table_name(column_name, ...) VALUES (data, ...); 		Sintaxe para inserir dados em uma tabela

-- INSERT INTO table_name 
--             (column_name, column_name) 
-- VALUES      (value, value), 
c
-- SHOW WARNINGS;

--     CREATE TABLE table_name (
--        id_column INT NOT NULL AUTO_INCREMENT,
--        column_name VARCHAR(100),
--        column_name_2 INT,
--        PRIMARY KEY (id)
--    );

-- UPDATE table_name SET table_column = table_value WHERE table_column = table_value

-- DELETE FROM table_name WHERE column_name = column_value || DELETE FROM table_name

-- SELECT CONCAT(column_name, ' ', column_name) AS alias FROM table_name;

-- SELECT column_name AS alias, column_name AS alias, 
--      CONCAT(column_name, ' ', column_name) AS alias FROM table_name;

-- SELECT CONCAT_WS(separator, column_name, column_name, ...) FROM table_name;

-- SELECT SUBSTRING(value, start, end) - optional -> FROM table_name 

-- SELECT DISTINCT table_column, table_column from table_name;					

