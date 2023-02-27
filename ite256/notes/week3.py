<title>Page 55 through 63 Curious Moon Notes</title>

	<h1>Lookup Tables</h1>

	- Dee begins off the page of her mentioning how she is needed to get the values for each of her 
lookup tables.

	select distint(team)
	as description
	into teams
	from import.master_plan;

	- Dee is now needed to add her primary key.

	alter table teams
	add id serial primary key;

	- Next she notices that she needs to relate her lookup table back to an events table she made in 
the past so she can tell where the values of the lookup ids to go but one thing about that is that she 
doesn't know how to do that! That is where Mr. Sullivan comes in to help.

	- Mr. Sullivan mentions that the way Dee tried to join her two tables was a time consuming and 
slow method but a faster way Mr. Sullivan mentions is that she can insert her events from her import 
table and set all her ids at once and ending her events with inner joins which is a join I believe we 
all were working on last week because all it really was is combining two tables into one with the data 
as well being formed into one table.

	<h1>Joins</h1>

	- After Dee trys out Mr. Sullivan's sql advice, it successfully runs but she notices that theres 
a problem and that problem is that there was supposed to be 61,873 rows that get imported but only 
48,627 were imported. Dee decides to sleep on the problem and just work on it the next day.

	- The next day, Dee solves the problem and notices what was wrong; it was the joins and because 
inner joins weren't going to work out, she decided to go with left joins which returns the data/rows 
from the left side of the table and fill in the missing rows with nulls.

	- Dee states that there are five joins you can do and those five are defined below.

- Inner Join
This is what Mr. Sullivan was using and what this join does is return just the results 
where there are matching rows in the join table to combine it all into one table.

- Left Join
This will return all the rows & records from the left side of the table and fill out the missing 
rows (the right side) with nulls.

- Right Join
This is like a left join but flipped this time meaning it will return all the rows & records from the 
right side of the table and fill out the left side with nulls.

- Full outer join
A Full outer join does both a left and right join at the same time which is pretty much just returning 
rows from both tables.

- Odd cross join
An Odd cross join returns every row and joins from a table crossed with every row in the other table 
meaning if a from table had five rows and the join table had two rows, it would multiply together and 
have a total of ten records/rows returned. This is a join not really many people work with but there can 
be some situations where a join like this is significant.

	- After giving the script another run, Dee successfully inserts all 61,873 rows.   
