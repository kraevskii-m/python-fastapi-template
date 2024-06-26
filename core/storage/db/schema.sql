begin;

create extension if not exists "uuid-ossp";
drop table if exists api_profile;
drop type if exists role;

create type role as enum ('admin', 'guest', 'junior', 'expert', 'worker');

create table if not exists api_profile
(
    id           uuid primary key default uuid_generate_v4(),
    username     varchar(32)  not null,
    password     varchar(256) not null,
    email        varchar(128) not null,
    phone_number varchar(16)  not null,
    first_name   varchar(32),
    last_name    varchar(32),
    photo_url    text,
    role         role             default 'guest',
    is_internal  bool             default false
);

commit;
