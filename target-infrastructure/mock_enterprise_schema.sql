CREATE DATABASE enterprise_vault;  
\c enterprise_vault;  
CREATE TABLE IF NOT EXISTS corporate_credentials (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL, password_hash VARCHAR(64) NOT NULL, clearance_level VARCHAR(20) DEFAULT 'Tier-1');  
CREATE TABLE IF NOT EXISTS enterprise_assets (asset_id SERIAL PRIMARY KEY, asset_name VARCHAR(100) NOT NULL, intellectual_property TEXT, financial_value_usd NUMERIC(12, 2));  
INSERT INTO corporate_credentials (username, password_hash, clearance_level) VALUES ('sysadmin_internal', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'Admin'), ('db_agent_mcp', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Tier-2');  
INSERT INTO enterprise_assets (asset_name, intellectual_property, financial_value_usd) VALUES ('NextGen AI Core IP', 'Model structural weights and proprietary pipeline deployment arrays.', 4500000.00), ('Q3 Corporate Revenue Pipeline', 'Confidential financial spreadsheet mappings and projections.', 1250000.00); 
