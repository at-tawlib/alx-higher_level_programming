-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- first column to be called genre and number_of_shows as second column
-- Results sorted in descending order by number of shows linked

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
	FROM tv_genres
	INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY tv_genres.name
	ORDER BY number_of_shows DESC;

