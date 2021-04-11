
CREATE TABLE product(
	product_id int(10) auto_increment primary key,
    name varchar(191) not null,
    product_description varchar(191) not null,
    price double(10,2) not null
)

CREATE TABLE customer(
	customer_id int(10) auto_increment primary key,
    name varchar(191) not null,
    email varchar(191) not null
)

CREATE TABLE `order`(
	order_id int(10) auto_increment primary key,
	customer_id int(10),
    creation_date Date,
    delivery_address varchar(191) not null,
    total double(15,2) not null,
    foreign key order_pk(customer_id) references customer(customer_id)
)

CREATE TABLE order_detail(
	order_detail_id int(10) auto_increment primary key,
	order_id int(10),
	product_id int(10),
    product_description varchar(191) not null,
    price double(10,2) not null,
    quantity int(10) not null,
    foreign key order_fk(order_id) references `order`(order_id),
    foreign key product_fk(product_id) references product(product_id)
)

CREATE TABLE customer_product(
	customer_id int(10),
    product_id int(10),
    foreign key customer_fk(customer_id) references customer(customer_id),
    foreign key product_fk(product_id) references product(product_id)
)