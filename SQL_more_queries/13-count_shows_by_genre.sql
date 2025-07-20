-- Count the number of shows in each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
-- Join genre-show association table
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group by genre name to count shows in each
GROUP BY tv_genres.name
-- Order by count descending
ORDER BY number_of_shows DESC;
