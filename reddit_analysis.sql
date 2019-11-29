-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 29. Nov 2019 um 13:33
-- Server-Version: 10.4.6-MariaDB
-- PHP-Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `reddit_analysis`
--
CREATE DATABASE IF NOT EXISTS `reddit_analysis` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `reddit_analysis`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE IF NOT EXISTS `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_post` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `date_posted` datetime NOT NULL,
  `id_subreddit` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `posthistoryelement`
--

DROP TABLE IF EXISTS `posthistoryelement`;
CREATE TABLE IF NOT EXISTS `posthistoryelement` (
  `id_post` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_saved` datetime NOT NULL,
  `score` int(11) NOT NULL,
  `num_comms` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `subreddit`
--

DROP TABLE IF EXISTS `subreddit`;
CREATE TABLE IF NOT EXISTS `subreddit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
