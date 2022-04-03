CREATE TABLE LIBRARY(
LIBRARY_ID VARCHAR(4) PRIMARY KEY,
LIBRARY_NAME TEXT
)

CREATE TABLE LEVEL(
LEVEL_ID VARCHAR(6) PRIMARY KEY,
LIBRARY_ID VARCHAR(4) REFERENCES LIBRARY(LIBRARY_ID),
LEVEL INTEGER
)

CREATE TABLE SEAT(
SEAT_ID VARCHAR(8) PRIMARY KEY,
LIBRARY_ID VARCHAR(4) REFERENCES LIBRARY(LIBRARY_ID),
LEVEL_ID VARCHAR(6) REFERENCES LEVEL(LEVEL_ID),
ROW CHARACTER,
COL CHARACTER
)

CREATE TABLE OCCUPIED (
OCCUPIED_ID SERIAL PRIMARY KEY,
MATRIC_NO VARCHAR(9),
LIBRARY_ID VARCHAR(4) REFERENCES LIBRARY(LIBRARY_ID),
LEVEL_ID VARCHAR(6) REFERENCES LEVEL(LEVEL_ID),
SEAT_ID VARCHAR(8) REFERENCES SEAT(SEAT_ID),
BOOK_DATE DATE,
START_TIME TIME,
END_TIME TIME
)



