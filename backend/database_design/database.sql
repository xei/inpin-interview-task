CREATE DATABASE inpin_db;
USE inpin_db;

CREATE TABLE `agency` (
	`id` bigint(20) NOT NULL AUTO_INCREMENT,
	`parent_id` bigint(20) DEFAULT NULL,
	`name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
	PRIMARY KEY (`id`),
	KEY `fkIdx_1` (`parent_id`),
	CONSTRAINT `sub_agency` FOREIGN KEY `fkIdx_1` (`parent_id`) REFERENCES `agency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `ad` (
	`id` bigint(20) NOT NULL AUTO_INCREMENT,
	`agency_id` bigint(20) NOT NULL,
	`name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
	`latitude` DECIMAL(10, 8),
	`longitude` DECIMAL(11, 8),
	PRIMARY KEY (`id`),
	KEY `fkIdx_2` (`agency_id`),
	CONSTRAINT `has` FOREIGN KEY `fkIdx_2` (`agency_id`) REFERENCES `agency` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;