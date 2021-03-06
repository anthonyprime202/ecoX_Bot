CREATE TABLE IF NOT EXISTS guilds (
    id BIGINT PRIMARY KEY,  
    currency VARCHAR(10),
    description VARCHAR(255),
    admin BIGINT
);

CREATE TABLE IF NOT EXISTS economy (
    member BIGINT PRIMARY KEY,
    guild BIGINT NOT NULL,
    balance INTEGER DEFAULT 0,
    roles BIGINT[]
);

CREATE TABLE IF NOT EXISTS shops (
    role BIGINT PRIMARY KEY,
    guild BIGINT NOT NULL,
    price INTEGER NOT NULL,
    description VARCHAR(255)
);