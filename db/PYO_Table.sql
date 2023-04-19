SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `pyo` ;
CREATE SCHEMA IF NOT EXISTS `pyo` DEFAULT CHARACTER SET latin1 ;
USE `pyo` ;

/*
 Curator Create Tables
 */

CREATE TABLE IF NOT EXISTS `pyo`.'Curator' (
    Name varchar(100) NOT NULL,
    Curator_ID INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS `pyo`.'Prompts' (
    Prompt varchar(400) NOT NULL,
    Prompt_ID int PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS `pyo`.'Genre' (
    Name varchar(100) NOT NULL,
    Genre_ID varchar(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS `pyo`.'Songs' (
    Genre_ID varchar(100) NOT NULL,
    ARTIST_ID varchar(100) NOT NULL,
    /* Song ID should be the same one as the Spotify one */
    Song_ID varchar(100) NOT NULL PRIMARY KEY,
    Name varchar(100) NOT NULL,
     foreign key(Genre_ID)
                      references Genre (Genre_ID)

);

CREATE TABLE IF NOT EXISTS `pyo`.'PostEngagement' (
    Views int NOT NULL,
    Post_ID int NOT NULL PRIMARY KEY,
    Interactions int NOT NULL
);


/*
 Artist Create Tables
 */

CREATE TABLE IF NOT EXISTS `pyo`.'Artist' (
    Name varchar(100) NOT NULL,
    Artist_ID varchar(100) PRIMARY KEY
);


CREATE TABLE IF NOT EXISTS `pyo`.'Profile' (
    Username varchar(100) NOT NULL,
    Phone LONG not null,
    User_ID int PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE IF NOT EXISTS `pyo`.'Posts' (
    Genre_ID varchar(100),
    Post_ID int PRIMARY KEY AUTO_INCREMENT,
    Prompt_ID int,
    Song_ID varchar(100) NOT NULL,
    Song_ID2 varchar(100) NOT NULL,
    Song_ID3 varchar(100) NOT NULL,
    Song_ID4 varchar(100) NOT NULL,
    User_ID int not null,
    timestamp datetime not null,
    foreign key(Prompt_ID)
                      references Prompts(prompt_id),
    foreign key(Genre_ID)
                      references Genre(Genre_ID),
    foreign key(User_ID)
                      references Profile(User_ID),
    foreign key(Song_ID)
                   references Songs(Song_ID),
    foreign key(Song_ID2)
                   references Songs(Song_ID),
    foreign key(Song_ID3)
                   references Songs(Song_ID),
    foreign key(Song_ID4)
                   references Songs(Song_ID)

);

CREATE TABLE IF NOT EXISTS `pyo`.'SongEngagement' (
    Song_ID varchar(100) NOT NULL,
    listens int NOT NULL,
    views int NOT NULL,
    numofposts int NOT NULL,
    foreign key(Song_ID)
                      references Songs(Song_ID)
);


/*
 User Create Tables
 */


CREATE TABLE IF NOT EXISTS `pyo`.'Comments' (
    Comment varchar(150) NOT NULL,
    Comment_ID int PRIMARY KEY AUTO_INCREMENT,
    User_ID int not null,
    foreign key(User_ID)
                      references Profile(User_ID)
);



CREATE TABLE IF NOT EXISTS `pyo`.'Likes' (
    User_ID int NOT NULL,
    Post_ID int NOT NULL,
    foreign key(User_ID)
                      references Profile(User_ID),
    foreign key(Post_ID)
                      references Posts(Post_ID)
);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
