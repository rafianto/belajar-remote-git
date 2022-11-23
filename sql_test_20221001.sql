delete from data_from_csv ;

-- create table ped_crashes (datain varchar);
--alter table ped_crashes  drop COLUMN datain ;
-- select * from ped_crashes pc ;

select * from data_from_csv dfc ;

create table sales082022 as select * from data_from_csv dfc ;
select * from sales082022 s order by s.tanggal desc ;
select count(*) from sales062022 ;
alter table datambs.public.sales082022 drop column textdata;
--alter table datambs.public.sales032022 drop column column121;


select * from sales012022 s ;
select distinct s.supplier  from sales012022 s;
select distinct s.division from sales012022 s;
select distinct s.branch  from sales012022 s ;
select distinct s.cust_group from sales012022 s ;
select distinct s.cust_chain from sales012022 s ;
select distinct s.productgrp  from sales012022 s ;
select distinct s.cust_city from sales012022 s ;
select distinct s.salesman from sales012022 s ;
select distinct s.rom from sales012022 s ;
select distinct s.div_chnl from sales012022 s ;



select * from sales022022 s ;
select distinct s.supplier  from sales022022 s;
select distinct s.division from sales022022 s;
select distinct s.branch  from sales022022 s ;
select distinct s.cust_group from sales022022 s ;
select distinct s.cust_chain from sales022022 s ;
select distinct s.productgrp  from sales022022 s ;

select * from sales032022 s ;
select distinct s.supplier  from sales032022 s;
select distinct s.division from sales032022 s;
select distinct s.branch  from sales032022 s ;
select distinct s.cust_group from sales032022 s ;
select distinct s.cust_chain from sales032022 s ;
select distinct s.productgrp  from sales032022 s ;

create or replace view sales01_05_2022 as
select * from sales012022 s 
union all
select * from sales022022 s2 
union all
select * from sales032022 s3 
union all
select * from sales042022 s4 
union all
select * from sales052022 s5;


union all
select * from sales062022 s6 ;
select * from sales062022 s6 where s6.


select distinct s.branch, to_char(s.trn_month,'99')||to_char(trn_year,'9999') , sum(s.total_hna) as omzet 
from sales2022 s 
group by s.branch ,to_char(s.trn_month,'99')||to_char(trn_year,'9999') 
having s.branch  IN('BDG1','YGY1')
order by s.branch ,to_char(s.trn_month,'99')||to_char(trn_year,'9999');

-- melihat kenaian omset dari bulan sebelum nya per site ( implementasi 3.4.20 refocus )
select *,( omset_hna - ( lag(omset_hna,1) over( partition by branch order by trn_month asc ) )
    ) difference_omset_from_month_before from (
select s.branch , s.trn_month, sum(s.total_hna) omset_hna 
from sales2022 s 
group by s.branch , s.trn_month order by branch ,trn_month) t ;

-- pembelian suatu barang yg paling akhir pada custumer tertentu
-- pembelian barang terakhir per outlet 
select * from (
select s.cust_name,s.product ,s.tanggal, s.sales_qty ,s.total_hna ,
rank() over(partition by s.cust_name,s.product order by s.tanggal desc) posisi
from sales2022  s ) dt where posisi = 1;


