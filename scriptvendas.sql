create table tb_clientes(
   id int primary key auto_increment,
   nome varchar(100),
   email varchar(200)
);

create table tb_produtos(
   id int primary key auto_increment,
   descricao varchar(100),
   preco decimal(6,2),
   estoque int
);

create table tb_pedidos(
  id int primary key auto_increment,
  data date,
  tb_clientes_id int,
  foreign key(tb_clientes_id) references tb_clientes(id)
);

create table tb_carrinhos(
   id int primary key auto_increment,
   tb_pedidos_id int,
   tb_produtos_id int,
   quantidade int,
   foreign key(tb_pedidos_id) references tb_pedidos(id),
   foreign key(tb_produtos_id) references tb_produtos(id)
);