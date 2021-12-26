-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema myDjangodb
-- -----------------------------------------------------
-- Dase de datos del reto

-- -----------------------------------------------------
-- Schema myDjangodb
--
-- Dase de datos del reto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `myDjangodb` DEFAULT CHARACTER SET utf8 ;
USE `myDjangodb` ;

-- -----------------------------------------------------
-- Table `myDjangodb`.`Object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myDjangodb`.`Object` (
  `idObject` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idObject`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myDjangodb`.`Feed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myDjangodb`.`Feed` (
  `title` VARCHAR(100) NULL,
  `id` VARCHAR(200) NOT NULL,
  `copyright` VARCHAR(200) NULL,
  `country` VARCHAR(100) NULL,
  `icon` VARCHAR(200) NULL,
  `updated` VARCHAR(150) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `object`
    FOREIGN KEY (`id`)
    REFERENCES `myDjangodb`.`Object` (`idObject`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myDjangodb`.`Author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myDjangodb`.`Author` (
  `name` VARCHAR(100) NOT NULL,
  `url` VARCHAR(200) NULL,
  PRIMARY KEY (`name`),
  CONSTRAINT `feed`
    FOREIGN KEY (`name`)
    REFERENCES `myDjangodb`.`Feed` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myDjangodb`.`Links`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myDjangodb`.`Links` (
  `self` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`self`),
  CONSTRAINT `feed`
    FOREIGN KEY (`self`)
    REFERENCES `myDjangodb`.`Feed` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myDjangodb`.`Results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myDjangodb`.`Results` (
  `artistName` VARCHAR(100) NULL,
  `id` VARCHAR(100) NOT NULL,
  `name` VARCHAR(100) NULL,
  `releaseDate` VARCHAR(100) NULL,
  `kind` VARCHAR(100) NULL,
  `artistId` INT NULL,
  `artistUrl` VARCHAR(200) NULL,
  `contentAdvisoryRating` VARCHAR(200) NULL,
  `artworkUrl100` VARCHAR(200) NULL,
  `url` VARCHAR(200) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `feed`
    FOREIGN KEY (`id`)
    REFERENCES `myDjangodb`.`Feed` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `myDjangodb`.`Genres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myDjangodb`.`Genres` (
  `genreId` VARCHAR(100) NOT NULL,
  `name` VARCHAR(200) NULL,
  `url` VARCHAR(200) NULL,
  PRIMARY KEY (`genreId`),
  CONSTRAINT `results`
    FOREIGN KEY (`genreId`)
    REFERENCES `myDjangodb`.`Results` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
