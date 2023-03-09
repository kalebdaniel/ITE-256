SELECT song.song_id, song.song_topname, artist.artist_id, artist.song_artist                                            
FROM song                                                                                                                         
INNER JOIN artist                                                                                                                 
ON song.song_id = artist.artist_id                                                                                                
ORDER BY song.song_id;

SELECT song.song_id, song.song_topname, artist.artist_id AS artist
FROM song
LEFT JOIN artist 
ON song.song_id = artist.artist_id
ORDER BY song.song_id;

SELECT song.song_id, song.song_topname, artist.artist_id AS artist
FROM song
RIGHT JOIN artist
ON song.song_id = artist.artist_id
ORDER BY song.song_id;

SELECT song.song_id, song.song_topname, artist.artist_id AS artist
FROM song
FULL JOIN artist
ON song.song_id = artist.artist_id
ORDER BY song.song_id;

SELECT song.song_id, song.song_topname, artist.artist_id AS artist
FROM song
CROSS JOIN artist
ON song.song_id = artist.artist_id
ORDER BY song.song_id;
