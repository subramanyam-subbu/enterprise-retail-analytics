CREATE INDEX idx_shipment_status
ON shipments(shipment_status);

CREATE INDEX idx_shipment_courier
ON shipments(courier_name);

CREATE INDEX idx_shipment_expected_date
ON shipments(expected_delivery_date);

CREATE INDEX idx_shipment_actual_date
ON shipments(actual_delivery_date);