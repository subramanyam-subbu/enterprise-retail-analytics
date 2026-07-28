CREATE INDEX idx_tracking_shipment
ON shipment_tracking(shipment_id);

CREATE INDEX idx_tracking_status
ON shipment_tracking(tracking_status);

CREATE INDEX idx_tracking_event_time
ON shipment_tracking(event_time);

CREATE INDEX idx_tracking_location
ON shipment_tracking(tracking_location);