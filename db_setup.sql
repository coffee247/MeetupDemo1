CREATE TABLE user (userID int, loginID varchar(256) PRIMARY KEY, loginPWD varchar(256), firstName varchar(20), lastName varchar(20), lastModified DATETIME);

INSERT INTO user(userID, loginID, loginPWD, firstName, lastName) VALUES (1, 'admin', 'password', 'Admin', 'User'),(2, 'coffee247', 'clearpass', 'James', 'Stallings');

CREATE VIEW users_List_View AS SELECT CONCAT(firstName, ' ', lastName, ': (', LoginID, ')') AS "Full_Name", LoginID AS "Login ID" FROM user ORDER BY lastName, firstName;

CREATE TRIGGER `User_Modified_Trigger` BEFORE UPDATE ON `user` FOR EACH ROW SET new.lastmodified = CURRENT_TIMESTAMP;

UPDATE user SET firstName = 'Jimmy' where loginID = 'coffee247'

