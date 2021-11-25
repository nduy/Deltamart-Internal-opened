-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1miniprotoUsers
-- Generation Time: Jul 02, 2021 at 06:19 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `miniproto`
--

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `UserID` varchar(3) NOT NULL,
  `Fullname` text NOT NULL,
  `IPAddress` tinytext NOT NULL,
  `Email` tinytext NOT NULL,
  `Online` tinyint(1) NOT NULL,
  `ZTNetworkID` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`UserID`, `Fullname`, `IPAddress`, `Email`, `Online`, `ZTNetworkID`) VALUES
('BCX', 'Callen Mendoza', '250.38.167.125', 'research@yahoo.ca', 0, 'c1l1nl7obwvny90q'),
('DDN', 'Duy Nguyen', '192.168.0.108', 'nanop@verizon.net', 0, '579lg1xn57234tam'),
('EPD', 'Pippa Barnes', '201.215.235.109', 'dkrishna@icloud.com', 0, 'no6eaf602ryth0k9'),
('ETF', 'Tariq Heaton', '215.91.214.67', 'naupa@gmail.com', 0, 't8c5v3kytd2qdhcf'),
('EZY', 'Lilly-Mai Larson', '222.20.170.167', 'zwood@yahoo.com', 0, 't8c5v3kytd2qdhcf'),
('FLF', 'Jay Kaufman', '46.162.157.250', 'storerm@msn.com', 0, 'k8seh1oh00wsfmv5'),
('FRE', 'Lily-Ann Rubio', '13.168.174.243', 'boomzilla@hotmail.com', 0, 'no6eaf602ryth0k9'),
('FVC', 'Bailey Contreras', '35.219.245.77', 'itstatus@yahoo.ca', 0, '2jtwbnj7sn5f79bp'),
('GHC', 'Addison Mccarty', '64.71.76.163', 'ivoibs@msn.com', 0, '2qk4fwug7oxoc5f6'),
('GRM', 'Marian Neville', '71.187.43.39', 'carreras@msn.com', 0, 'cir5k6j7cn5u7yx4'),
('GWG', 'Joey Mccullough', '84.163.12.171', 'rfoley@hotmail.com', 0, 'p7cudq83woujsfif'),
('HAB', 'Mylie Connor', '216.70.109.98', 'dvdotnet@icloud.com', 0, 'ry3oogsngyvwu92y'),
('HKX', 'Arwa Evans', '73.107.211.91', 'jramio@msn.com', 0, 'iok5x3b1b4fy4kiv'),
('JNU', 'Sannah Luna', '102.144.137.171', 'johndo@me.com', 0, 'p4jfbt6pnqrrl4z5'),
('KTC', 'Lynn Webster', '217.134.249.87', 'wainwrig@yahoo.ca', 0, 'VM2355980'),
('LYC', 'Kairon Cervantes', '148.123.151.44', 'akoblin@gmail.com', 0, 'bq60f6d2c6k5stak'),
('MCY', 'Tayla Ali', '144.15.82.184', 'cisugrad@verizon.net', 0, 'VM2355980'),
('MHE', 'Shana Mccormick', '238.215.88.122', 'ullman@verizon.net', 0, 'tel62pqk5l2yjfy3'),
('PCS', 'Keziah Mcdermott', '188.247.201.145', 'matsn@mac.com', 0, 'ut79tod87tkvjybf'),
('PKD', 'Gino Scott', '50.109.201.254', 'amimojo@outlook.com', 0, 'c1l1nl7obwvny90q'),
('PXK', 'Vivek Graham', '107.159.53.14', 'doche@mac.com', 0, 'tw70s3ahow3wkrzz'),
('PZA', 'Jena Harwood', '64.35.244.31', 'scarolan@me.com', 0, 'VM2355980'),
('QAR', 'Una Corona', '44.183.146.71', 'bsikdar@gmail.com', 0, 'wugfnstgcn8sfd8p'),
('SLZ', 'Tazmin Rawlings', '180.16.184.133', 'psharpe@yahoo.ca', 0, '77pp7adrvnrqzy59'),
('THA', 'Bernard Hanna', '66.21.19.247', 'goresky@yahoo.com', 0, 's085g6jmp2v3gs14'),
('TPF', 'Test User Pi4', '192.168.0.108', 'duydev.dsi@gmail.com', 1, 'VM2355980'),
('TPT', 'Test User Pi 3', '192.168.0.116', 'nguyenduy.uit@gmail.com', 1, 'VM2355980'),
('TSF', 'Test User Pi4', '192.168.0.108', 'duydev.dsi@gmail.com', 1, 'VM2355980'),
('TST', 'Test User Pi 3', '192.168.0.116', 'nguyenduy.uit@gmail.com', 1, 'VM2355980'),
('UFF', 'Ayana Garcia', '161.13.70.181', 'kalpol@yahoo.ca', 0, 'VM2355980'),
('UKN', 'Unknown Dummy User Public Mosquitto ', 'test.mosquitto.org', 'dummy@mos.com', 1, 'Publicnetwork'),
('UWS', 'Evie-May Drew', '13.182.111.190', 'wilsonpm@comcast.net', 0, '2qk4fwug7oxoc5f6'),
('WJN', 'Kayley Shannon', '184.116.204.160', 'gator@verizon.net', 0, 'jkn28jqtzca7n03l'),
('WRV', 'Saif Handley', '35.48.234.95', 'redingtn@sbcglobal.net', 0, 'lrv8gh0n8buombcc'),
('WZP', 'Frederic Oneill', '61.21.147.73', 'evans@yahoo.com', 0, 'apneovwjunmfhf6v'),
('XCW', 'Vlad Lowry', '189.219.113.84', 'kewley@optonline.net', 0, 'o4bcybyqx0s0s3s9');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`UserID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
