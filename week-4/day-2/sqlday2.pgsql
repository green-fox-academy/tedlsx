select title from movie
where director = 'Steven Spielberg'


select distinct year from movie 
left join rating on movie.mID = rating.mID
where stars between 4 and 5
order by year asc

select title from movie
left join rating on rating.mID = movie.mID 
where stars is Null

select name from reviewer
inner join rating on rating.rID = reviewer.rID
where ratingdate is Null















select title, max(stars) from movie
inner join rating on rating.mID = movie.mID
group by title
order by title asc

select title, (max(stars)-min(stars)) as rating_spread from movie
inner join rating on rating.mID = movie.mID
group by title
order by rating_spread desc



--Q1
select distinct name from reviewer
inner join rating on rating.rID = reviewer.rID
inner join movie on movie.mID = rating.mID
where title = 'Gone with the Wind'

--Q2  
select name, title, stars from movie
inner join rating on rating.mID = movie.mID
inner join reviewer on reviewer.rID = rating.rID
where name = director


--view
drop view if EXISTS name_review;

CREATE view name_review as
select distinct name, count(stars) from reviewer
inner join rating on rating.rid = reviewer.rid
group by name;

select * from name_review;

drop view if EXISTS noreview;

CREATE VIEW noreview as
select distinct title from movie
left join rating on rating.mid = movie.mid
where stars is NULL;

SELECT * from noreview

CREATE view all_director as
select distinct director from movie
where director is not NULL;

select * from all_director

create view title_rating as
select title, avg(stars) from movie
inner join rating on rating.mid = movie.mid
group by title;

select * from title_rating



select starttime from cd.bookings
inner join cd.members on cd.members.memid = cd.bookings.memid
where surname = 'Farrell' and firstname = 'David'

select starttime, name from cd.bookings
inner join cd.facilities on cd.facilities.facid = cd.bookings.facid
where extract(year from starttime) = '2012'
	and extract(month from starttime) = '09'
	and extract(day from starttime) = '21'
	and name like 'Tennis Court%'
order by starttime asc

select mems.firstname as memfname, mems.surname as memsname, recs.firstname as recname, recs.surname as resname
from cd.members mems left join cd.members recs on recs.memid = mems.recommendedby
order by memsname, memfname

select distinct firstname ||' '|| surname as fullname, name
from cd.members 
inner join cd.bookings on cd.bookings.memid = cd.members.memid
inner join cd.facilities on cd.bookings.facid = cd.facilities.facid
where cd.facilities.facid in (0, 1)
order by fullname

select mems.firstname || ' ' || mems.surname as member, 
	facs.name as facility, 
	case 
		when mems.memid = 0 then
			bks.slots*facs.guestcost
		else
			bks.slots*facs.membercost
	end as cost
        from
                cd.members mems                
                inner join cd.bookings bks
                        on mems.memid = bks.memid
                inner join cd.facilities facs
                        on bks.facid = facs.facid
        where
		bks.starttime >= '2012-09-14' and 
		bks.starttime < '2012-09-15' and (
			(mems.memid = 0 and bks.slots*facs.guestcost > 30) or
			(mems.memid != 0 and bks.slots*facs.membercost > 30)
		)
order by cost desc; 

select distinct mems.firstname || ' ' ||  mems.surname as member,
	(select recs.firstname || ' ' || recs.surname as recommender 
		from cd.members recs 
		where recs.memid = mems.recommendedby
	)
	from 
		cd.members mems
order by member;


select member, facility, cost from (
	select 
		mems.firstname || ' ' || mems.surname as member,
		facs.name as facility,
		case
			when mems.memid = 0 then
				bks.slots*facs.guestcost
			else
				bks.slots*facs.membercost
		end as cost
		from
			cd.members mems
			inner join cd.bookings bks
				on mems.memid = bks.memid
			inner join cd.facilities facs
				on bks.facid = facs.facid
		where
			bks.starttime >= '2012-09-14' and
			bks.starttime < '2012-09-15'
	) as bookings
	where cost > 30
order by cost desc; 
