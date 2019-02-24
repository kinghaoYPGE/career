# user, movie, user_movie, movie_style
create table user(
  id int,
  name varchar(20),
  primary key(id)
);
create table movie(
  id int,
  name varchar(20),
  brief varchar(100),
  primary key(id)
);
create table movie_style(
  movie_id int,
  style_id int,
  foreign key(movie_id) references movie(id)
);
create table user_movie(
  user_id int,
  movie_id int,
  foreign key(user_id) references user(id),
  foreign key(movie_id) references movie(id)
);
insert into user values(1,"Tom");
insert into movie values(279,"a","A");
insert into movie values(3494,"b","B");
insert into movie values(3377,"c","C");
insert into movie values(3452,"d","D");
insert into movie values(782,"e","E");
insert into movie values(3421,"f","F");
insert into movie values(2730,"g","G");

insert into movie_style values(279,26);
insert into movie_style values(279,30);
insert into movie_style values(279,32);
insert into movie_style values(279,8);
insert into movie_style values(279,7);
insert into movie_style values(3494,9);
insert into movie_style values(3494,19);
insert into movie_style values(3494,29);
insert into movie_style values(3494,46);
insert into movie_style values(3377,34);
insert into movie_style values(3377,7);
insert into movie_style values(3377,18);
insert into movie_style values(3452,30);
insert into movie_style values(3452,32);
insert into movie_style values(3452,7);
insert into movie_style values(3452,22);
insert into movie_style values(782,30);
insert into movie_style values(782,32);
insert into movie_style values(782,7);
insert into movie_style values(782,1);
insert into movie_style values(782,50);
insert into movie_style values(3421,30);
insert into movie_style values(3421,32);
insert into movie_style values(3421,7);
insert into movie_style values(3421,22);
insert into movie_style values(2730,11);
insert into movie_style values(2730,30);
insert into movie_style values(2730,22);

insert into user_movie  values(1,782);
insert into user_movie  values(1,3421);
insert into user_movie  values(1,2730);