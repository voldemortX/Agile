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
    `createtime` timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username),
    PRIMARY KEY (systemname, username)
);

CREATE TABLE `assets`
(
	`assetname` varchar(20),
    `systemname` varchar(50) NOT NULL,
    `val` int NOT NULL,
    `description` text NOT NULL,
    FOREIGN KEY (systemname) REFERENCES systems(systemname),
    PRIMARY KEY (assetname, systemname)
);

CREATE TABLE `vulnerabilities`
(
	`vulname` varchar(20),
    `systemname` varchar(50) NOT NULL,
    `val` int NOT NULL,
    `description` text NOT NULL,
    FOREIGN KEY (systemname) REFERENCES systems(systemname),
    PRIMARY KEY (vulname, systemname)
);

CREATE TABLE `threats`
(
	`threatname` varchar(20),
    `systemname` varchar(50) NOT NULL,
    `val` int NOT NULL,
    `description` text NOT NULL,
    FOREIGN KEY (systemname) REFERENCES systems(systemname),
    PRIMARY KEY (threatname, systemname)
);
