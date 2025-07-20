-- List all shows and their associated genre_id (if any)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Left join to include shows without a genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
