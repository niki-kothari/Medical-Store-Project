CREATE DATABASE  IF NOT EXISTS `apollomedicaldb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `apollomedicaldb`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: apollomedicaldb
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `branch_id` int NOT NULL,
  `branch_name` varchar(45) DEFAULT NULL,
  `area_sqft` decimal(10,0) DEFAULT NULL,
  `gst_no` varchar(45) DEFAULT NULL,
  `b_address` varchar(100) DEFAULT NULL,
  `b_area` varchar(45) DEFAULT NULL,
  `b_city` varchar(20) DEFAULT NULL,
  `b_state` varchar(45) DEFAULT NULL,
  `b_country` varchar(45) DEFAULT NULL,
  `branch_ph_no` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `c_type` varchar(45) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Fever','body high temperature'),(2,'Cough','cough cold syrup'),(3,'Loose Motions',NULL),(4,'cotton',NULL),(5,'Antiseptic','dettol cotton ointment'),(6,'Shampoo',NULL),(7,'Conditioner',NULL),(8,'Oral Care','toothbrush toothpaste mouth cleaner'),(9,'Thermometer','temperature measuring device');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` int NOT NULL AUTO_INCREMENT,
  `c_fname` varchar(45) DEFAULT NULL,
  `c_lname` varchar(45) DEFAULT NULL,
  `c_address` varchar(200) DEFAULT NULL,
  `c_area` varchar(45) DEFAULT NULL,
  `c_city` varchar(45) DEFAULT NULL,
  `c_state` varchar(45) DEFAULT NULL,
  `c_country` varchar(45) DEFAULT NULL,
  `c_ph_no` varchar(15) DEFAULT NULL,
  `c_dob` date DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'niki','kothari','101, shramandeep apt','ghod dod road','surat','gujarat','india','9913761442','1989-02-25'),(2,'siddharth','parakh','add1','city light','surat','rajasthan','india','9785463214','1982-02-14'),(3,'priya','singhal','surya palace','bhatar','surat','gujarat','india','6547892354','2000-04-13'),(4,'divit','jain','160, manan bunglow','ghod dod road','mumbai','maharastra','india','9874563210','2014-08-14');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_id` int NOT NULL,
  `branch_id` int DEFAULT NULL,
  `e_fname` varchar(45) DEFAULT NULL,
  `e_mname` varchar(45) DEFAULT NULL,
  `e_lname` varchar(45) DEFAULT NULL,
  `e_address` varchar(200) DEFAULT NULL,
  `e_area` varchar(45) DEFAULT NULL,
  `e_city` varchar(45) DEFAULT NULL,
  `e_state` varchar(45) DEFAULT NULL,
  `e_country` varchar(45) DEFAULT NULL,
  `e_ph_no` varchar(15) DEFAULT NULL,
  `e_aadhar_no` varchar(10) DEFAULT NULL,
  `e_dob` date DEFAULT NULL,
  `e_salary` double DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,1,'niki','amit','kothari','102, shramandeep apt.','ghod dod road','surat','gujarat','india','9913761442','hj25t52rt1','1989-02-25',20000),(2,2,'amit','pukhraj','kothari','102, shramandeep apt.','ghod dod road','surat','gujarat','india','9879198422','2dfg457y4h','1986-01-18',60000),(3,1,'mayur','pukhraj','jain','160 manan bunglow','bhatar','Surat','Gujarat','India','9879195555','2dfg457y4h','1984-03-17',80000),(4,2,'purav','mayur','kothari','160 manan bunglow','bhatar','Surat','Gujarat','India','9799995555','2dfg457y4h','2014-08-01',1000),(5,1,'divit','amit','jain','102, shramandeep apt.','ghod dod road','Surat','Gujarat','India','889995555','2dfg457y4h','2014-08-14',10000);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_transaction`
--

DROP TABLE IF EXISTS `employee_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_transaction` (
  `transaction_id` int NOT NULL,
  `emp_id` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `amount` decimal(2,0) DEFAULT NULL,
  `payment_mode` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_transaction`
--

LOCK TABLES `employee_transaction` WRITE;
/*!40000 ALTER TABLE `employee_transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `invoice_no` int NOT NULL,
  `date` datetime DEFAULT NULL,
  `emp_id` int DEFAULT NULL,
  `cust_id` int DEFAULT NULL,
  `total_amt` decimal(2,0) DEFAULT NULL,
  `paid_amt` decimal(2,0) DEFAULT NULL,
  `payment_mode` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`invoice_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice_details`
--

DROP TABLE IF EXISTS `invoice_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_details` (
  `detail_id` int NOT NULL,
  `invoice_id` int DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `qty_purchased` int DEFAULT NULL,
  `discount` decimal(2,0) DEFAULT NULL,
  PRIMARY KEY (`detail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_details`
--

LOCK TABLES `invoice_details` WRITE;
/*!40000 ALTER TABLE `invoice_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `item_id` int NOT NULL,
  `category_id` int DEFAULT NULL,
  `i_name` varchar(45) DEFAULT NULL,
  `supplier_id` int DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `i_rate` double DEFAULT NULL,
  `i_stock_qty` int DEFAULT NULL,
  `i_manufacturing_date` date DEFAULT NULL,
  `i_expiry_date` date DEFAULT NULL,
  `rack_id` int DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,1,'dolo',1,'fever remedy',50,100,'2024-05-12','2027-05-12',1),(2,1,'ibugesic',2,'fever medicine',105,25,'2025-01-14','2026-06-18',1),(3,2,'crocin advance',1,'fever',30,50,'2025-01-11','2027-01-11',1),(4,3,'norflox',1,'gastro',120,44,'2025-05-25','2026-05-25',2),(5,3,'zanocin',3,'diahrea',200,20,'2024-11-01','2025-08-08',2),(6,2,'tusq-d',2,'cough syrup',180,25,'2025-05-15','2026-03-13',3),(7,6,'loreal shampoo',5,'shampoo',500,10,'2024-10-10','2026-10-10',6),(8,7,'loreal pro active',5,'conditioner',250,5,'2024-02-02','2026-05-15',6),(9,6,'clinic plus',6,'shampoo',350,20,'2025-03-03','2027-12-03',6),(10,8,'colgate sensitive',4,'toothpaste',150,15,'2025-06-14','2026-06-13',5),(15,3,'item1',2,'desc1',50,20,'2025-02-02','2026-02-02',5);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rack`
--

DROP TABLE IF EXISTS `rack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rack` (
  `rack_id` int NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`rack_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rack`
--

LOCK TABLES `rack` WRITE;
/*!40000 ALTER TABLE `rack` DISABLE KEYS */;
INSERT INTO `rack` VALUES (1,'1st rack',1),(2,'2nd rack',3),(3,'3rd rack',2),(4,'4th rack',4),(5,'5th rack',5);
/*!40000 ALTER TABLE `rack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplier_id` int NOT NULL,
  `s_fname` varchar(45) DEFAULT NULL,
  `s_lname` varchar(45) DEFAULT NULL,
  `s_address` varchar(200) DEFAULT NULL,
  `s_area` varchar(45) DEFAULT NULL,
  `s_city` varchar(45) DEFAULT NULL,
  `s_state` varchar(45) DEFAULT NULL,
  `s_country` varchar(45) DEFAULT NULL,
  `s_ph_no` varchar(15) DEFAULT NULL,
  `s_email` varchar(45) DEFAULT NULL,
  `s_pan_no` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'ajay','jain','101, shramandeep apt.','ghod dod road','Surat','Gujarat','India','9825675456','ajay.jain@gmail.com','124578gth8'),(2,'chandu','bhogar','101, shramandeep apt.','ghod dod road','Surat','Gujarat','India','9825675456','chandu.bhogar@gmail.com','124578gth8'),(3,'raj','kapadia','201, surya enclave','city light','Surat','Gujarat','India','9834675456','raj_kapadia89@gmail.com','124578gth8'),(4,'dhiraj','dukkad','201, surya enclave','vesu','Surat','Gujarat','India','9564675456','dhiraj1_dukkad@gmail.com','124578gth8');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-18 12:17:00
