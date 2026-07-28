/*
===========================================================
File Name   : 35_create_shipment_tracking.sql
Module      : Shipping Management
Project     : Enterprise Retail Analytics Platform
Description : Stores shipment tracking history.
===========================================================
*/

USE enterprise_retail_analytics;

CREATE TABLE shipment_tracking (

    tracking_event_id INT AUTO_INCREMENT PRIMARY KEY,

    shipment_id INT NOT NULL,

    tracking_status ENUM(
        'Shipment Created',
        'Picked Up',
        'In Transit',
        'Arrived At Hub',
        'Out For Delivery',
        'Delivered',
        'Delivery Failed',
        'Returned'
    ) NOT NULL,

    tracking_location VARCHAR(150),

    remarks VARCHAR(500),

    event_time DATETIME NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_tracking_shipment
        FOREIGN KEY (shipment_id)
        REFERENCES shipments(shipment_id)
        ON DELETE CASCADE
);