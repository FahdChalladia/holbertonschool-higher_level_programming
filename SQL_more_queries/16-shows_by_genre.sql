-- List all shows and all genres they belong to
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- Left join to show even those without genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
