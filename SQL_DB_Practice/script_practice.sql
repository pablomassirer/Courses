SELECT DISTINCT author_lname FROM books WHERE released_year < 2000;

SELECT * FROM books WHERE author_lname = 'Lahiri';

SELECT title from books WHERE title like 'the%';

SELECT title FROM books WHERE title LIKE '%stories%';

SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1; 

SELECT DISTINCT CONCAT(title, " - ", released_year) as summary FROM books ORDER BY released_year DESC LIMIT 3;

SELECT title, author_lname FROM books WHERE author_lname LIKE "% %";

SELECT title, author_lname FROM books ORDER BY author_lname, title;

SELECT CONCAT('My FAVORITE AUTHOR IS ', author_fname, " ", author_lname, "!") as yell
FROM books ORDER BY author_lname;

SELECT COUNT(DISTINCT author_fname) as qtd_of_authors FROM books;

SELECT DISTINCT author_fname, author_lname FROM books;

SELECT author_fname, author_lname, COUNT(*) as qtd_books FROM books GROUP BY author_fname, author_lname;

SELECT * FROM books;

SELECT DISTINCT author_fname, author_lname FROM books;

SELECT COUNT(*) FROM books;

SELECT released_year, COUNT(*) as qtd_books FROM books GROUP BY released_year;

SELECT SUM(stock_quantity) as qtd_books_stock FROM books;

SELECT author_fname, author_lname, AVG(released_year) as avg_released_year FROM books GROUP BY author_fname, author_lname;

SELECT CONCAT(author_fname, " ", author_lname) as author_name, pages FROM books ORDER BY pages DESC LIMIT 1;

SELECT released_year as 'year', COUNT(*) as '# books', AVG(pages) as 'avg pages' FROM books GROUP BY released_year;

SELECT DATE_FORMAT(NOW(), '%W');

SELECT DATE_FORMAT(NOW(), '%m/%d/%Y'); 

SELECT DATE_FORMAT(NOW(), '%M %D at %h:%i');

SELECT * FROM tweets;

SELECT * FROM books WHERE released_year BETWEEN 2000 AND 2005 AND stock_quantity > 50;

SELECT title, released_year FROM books
WHERE released_year NOT IN 
(2000,2002,2004,2006,2008,2010,2012,2014,2016);

SELECT * FROM books WHERE author_lname in ('Eggers', 'Chabon');


SELECT title, author_lname,
		CASE 
			WHEN title LIKE '%stories%' THEN 'Short Stories'
			WHEN title LIKE '%Just Kids%' or title LIKE '%A Heartbreaking Work%' THEN 'Memoir'
			ELSE 'Novel'
		END as 'Type'
FROM books;

SELECT title, author_lname,
		CASE 
			WHEN COUNT(*) > 1 THEN CONCAT(COUNT(*), ' ', 'books')
			ELSE CONCAT(COUNT(*), ' ', 'book')
		END as COUNT
FROM books GROUP BY author_fname, author_lname;



SELECT * FROM users ORDER BY created_at LIMIT 5; 

SELECT DAYNAME(created_at) AS day, COUNT(*) as most_pop_regist
FROM users GROUP BY day
ORDER BY most_pop_regist DESC LIMIT 2;


SELECT username, 
IFNULL(image_url, 'SEM FOTO') as image_status
FROM users AS u
LEFT JOIN photos AS ph 
ON u.id = ph.user_id
WHERE ISNULL(ph.image_url);


SELECT * FROM users as usr 
JOIN likes l 
ON usr.id =l.user_id;


SELECT first_name, title, grade FROM students as s
JOIN papers as p ON s.id = p.student_id ORDER BY grade DESC;

SELECT first_name, title, grade FROM students as s
LEFT JOIN papers as p ON s.id = p.student_id;



SELECT first_name, IFNULL(title, 'Missing'),  IFNULL(grade, 0) FROM students as s
LEFT JOIN papers as p ON s.id = p.student_id;

SELECT first_name, AVG(grade) as average FROM students s
LEFT JOIN papers p ON s.id = p.student_id 
GROUP BY s.id
ORDER BY average DESC;


SELECT first_name, AVG(grade) as average,
	CASE
	 	WHEN AVG(grade) >= 75 THEN 'PASSING'
	 	ELSE 'FAILING'
	 END as passing_status
FROM students s
LEFT JOIN papers p ON s.id = p.student_id 
GROUP BY s.id
ORDER BY average DESC;



## User that did most likes
SELECT u.username, ph.image_url, COUNT(*) AS qtd_likes 
FROM photos AS ph
JOIN likes AS l 
ON ph.id = l.photo_id
JOIN users AS u 
ON l.user_id = u.id
GROUP BY u.username
ORDER BY qtd_likes DESC 
LIMIT 1;

## User who created the most pop photo and its photo
SELECT 
    username,
    photos.id,
    photos.image_url, 
    COUNT(*) AS total
FROM photos
INNER JOIN likes
    ON likes.photo_id = photos.id
INNER JOIN users
    ON photos.user_id = users.id
GROUP BY photos.id
ORDER BY total DESC
LIMIT 1;


# Avarage of posts made
SELECT (
	(SELECT COUNT(*) FROM users) / 
		(SELECT COUNT(*) FROM photos)
	
) AS avg;	


# Top 5 most used hashtags
SELECT tag_name, COUNT(*) as qtd_appears FROM tags 
JOIN photo_tags AS pht
ON tags.id = pht.tag_id 
JOIN photos AS ph
ON ph.id = pht.photo_id
GROUP BY pht.tag_id
ORDER BY qtd_appears DESC
LIMIT 5;


