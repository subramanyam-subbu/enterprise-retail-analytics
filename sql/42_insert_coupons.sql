INSERT INTO coupons
(
campaign_id,
coupon_code,
discount_type,
discount_value,
minimum_order_amount,
maximum_discount,
valid_from,
valid_to,
usage_limit
)
VALUES

(1,'SUMMER20','Percentage',20,100,50,'2026-05-01','2026-05-31',1000),

(2,'DIWALI25','Percentage',25,200,100,'2026-10-15','2026-11-05',2000),

(3,'BLACK50','Flat Amount',50,300,NULL,'2026-11-25','2026-11-30',1500),

(4,'XMAS15','Percentage',15,100,75,'2026-12-15','2026-12-31',1200),

(5,'NEWYEAR30','Percentage',30,250,120,'2026-12-28','2027-01-05',1800);