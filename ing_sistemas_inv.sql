-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 12, 2024 at 07:48 AM
-- Server version: 8.0.32
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ing_sistemas_inv`
--

-- --------------------------------------------------------

--
-- Table structure for table `evaluators`
--

CREATE TABLE `evaluators` (
  `evaluator_id` int UNSIGNED NOT NULL,
  `type_of_id` enum('Cedula de ciudadania','Cedula de extranjeria','DNI') NOT NULL,
  `doc_id_number` int NOT NULL,
  `names` varchar(100) NOT NULL,
  `lastnames` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` char(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `project_id` int UNSIGNED NOT NULL,
  `title` varchar(200) NOT NULL,
  `area_of_study` varchar(100) NOT NULL,
  `director_id` int UNSIGNED DEFAULT NULL,
  `director_full_name` varchar(100) DEFAULT NULL,
  `project_advisor_id` int UNSIGNED DEFAULT NULL,
  `project_advisor_full_name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `author_1_id` int UNSIGNED NOT NULL,
  `author_2_id` int UNSIGNED DEFAULT NULL,
  `author_3_id` int UNSIGNED DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `evaluator_id` int UNSIGNED DEFAULT NULL,
  `state` enum('Sin evaluador','Con evaluador','Revisado') NOT NULL DEFAULT 'Sin evaluador',
  `file_path` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `scores`
--

CREATE TABLE `scores` (
  `score_id` int UNSIGNED NOT NULL,
  `tematica_score` int UNSIGNED NOT NULL,
  `tematica_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `coherencia_score` int UNSIGNED NOT NULL,
  `coherencia_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `planteamiento_problema_score` int UNSIGNED NOT NULL,
  `planteamiento_problema_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `justificacion_score` int UNSIGNED NOT NULL,
  `justificacion_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `objetivos_score` int UNSIGNED NOT NULL,
  `objetivos_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `metodologia_score` int UNSIGNED NOT NULL,
  `metodologia_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `resultados_score` int DEFAULT NULL,
  `resultados_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `principales_conclusiones_score` int UNSIGNED NOT NULL,
  `principales_conclusiones_comment` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `general_observations` varchar(300) DEFAULT NULL,
  `project_id` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_cod` int UNSIGNED NOT NULL,
  `names` varchar(45) NOT NULL,
  `lastnames` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password_hash` char(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `evaluators`
--
ALTER TABLE `evaluators`
  ADD PRIMARY KEY (`evaluator_id`),
  ADD UNIQUE KEY `evaluator_id_UNIQUE` (`evaluator_id`),
  ADD UNIQUE KEY `password_hash_UNIQUE` (`password_hash`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`project_id`),
  ADD UNIQUE KEY `project_id_UNIQUE` (`project_id`),
  ADD KEY `author_1_idx` (`author_1_id`),
  ADD KEY `author_3_idx` (`author_3_id`),
  ADD KEY `author_2_idx` (`author_2_id`);

--
-- Indexes for table `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`score_id`),
  ADD UNIQUE KEY `score_id_UNIQUE` (`score_id`),
  ADD KEY `project_idx` (`project_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_cod`),
  ADD UNIQUE KEY `student_cod_UNIQUE` (`student_cod`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`),
  ADD UNIQUE KEY `password_hash_UNIQUE` (`password_hash`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `evaluators`
--
ALTER TABLE `evaluators`
  MODIFY `evaluator_id` int UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `project_id` int UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scores`
--
ALTER TABLE `scores`
  MODIFY `score_id` int UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
