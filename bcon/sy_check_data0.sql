-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: sy
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `check_data`
--

DROP TABLE IF EXISTS `check_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `check_data` (
  `번호` int NOT NULL,
  `ID` varchar(45) DEFAULT NULL,
  `비밀번호` varchar(45) DEFAULT NULL,
  `이름` varchar(45) DEFAULT NULL,
  `구분` varchar(45) DEFAULT '학생',
  `입실` varchar(45) DEFAULT NULL,
  `복귀` varchar(45) DEFAULT NULL,
  `외출` varchar(45) DEFAULT NULL,
  `퇴실` varchar(45) DEFAULT NULL,
  `출석횟수` int DEFAULT '46',
  `지각횟수` int DEFAULT '0',
  `조퇴횟수` int DEFAULT '0',
  `외출횟수` int DEFAULT '0',
  `결석횟수` int DEFAULT '0',
  `클래스` varchar(45) DEFAULT '데이터 기반 AI SW개발자 양성',
  `훈련회차` varchar(45) DEFAULT '2회차',
  `훈련기관` varchar(45) DEFAULT '대한상공회의소 광주인력개발원',
  `기관위치` varchar(45) DEFAULT '광주 광산구',
  `전화번호` varchar(45) DEFAULT '062-940-3520',
  `훈련기간` varchar(45) DEFAULT '2022.10.25 - 2023.05.24',
  `훈련유형` varchar(45) DEFAULT '통합심사과정훈련',
  `금일훈련` varchar(45) DEFAULT NULL,
  `출석일수` int DEFAULT '46',
  `최대출석일수` int DEFAULT '140',
  `과정진행` int DEFAULT '46',
  `총과정진행` int DEFAULT '140',
  PRIMARY KEY (`번호`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_data`
--

LOCK TABLES `check_data` WRITE;
/*!40000 ALTER TABLE `check_data` DISABLE KEYS */;
INSERT INTO `check_data` VALUES (1,'ai01','1234','강민영','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(2,'ai02','1234','고연재','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(3,'ai03','1234','김기태','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(4,'ai04','1234','김명은','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(5,'ai05','1234','김성일','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(6,'ai06','1234','김연수','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(7,'ai07','1234','노도현','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(8,'ai08','1234','박규환','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(9,'ai09','1234','박성빈','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(10,'ai10','1234','박시형','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(11,'ai11','1234','박의용','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(12,'ai12','1234','오송화','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(13,'ai13','1234','이범규','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(14,'ai14','1234','이보라','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(15,'ai15','1234','이소윤','학생','2023-01-11 20:07:36','2023-01-11 14:51:54','2023-01-11 14:52:03','2023-01-11 14:52:07',46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(16,'ai16','1234','이여름','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(17,'ai17','1234','이지혜','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(18,'ai18','1234','이현도','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(19,'ai19','1234','임성경','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(20,'ai20','1234','임영효','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(21,'ai21','1234','임홍선','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(22,'ai22','1234','장은희','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(23,'ai23','1234','정연우','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(24,'ai24','1234','정철우','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(25,'ai25','1234','주민석','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(26,'ai26','1234','최지혁','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(27,'ai27','1234','류가미','학생',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(100,'boki','1234','이상복','교수',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(101,'ryuryu','1234','류홍걸','교수',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140),(102,'cho','1234','조동현','교수',NULL,NULL,NULL,NULL,46,0,0,0,0,'데이터 기반 AI SW개발자 양성','2회차','대한상공회의소 광주인력개발원','광주 광산구','062-940-3520','2022.10.25 - 2023.05.24','통합심사과정훈련',NULL,46,140,46,140);
/*!40000 ALTER TABLE `check_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-11 21:16:17
