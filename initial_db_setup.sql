CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
    Id	   		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName 	TEXT NOT NULL,
    LastName 	TEXT NOT NULL,
    SlackHandle TEXT NOT NULL,
    CohortId 	INTEGER NOT NULL,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
    
);

CREATE TABLE Instructor (
    Id	   		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName 	TEXT NOT NULL,
    LastName 	TEXT NOT NULL,
    SlackHandle TEXT NOT NULL,
    Specialty	TEXT NOT NULL,
    CohortId 	INTEGER NOT NULL,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
    Id	   		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name 		TEXT NOT NULL,
    Language 	TEXT NOT NULL
);

CREATE TABLE StudentExercise (
	Id 			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId 	INTEGER NOT NULL,
	ExerciseId 	INTEGER NOT NULL,
	FOREIGN KEY(StudentId) REFERENCES Student(Id),
	FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id)
);

INSERT INTO Cohort (Name)
VALUES ("Day Cohort 38"), ("Day Cohort 31"), ("Day Cohort 33");

INSERT INTO Exercise(Name, Language)
VALUES ("Chicken Monkey", "Javascript"),
("Array Methods", "Javascript"),
("Urban Planner", "CSharp"),
("Kennel", "React"),
("Music History", "SQL");

INSERT INTO Instructor (FirstName, LastName, SlackHandle, Specialty, CohortId)
VALUES ("Joe", "Shepherd", "joes", "dad jokes", 3),
("Jisie", "David", "jisied", "leading", 1),
("Andy", "Collins", "andyc", "sarcasm", 2);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ("Mollie", "Goforth", "mollieg", 1),
("Sydney", "Noh", "sydneyn", 3),
("Chris", "Morgan", "chrism", 2),
("Trinity", "Terry", "trinityt", 1),
("Jeff", "Hill", "jeffh", 3),
("Billy", "Mitchell", "billym", 2),
("Landon", "Morgan", "landonm", 1);

INSERT INTO StudentExercise (StudentId, ExerciseId)
VALUES (1, 1), (1, 4), 
(2, 5), (2, 2), 
(3, 3), (3, 1), 
(4, 4), (4, 5), 
(5, 4), (5, 1), 
(6, 2), (6, 3), 
(7, 2), (7, 5);