# 0x0E. SQL - More queries

| Code | Function | Option |
|--|--| ----- |
| [0-privileges.sql](0-privileges.sql) | lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`) |  |
| [1-create_user.sql](1-create_user.sql) | creates the MySQL server user `user_0d_1` | all privileges and password set to `user_0d_1_pwd` |
| [2-create_read_user.sql](2-create_read_user.sql) | creates the database  `hbtn_0d_2`  and the user  `user_0d_2` | Grant `SELECT` privilege to the user. If database and user already exists, script should not fail |
| [3-force_name.sql](3-force_name.sql) | creates the table `force_name` on your MySQL server | `id` as `INT` with default value of 1 and `name` as `VARCHAR` |
| [4-never_empty.sql](4-never_empty.sql) | creates the table `id_not_null` on your MySQL server | `id` as `INT` and default value `1` and `name` as `VARCHAR`  |
| [5-unique_id.sql](5-unique_id.sql) | creates the table `unique_id` with a `unique id` |  |
| [6-states.sql](6-states.sql) | creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) |  |
| [7-cities.sql](7-cities.sql) | creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) with `unique id`, `primary key`, `foreign key` |  |
| [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) | lists all `cities` of `California` that can be found in the database  | `states` table contain record of `California` and results must be sorted in ascending order by `cities` |
| [9-cities_by_state_join.sql](9-cities_by_state_join.sql) | lists all cities contained in the database `hbtn_0d_usa` | Each record should display:  `cities.id`  -  `cities.name`  -  `states.name` Results must be sorted in ascending order by  `cities.id` |
| [10-genre_id_by_show.sql](10-genre_id_by_show.sql) | lists all shows contained in `hbtn_0d_tvshows`([download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")) that have at least one genre linked | record displays: `tv_shows.title` - `tv_show_genres.genre_id` and results sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id` |
| [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) | lists all shows contained in the database `hbtn_0d_tvshows` | -   Each record should display:  `tv_shows.title`  -  `tv_show_genres.genre_id`  and sorted in ascending order by  `tv_shows.title`  and  `tv_show_genres.genre_id` and if a show doesn’t have a genre, display  `NULL` |
| [12-no_genre.sql](12-no_genre.sql) | lists all shows contained in `hbtn_0d_tvshows` without a genre linked | Each record should display:  `tv_shows.title`  -  `tv_show_genres.genre_id` | and Results must be sorted in ascending order by  `tv_shows.title`  and  `tv_show_genres.genre_id`
| [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) | lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each | Each record should display:  `<TV Show genre>`  -  `<Number of shows linked to this genre>` |
| [14-my_genres.sql](14-my_genres.sql) | uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter` |  |
| [15-comedy_only.sql](15-comedy_only.sql) | lists all Comedy shows in the database `hbtn_0d_tvshows` |  |
| [16-shows_by_genre.sql](16-shows_by_genre.sql) | lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows` |  |

> Written with [StackEdit](https://stackedit.io/).
