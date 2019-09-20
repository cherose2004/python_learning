-- MySQL dump 10.13  Distrib 5.6.44, for Win64 (x86_64)
--
-- Host: localhost    Database: day40
-- ------------------------------------------------------
-- Server version	5.6.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (200,'技术'),(201,'人力资源'),(202,'销售'),(203,'运营');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp`
--

DROP TABLE IF EXISTS `emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `sex` enum('male','female') NOT NULL DEFAULT 'male',
  `age` int(11) DEFAULT NULL,
  `dep_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp`
--

LOCK TABLES `emp` WRITE;
/*!40000 ALTER TABLE `emp` DISABLE KEYS */;
INSERT INTO `emp` VALUES (1,'egon','male',18,200),(2,'alex','female',48,201),(3,'wupeiqi','male',38,201),(4,'yuanhao','female',28,202),(5,'liwenzhou','male',18,200),(6,'jingliyang','female',18,204);
/*!40000 ALTER TABLE `emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_name` varchar(20) NOT NULL,
  `sex` enum('male','female') NOT NULL DEFAULT 'male',
  `age` int(3) unsigned NOT NULL DEFAULT '28',
  `hire_date` date NOT NULL,
  `post` varchar(50) DEFAULT NULL,
  `post_comment` varchar(100) DEFAULT NULL,
  `salary` double(15,2) DEFAULT NULL,
  `office` int(11) DEFAULT NULL,
  `depart_id` int(11) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'egon','male',18,'2017-03-01','老男孩驻沙河办事处外交大使',NULL,7300.33,401,1),(2,'alex','male',78,'2015-03-02','teacher',NULL,1000000.31,401,1),(3,'wupeiqi','male',81,'2013-03-05','teacher',NULL,8300.00,401,1),(4,'yuanhao','male',73,'2014-07-01','teacher',NULL,3500.00,401,1),(5,'liwenzhou','male',28,'2012-11-01','teacher',NULL,2100.00,401,1),(6,'jingliyang','female',18,'2011-02-11','teacher',NULL,9000.00,401,1),(7,'jinxin','male',18,'1900-03-01','teacher',NULL,30000.00,401,1),(8,'成龙','male',48,'2010-11-11','teacher',NULL,10000.00,401,1),(9,'歪歪','female',48,'2015-03-11','sale',NULL,3000.13,402,2),(10,'丫丫','female',38,'2010-11-01','sale',NULL,2000.35,402,2),(11,'丁丁','female',18,'2011-03-12','sale',NULL,1000.37,402,2),(12,'星星','female',18,'2016-05-13','sale',NULL,3000.29,402,2),(13,'格格','female',28,'2017-01-27','sale',NULL,4000.33,402,2),(14,'张野','male',28,'2016-03-11','operation',NULL,10000.13,403,3),(15,'程咬金','male',18,'1997-03-12','operation',NULL,20000.00,403,3),(16,'程咬银','female',18,'2013-03-11','operation',NULL,19000.00,403,3),(17,'程咬铜','male',18,'2015-04-11','operation',NULL,18000.00,403,3),(20,'郭凯丰','male',40,'2019-08-08',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-24 17:16:50
