-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gym_sys
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `gym_sys` ;

-- -----------------------------------------------------
-- Schema gym_sys
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gym_sys` DEFAULT CHARACTER SET utf8 ;
USE `gym_sys` ;

-- -----------------------------------------------------
-- Table `gym_sys`.`gym_hall`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`gym_hall` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`gym_hall` (
  `hall_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`hall_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`equipment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`equipment` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`equipment` (
  `equip_seq_num` VARCHAR(45) NOT NULL,
  `hall_name` VARCHAR(45) NOT NULL,
  `equipment_description` TEXT NOT NULL,
  PRIMARY KEY (`equip_seq_num`),
  CONSTRAINT `fk_equipment_gym_hall1`
    FOREIGN KEY (`hall_name`)
    REFERENCES `gym_sys`.`gym_hall` (`hall_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`trainer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`trainer` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`trainer` (
  `trainer_name` VARCHAR(100) NOT NULL,
  `hall_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`trainer_name`),
  CONSTRAINT `fk_trainer_gym_hall1`
    FOREIGN KEY (`hall_name`)
    REFERENCES `gym_sys`.`gym_hall` (`hall_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`customer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`customer` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`customer` (
  `customer_name` VARCHAR(100) NOT NULL,
  `address` VARCHAR(100) NULL,
  `phone` VARCHAR(20) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`customer_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`exercise_plan`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`exercise_plan` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`exercise_plan` (
  `idexercise_plan` INT NOT NULL AUTO_INCREMENT,
  `trainer_name` VARCHAR(100) NOT NULL,
  `planDetails` TEXT NULL,
  PRIMARY KEY (`idexercise_plan`),
  CONSTRAINT `fk_exercise_plan_trainer1`
    FOREIGN KEY (`trainer_name`)
    REFERENCES `gym_sys`.`trainer` (`trainer_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`assign`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`assign` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`assign` (
  `idexercise_plan` INT NOT NULL,
  `idequipment` VARCHAR(45) NOT NULL,
  `equip_seq_num` INT NOT NULL,
  `duration` CHAR(6) NOT NULL,
  PRIMARY KEY (`idexercise_plan`, `idequipment`, `equip_seq_num`),
  CONSTRAINT `fk_equipment_has_exercise_plan_equipment1`
    FOREIGN KEY (`idequipment`)
    REFERENCES `gym_sys`.`equipment` (`equip_seq_num`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_equipment_has_exercise_plan_exercise_plan1`
    FOREIGN KEY (`idexercise_plan`)
    REFERENCES `gym_sys`.`exercise_plan` (`idexercise_plan`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`subscribe`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`subscribe` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`subscribe` (
  `customer_name` VARCHAR(100) NOT NULL,
  `meetingTime` DATETIME NOT NULL,
  `trainer_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`customer_name`, `meetingTime`),
  CONSTRAINT `fk_subscribe_customer1`
    FOREIGN KEY (`customer_name`)
    REFERENCES `gym_sys`.`customer` (`customer_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_subscribe_trainer1`
    FOREIGN KEY (`trainer_name`)
    REFERENCES `gym_sys`.`trainer` (`trainer_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`openHRs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`openHRs` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`openHRs` (
  `hall_name` VARCHAR(45) NOT NULL,
  `weekday` INT NOT NULL,
  `startTime` CHAR(6) NOT NULL,
  `endTime` CHAR(6) NOT NULL,
  PRIMARY KEY (`hall_name`, `weekday`),
  CONSTRAINT `fk_openHRs_gym_hall1`
    FOREIGN KEY (`hall_name`)
    REFERENCES `gym_sys`.`gym_hall` (`hall_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_sys`.`follow`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_sys`.`follow` ;

CREATE TABLE IF NOT EXISTS `gym_sys`.`follow` (
  `customer_name` VARCHAR(100) NOT NULL,
  `exercise_plan` INT NOT NULL,
  `startTime` DATETIME NOT NULL,
  `finishTime` DATETIME NOT NULL,
  PRIMARY KEY (`customer_name`, `exercise_plan`),
  CONSTRAINT `fk_customer_has_exercise_plan_customer1`
    FOREIGN KEY (`customer_name`)
    REFERENCES `gym_sys`.`customer` (`customer_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_customer_has_exercise_plan_exercise_plan1`
    FOREIGN KEY (`exercise_plan`)
    REFERENCES `gym_sys`.`exercise_plan` (`idexercise_plan`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
