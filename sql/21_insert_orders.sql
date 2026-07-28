INSERT INTO orders
(
order_number,
customer_id,
order_date,
order_status,
payment_status,
subtotal,
discount_amount,
tax_amount,
shipping_charges,
total_amount
)
VALUES

('ORD202600001',1,'2026-07-01 10:30:00','Delivered','Paid',1199.99,50.00,180.00,20.00,1349.99),

('ORD202600002',2,'2026-07-02 12:15:00','Delivered','Paid',159.99,10.00,24.00,5.00,179.99),

('ORD202600003',3,'2026-07-03 09:45:00','Shipped','Paid',899.99,30.00,135.00,15.00,1019.99),

('ORD202600004',4,'2026-07-04 15:20:00','Pending','Pending',749.99,0.00,112.50,10.00,872.49),

('ORD202600005',5,'2026-07-05 18:05:00','Cancelled','Refunded',179.99,0.00,27.00,0.00,206.99);