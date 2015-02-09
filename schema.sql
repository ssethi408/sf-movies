drop table if exists films;
create table films (
  id integer primary key autoincrement,
  title text not null,
  release text not null,
  locations text not null,
  fun_facts text not null,
  production text not null,
  distributor text not null,
  director text not null,
  writer text not null,
  actor1 text,
  actor2 text,
  actor3 text 
);
