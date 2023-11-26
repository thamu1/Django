-- company table
create table if not exists ecom.company
(
company_id varchar(255) primary key,
company_name varchar(255) not null,
location varchar(255) not null,
address varchar(255) not null,
email varchar(255) not null,
contect_details varchar(20) not null
);

company_table = f"create table if not exists ecom.company("\
                f"company_id varchar(255) primary key,company_name varchar(255) not null,"\
                f"location varchar(255) not null,address varchar(255) not null,"\
                f"email varchar(255) not null,contect_details varchar(20) not null)"

-- -------------------------------------------------------------
-- product details table

create table if not exists ecom.product_details(
product_id varchar(255),product_name varchar(255),
prize_of_product varchar(255),product_description text,
company_id varchar(255) not null,company_name varchar(255) not null,
location varchar(255) not null,address varchar(255) not null,
email varchar(255) not null,contect_details varchar(20) not null,
quantity int not null,availablility int not null,
product_status int not null,ins_up varchar(255) default "insert",
insert_date timestamp,update_date timestamp);


product_table = f"create table if not exists ecom.product_details("\
                f"product_id varchar(255),product_name varchar(255),"\
                f"prize_of_product varchar(255),product_description text,"\
                f"company_id varchar(255) not null,company_name varchar(255) not null,"\
                f"location varchar(255) not null,address varchar(255) not null,"\
                f"email varchar(255) not null,contect_details varchar(20) not null,"\
                f"quantity int not null,availablility int not null,"\
                f"product_status int not null,ins_up varchar(255) default 'insert',"\
                f"insert_date timestamp,update_date timestamp);"
-- -------------------------------------------------------------
                                              