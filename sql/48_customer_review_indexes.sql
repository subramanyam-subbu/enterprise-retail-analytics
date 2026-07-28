CREATE INDEX idx_review_customer
ON customer_reviews(customer_id);

CREATE INDEX idx_review_product
ON customer_reviews(product_id);

CREATE INDEX idx_review_rating
ON customer_reviews(rating);

CREATE INDEX idx_review_date
ON customer_reviews(review_date);