# If tables already exist, just drop all of them
DROP TABLE IF EXISTS `threats`;
DROP TABLE IF EXISTS `vulnerabilities`;
DROP TABLE IF EXISTS `assets`;
DROP TABLE IF EXISTS `systems`;
DROP TABLE IF EXISTS `users`;

# Create new tables
# Implement cascade DELETE via foreign keys
# No unit tests for this directly
# However, these queries are tested on python library level
CREATE TABLE `users`
(
	`username` varchar(20) PRIMARY KEY,
    `password` varchar(40) NOT NULL
);

CREATE TABLE `systems`
(
	`systemname` varchar(50) NOT NULL UNIQUE,
    `username` varchar(20) NOT NULL,
    `method` varchar(20) NOT NULL,
    `results` text NOT NULL,
    `description` text NOT NULL,
    `createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE,
    PRIMARY KEY (systemname, username)
);

CREATE TABLE `assets`
(
	`assetname` varchar(20),
    `systemname` varchar(50) NOT NULL,
    `val` int NOT NULL,
    `description` text NOT NULL,
    FOREIGN KEY (systemname) REFERENCES systems(systemname) ON DELETE CASCADE,
    PRIMARY KEY (assetname, systemname)
);

CREATE TABLE `vulnerabilities`
(
	`vulname` varchar(20),
    `systemname` varchar(50) NOT NULL,
    `val` int NOT NULL,
    `description` text NOT NULL,
    FOREIGN KEY (systemname) REFERENCES systems(systemname) ON DELETE CASCADE,
    PRIMARY KEY (vulname, systemname)
);

CREATE TABLE `threats`
(
	`threatname` varchar(20),
    `systemname` varchar(50) NOT NULL,
    `val` int NOT NULL,
    `description` text NOT NULL,
    FOREIGN KEY (systemname) REFERENCES systems(systemname) ON DELETE CASCADE,
    PRIMARY KEY (threatname, systemname)
);
