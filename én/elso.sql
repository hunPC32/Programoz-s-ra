CREATE DATABASE gameDatabase DEFAULT CHARACTER SET utf8
COLLATE utf8_hungarian_ci;

CREATE TABLE games(
    id INT PRIMARY KEY,
    nev VARCHAR(100),
    ertekeles DOUBLE,
    ar INT,
    kiado VARCHAR(100)
);

INSERT INTO games VALUES('1', 'Cyberpunk 2077', '8.5', '14990', 'CD Project Red');

INSERT INTO games(id, nev, ertekeles, ar) VALUES('2', 'Half-Life Alyx', '9.2', '19900');

UPDATE games SET kiado = 'Vavle' WHERE nev = 'Half-Life Alyx';

DELETE FROM games;  --Minden sort töröl
DELETE FROM games WHERE ertekeles < 9;