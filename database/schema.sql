-- Create Database
CREATE DATABASE heart_disease_project;

-- Use Database
USE heart_disease_project;

-- Create Table
CREATE TABLE heart_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    HeartDisease VARCHAR(10),
    BMI FLOAT,
    Smoking VARCHAR(5),
    AlcoholDrinking VARCHAR(5),
    Stroke VARCHAR(5),
    PhysicalHealth INT,
    MentalHealth INT,
    DiffWalking VARCHAR(5),
    Sex VARCHAR(10),
    AgeCategory VARCHAR(20),
    Race VARCHAR(30),
    Diabetic VARCHAR(20),
    PhysicalActivity VARCHAR(5),
    GenHealth VARCHAR(20),
    SleepTime FLOAT,
    Asthma VARCHAR(5),
    KidneyDisease VARCHAR(5),
    SkinCancer VARCHAR(5)
);
