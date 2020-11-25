create table publishers(
    publisher_id int primary key auto_increment,
    publisher_name varchar(64) unique  not null
);

create table authors(
    author_id int primary key auto_increment,
    first_name varchar(32) not null,
    last_name varchar(32) not null
);

create table books(
    isbn_13 char(13) primary key,
    title varchar(64) not null,
    author_fk int,
    publisher_fk int,
    date_published date not null,
    price int not null,
    foreign key (publisher_fk) references publishers (publisher_id),
    foreign key (author_fk) references authors (author_id)
);

create table copies(
    copy_id char(36) primary key,
    isbn_13_fk char(13),
    date_acquired date not null,
    foreign key (isbn_13_fk) references books (isbn_13)
);

create table membership_plans(
    id int primary key auto_increment,
    title varchar(32) unique not null,
    borrow_limit int not null,
    annual_fee int not null,
    fine_per_day int not null
);

create table members(
    member_id char(36) primary key,
    first_name varchar(32) not null,
    last_name varchar(32) not null,
    doj date not null,
    email varchar(64) unique not null,
    gender enum('Male', 'Female'),
    membership_fk int,
    expiry_date date not null,
    dob date not null,
    foreign key (membership_fk) references membership_plans (id)
);

create table staff_permissions(
    id int primary key auto_increment,
    title varchar(32) unique not null,
    manage_member boolean,
    manage_staff boolean,
    manage_books boolean,
    manage_issues boolean,
    salary int not null
);

create table staff(
    staff_id char(36) primary key,
    first_name varchar(32) not null,
    last_name varchar(32) not null,
    dob date not null,
    doj date not null,
    gender enum('Male', 'Female'),
    permission_fk int,
    email varchar(64) not null,
    foreign key (permission_fk) references staff_permissions (id)
);

create table issues(
    issue_id int primary key auto_increment,
    copy_id_fk char(36),
    issued_by char(36),
    issued_on date not null,
    issued_to char(36),
    due_on date not null,
    fine int default 0,
    active boolean default 1,
    foreign key (copy_id_fk) references copies (copy_id),
    foreign key (issued_by) references staff (staff_id),
    foreign key (issued_to) references members (member_id) on update cascade
);

delimiter $$

create event update_fines
on schedule every 1 day starts timestamp(curdate())
do begin
    update issues
    set fine = datediff(curdate(), due_on) * (
        select fine_per_day from membership_plans 
        where id = (
            select membership_fk from members 
            where member_id = issued_to
        )
    )
    where due_on < curdate();
end$$

create event expire_members
on schedule every 1 day starts timestamp(curdate())
do begin
    update members
    set membership_fk = 1
    where expiry_date < curdate();
end$$

delimiter ;
