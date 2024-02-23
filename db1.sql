.open heart1

CREATE TABLE smoker
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into smoker values('1', 'Does Not Smoke');
insert into smoker values('2', 'Smokes Less Than three times daily');
insert into smoker values('3', 'Smokes three times daily');
insert into smoker values('4', 'Smokes More Than three times daily');
insert into smoker values('5', 'Chain Smoker');

CREATE TABLE drinker
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into drinker values('1', 'Does Not Drink');
insert into drinker values('2', 'Drinks less than thrice a week');
insert into drinker values('3', 'Drinks thrice a week');
insert into drinker values('4', 'Drinks more than thrice a week');
insert into drinker values('5', 'Drinks Daily');

CREATE TABLE diabetic
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into diabetic values('1', 'No Diabetis');
insert into diabetic values('2', 'Type 2 Diabetis');
insert into diabetic values('3', 'Severe Type 2 Diabetis');
insert into diabetic values('4', 'Type 1 Diabetis');
insert into diabetic values('5', 'Severe Type 1 Diabetis');

CREATE TABLE Arrhythmiatic
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into Arrhythmiatic values('1', 'Regular Heart Beat');
insert into Arrhythmiatic values('2', 'Low Irregular Beat');
insert into Arrhythmiatic values('3', 'Medium Irregular Beat');
insert into Arrhythmiatic values('4', 'Highly Irregular Beat');
insert into Arrhythmiatic values('5', 'Strongly Irregular Beat');

CREATE TABLE exercise
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into exercise values('1', 'Around 7hrs per week');
insert into exercise values('2', 'Around 5hrs per week');
insert into exercise values('3', 'Around 3hrs per week');
insert into exercise values('4', 'Around 1hr per week');
insert into exercise values('5', 'No Exercise');

CREATE TABLE stress
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into stress values('1', 'Relaxed Lifestyle');
insert into stress values('2', 'Less Relaxed Lifestyle');
insert into stress values('3', 'Mildly Stressful Lifestyle');
insert into stress values('4', 'Highly Stressful Lifestyle');
insert into stress values('5', 'Severe Stressful Lifestyle');

CREATE TABLE cholesterol
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into cholesterol values('1', 'Less Than 200');
insert into cholesterol values('2', 'Around 200');
insert into cholesterol values('3', 'In Between 200 to 239');
insert into cholesterol values('4', 'Around 240 ');
insert into cholesterol values('5', 'More than 240');


CREATE TABLE sleeptime
(
lsid VARCHAR(3),
lsdesc VARCHAR(15)
);
insert into sleeptime values('1', 'Around 7 hours');
insert into sleeptime values('2', 'Around 8 hours');
insert into sleeptime values('3', 'Around 9 hours');
insert into sleeptime values('4', 'More than 9 hours');
insert into sleeptime values('5', 'Less than 4 hours');

CREATE TABLE lsfacts
(
smoker VARCHAR(20),
drinker VARCHAR(20),
diabetic VARCHAR(20),
Arrhythmiatic VARCHAR(20),
exercise VARCHAR(20),
stress VARCHAR(20),
cholesterol VARCHAR(20),
sleeptime VARCHAR(20)
);

CREATE TABLE patient
(
id VARCHAR(6),
name VARCHAR(60),
age VARCHAR(3),
address1 VARCHAR(60),
address2 VARCHAR(60),
adhar VARCHAR(15),
mobile VARCHAR(15)
);
