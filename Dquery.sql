CREATE TABLE Flyers(
    uuid varchar(50) PRIMARY KEY,
    FirstName varchar(20), 
    LastName varchar(20),
    FlyerPoints int, 
    Hash varchar(50),
    username varchar(50)
);
INSERT INTO Flyers (uuid, FirstName, LastName, FlyerPoints, Hash, username) 
VALUES ("fbfd341a-7f82-11e6-9ccc-916367f449e2","Daphene", "whitley", "50000", "$2b$12$iQA.I5Fl3Z1zY39aR3CyqueRJGursUVg20SZAoZ195g/lUjUaFDtm", "user");

