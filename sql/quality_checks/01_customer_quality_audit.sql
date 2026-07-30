-- 1. Total customers

SELECT
    COUNT(*) AS total_customers
FROM customers;

-- 2. Duplicate email check

SELECT
    email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- 3. Duplicate phone check
select 
    phone_number,
    count(*) as duplicate_count
from customers
group by phone_number
having count(*) > 1;

-- 4. Missing value audit

-- 4. Missing value audit

SELECT
    SUM(
        CASE
            WHEN first_name IS NULL
                 OR TRIM(first_name) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_first_name,

    SUM(
        CASE
            WHEN last_name IS NULL
                 OR TRIM(last_name) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_last_name,

    SUM(
        CASE
            WHEN email IS NULL
                 OR TRIM(email) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_email,

    SUM(
        CASE
            WHEN phone_number IS NULL
                 OR TRIM(phone_number) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_phone,

    SUM(
        CASE
            WHEN gender IS NULL
                 OR TRIM(gender) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_gender
FROM customers;

-- 5. Invalid gender check

SELECT
    gender,
    COUNT(*) AS customer_count
FROM customers
GROUP BY gender
ORDER BY customer_count DESC;

-- 6. Country validation

SELECT
    country,
    COUNT(*) AS customer_count
FROM customers
GROUP BY country
ORDER BY customer_count DESC;

-- 7. Invalid email format

SELECT
    customer_id,
    email
FROM customers
WHERE email NOT LIKE '%@%'
   OR email NOT LIKE '%.%';

   -- 8. Phone number validation

SELECT
    customer_id,
    phone_number
FROM customers
WHERE CHAR_LENGTH(phone_number) <> 10;

-- 8. Phone number validation

SELECT
    customer_id,
    phone_number
FROM customers
WHERE CHAR_LENGTH(phone_number) <> 10;

-- 10. Customer distribution by city

SELECT
    city,
    COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;

-- 11. Customer data quality summary

SELECT

    COUNT(*) AS total_customers,

    COUNT(DISTINCT email) AS unique_emails,

    COUNT(DISTINCT phone_number) AS unique_phones,

    SUM(
        CASE
            WHEN email IS NULL
                 OR TRIM(email) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_emails,

    SUM(
        CASE
            WHEN phone_number IS NULL
                 OR TRIM(phone_number) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_phones

FROM customers;

/*
Customer Data Quality Audit

Checks performed:
1. Total customer count
2. Duplicate emails
3. Duplicate phone numbers
4. Missing values
5. Gender validation
6. Country validation
7. Email format validation
8. Phone number validation
9. Customer distribution by state
10. Customer distribution by city
11. Overall data quality summary
*/