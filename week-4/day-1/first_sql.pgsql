--List the users who registered in 2018 with a .com email address and living in China--

select username, date_of_registration from users
where extract (year from date_of_registration) = 2018 and email like '%.com'

-- how many user --
SELECT DISTINCT username from users

--How many users registered in 2019?--
SELECT username, date_of_registration from users
where EXTRACT(year from date_of_registration) = 2019 

--How many users registered in January?--
SELECT username, date_of_registration from users
where EXTRACT(MONTH from date_of_registration) = 1

--Which country has the most users?--
SELECT country, count(username) as count_user from users
GROUP by country
order by count_user desc

--What is the gender ratio--
SELECT DISTINCT gender, count(username) from users
GROUP by gender

--How many users left at least one field blank
SELECT username from users
where id is NULL
or email  is NULL
or date_of_registration is NULL
or first_name is NULL
or last_name is NULL
or country is NULL
or gender is NULL

--Which are the 3 most expensive products?
SELECT name, price from products
order by price DESC
LIMIT 3

--Which are the 4th and 5th cheapest products
SELECT name, price from products
order by price ASC
LIMIT 2 offset 

--What is the average price for an electric product?
SELECT category, avg(price) as average_price from products
where category = 'Electronics'
group by category

--How much would it cost me to buy all the toys
SELECT category, sum(price) as total_cost from products
where category = 'Toys'
group by category

--What is the average rating?
SELECT avg(rating) as average_rating from reviews

--Which product has the best average rating
SELECT product_id, avg(rating) as average_rating from reviews
group by product_id 
order by average_rating DESC

--Which product has the worst rating
SELECT product_id, avg(rating) as average_rating from reviews
group by product_id 
order by average_rating ASC

--Which products have no review?
SELECT product_id from reviews
where comment is NULL

--How many reviews are 3 or below without comment?
SELECT product_id, count(comment) as num_of_comment FROM reviews
group by product_id
HAVING COUNT(comment) < 3

--Which user reviewed the most?
SELECT product_id, count(comment) as num_of_comment FROM reviews
group by product_id
HAVING COUNT(comment) < 3
order by num_of_comment DESC

--List the average rating for each product
SELECT  product_id, avg(rating) from reviews
GROUP by product_id

--How many days passed since the last review?
SELECT AGE(NOW(), date) as time_passed from reviews
order by time_passed asc
LIMIT 1

-- or 
SELECT DATE_PART('day', NOW() - date) as time_passed from reviews
order by time_passed asc
LIMIT 1











