
-- Jawaban 1 revisi --
select p.id ,p."name" ,sum(oi.sale_price) as omset from order_items oi 
inner join orders o on oi.order_id  = o.order_id 
inner join products p on oi.product_id = p.id 
inner join users u on oi.user_id  = u.id 
where o.status = 'Complete' 
group by p.id,p."name" 
order by omset desc limit 5;


-- Jawaban 2 Revisi 
select u.country ,sum(oi.sale_price) as omset from order_items oi 
inner join orders o on oi.order_id  = o.order_id 
inner join products p on oi.product_id = p.id 
inner join users u on oi.user_id  = u.id 
where oi.product_id in ('22927','8429','23546','25348','8300') -- diambil id produk query jawaban 1 di atas
group by u.country  order by omset desc limit 5;


-- =================
-- Jawaban :

select * from (
select distinct p."name",               
       case 
           when length(p."name") < 30 then 'Nama produk sesuai aturan'
           when p."name" ~~* any(array['0%','1%','2%','3%','4%','5%','6%','7%','8%','9%']) then 'Nama produk tidak sesuai aturan'
           else  'Nama produk tidak sesuai aturan'
       end   hasil_validasi 
from products p ) ts order by hasil_validasi asc;

-- cek validasi total --
select hasil_validasi,sum(jumlah) as jumlah from (
select distinct p."name", 1 as jumlah,              
       case 
           when length(p."name") < 30 then 'Nama produk sesuai aturan'
           when p."name" ~~* any(array['0%','1%','2%','3%','4%','5%','6%','7%','8%','9%']) then 'Nama produk tidak sesuai aturan'
           else  'Nama produk tidak sesuai aturan'
       end   hasil_validasi 
from products p ) ts group by hasil_validasi order by hasil_validasi desc;

-- total data sebelum nya / bisa jadi data duplicate
select count(*) from products p ;

-- ====================================================
-- L04
-- =========================================================================

select distinct user_id,email,category,age_transaksi_terakhir from (
select oi.user_id ,u.first_name ,u.email,p."name",p.category ,
oi.created_at,extract(day from now()- oi.created_at) age_transaksi_terakhir,
rank() over(partition by oi.user_id order by oi.created_at  desc) posisi
from order_items oi 
inner join users u on oi.user_id = u.id 
inner join products p on oi.product_id = p.id
where oi.status = 'Complete' 
and extract(day from now()- oi.created_at) > 90
order by oi.user_id ,oi.created_at desc ) dt where posisi = 1 
group by user_id,email,category,age_transaksi_terakhir;


-- ===============================================================================
-- L.05
-- A Jumlah penjualan/omset yang dihasilkan setiap bulannya lebih dari USD 200.000
-- ===============================================================================
select extract(year from o.created_at) as year_order,
       extract(month from o.created_at) as month_order,
       sum(oi.sale_price) as omzet 
from order_items oi 
 inner join orders o on oi.order_id = o.order_id 
 inner join users u on oi.user_id = u.id 
 inner join products p on oi.product_id = p.id 
group by year_order,month_order 
having sum(oi.sale_price) > 200000 ;


-- B. Rata-rata lama proses order dibuat hingga barang dikirim tidak lebih dari 12 JAM. 
-- Rata-rata lama pengiriman di review setiap bulannya
-- ====================================================================================
select extract(year from o.created_at) as year_order,
       extract(month from o.created_at) as month_order,
       avg(extract(hour from (oi.shipped_at - o.created_at))) as avg_hourship,
       max(extract(hour from (oi.shipped_at - o.created_at))) as max_hourship,
       min(extract(hour from (oi.shipped_at - o.created_at))) as min_hourship,
       count(oi.order_id) as count_order_by_month
from order_items oi 
  inner join orders o on oi.order_id = o.order_id 
group by year_order,month_order
having avg(extract(hour from (oi.shipped_at - o.created_at))) <= 12; 


