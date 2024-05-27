-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table law_firm_system.case_table
DROP TABLE IF EXISTS `case_table`;
CREATE TABLE IF NOT EXISTS `case_table` (
  `case_id` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `case_name` varchar(255) DEFAULT NULL,
  `case_type` varchar(255) DEFAULT NULL,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(255) DEFAULT NULL,
  `case_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table law_firm_system.case_table: ~4 rows (approximately)
INSERT IGNORE INTO `case_table` (`case_id`, `case_name`, `case_type`, `start_date`, `end_date`, `case_status`) VALUES
	('A01', 'Morgana Logistics vs Samsung', 'Class Action', '01-01-2000', 'To be Determined', 'Ongoing'),
	('R31', 'hannah vs miley', 'Criminal', '05-24-2024', 'To be Determined', 'Ongoing'),
	('T12', 'Ariana Grande vs Nickic Minaj', 'Civil', '01-01-2000', 'To be Determined', 'Open'),
	('Y61', 'demi vs taylor', 'Civil', '01-01-2000', '05-24-2024', 'Pending');

-- Dumping structure for table law_firm_system.client_case_table
DROP TABLE IF EXISTS `client_case_table`;
CREATE TABLE IF NOT EXISTS `client_case_table` (
  `client_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `case_id` varchar(3) NOT NULL,
  PRIMARY KEY (`client_id`,`case_id`) USING BTREE,
  KEY `case_id` (`case_id`),
  CONSTRAINT `fk_case_id` FOREIGN KEY (`case_id`) REFERENCES `case_table` (`case_id`),
  CONSTRAINT `fk_client_id` FOREIGN KEY (`client_id`) REFERENCES `client_table` (`clientID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table law_firm_system.client_case_table: ~1 rows (approximately)
INSERT IGNORE INTO `client_case_table` (`client_id`, `case_id`) VALUES
	('A424', 'R31');

-- Dumping structure for table law_firm_system.client_table
DROP TABLE IF EXISTS `client_table`;
CREATE TABLE IF NOT EXISTS `client_table` (
  `clientID` varchar(50) NOT NULL,
  `clientName` varchar(50) DEFAULT NULL,
  `clientType` varchar(50) DEFAULT NULL,
  `clientEmail` varchar(50) DEFAULT NULL,
  `clientLawyer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`clientID`),
  KEY `clientLawyer` (`clientLawyer`),
  CONSTRAINT `clientLawyer` FOREIGN KEY (`clientLawyer`) REFERENCES `lawyer_table` (`lawyerName`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table law_firm_system.client_table: ~4 rows (approximately)
INSERT IGNORE INTO `client_table` (`clientID`, `clientName`, `clientType`, `clientEmail`, `clientLawyer`) VALUES
	('A3131', 'Jollibee', 'Company', 'jollibee@mail.com', 'Jessica Pearson'),
	('A424', 'John', 'Individual', 'John@gmail.com', 'Jessica Pearson'),
	('A4243', 'hannah montana', 'Individual', 'hannah_montana@gmail.com', 'Jessica Pearson'),
	('F4244', 'Mang Inasal', 'Company', 'mangInasal@mail.com', NULL);

-- Dumping structure for table law_firm_system.lawyer_case_table
DROP TABLE IF EXISTS `lawyer_case_table`;
CREATE TABLE IF NOT EXISTS `lawyer_case_table` (
  `lawyer_id` varchar(5) NOT NULL,
  `case_id` varchar(3) NOT NULL,
  `start_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`lawyer_id`,`case_id`),
  KEY `case_id` (`case_id`),
  CONSTRAINT `case_id` FOREIGN KEY (`case_id`) REFERENCES `case_table` (`case_id`),
  CONSTRAINT `lawyer_id` FOREIGN KEY (`lawyer_id`) REFERENCES `lawyer_table` (`lawyerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table law_firm_system.lawyer_case_table: ~5 rows (approximately)
INSERT IGNORE INTO `lawyer_case_table` (`lawyer_id`, `case_id`, `start_date`) VALUES
	('2424A', 'A01', '01-01-2000'),
	('2424A', 'R31', '01-01-2000'),
	('2424A', 'T12', '01-01-2000'),
	('A0001', 'R31', '01-01-2000'),
	('O3139', 'T12', '01-01-2000');

-- Dumping structure for table law_firm_system.lawyer_table
DROP TABLE IF EXISTS `lawyer_table`;
CREATE TABLE IF NOT EXISTS `lawyer_table` (
  `lawyerID` varchar(5) NOT NULL,
  `lawyerName` varchar(50) DEFAULT NULL,
  `lawyerGender` varchar(50) DEFAULT NULL,
  `lawyerPosition` varchar(50) DEFAULT NULL,
  `lawyerSpecialization` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `lawyerEmail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lawyerID`),
  UNIQUE KEY `lawyerName` (`lawyerName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table law_firm_system.lawyer_table: ~3 rows (approximately)
INSERT IGNORE INTO `lawyer_table` (`lawyerID`, `lawyerName`, `lawyerGender`, `lawyerPosition`, `lawyerSpecialization`, `lawyerEmail`) VALUES
	('2424A', 'Jessica Pearson', 'Female', 'Managing Partner', 'Corporate Law', 'jessica@mail.com'),
	('A0001', 'Robert Zane', 'Male', 'Managing Partner', 'Corporate Law', 'robertzane@gmail.com'),
	('O3139', 'Oggy and the Cockroaches', 'Nonbinary', 'Managing Partner', 'Bankruptcy Law', 'zoizoi@gmail.com');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
