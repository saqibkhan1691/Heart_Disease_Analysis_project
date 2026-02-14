SELECT * FROM heart_data;


-- Total Records
SELECT COUNT(*) FROM heart_data;

-- Heart Disease Distribution 
SELECT HeartDisease ,COUNT(*) AS total FROM heart_data
GROUP BY HeartDisease;


-- Heart Disease Rate % 
SELECT HeartDisease, (COUNT(*)/ (SELECT COUNT(*) FROM heart_data) )*100.0 AS percentange FROM heart_data
GROUP BY HeartDisease;


-- Average BMI by Heart Disease
SELECT HeartDisease, AVG(BMI) AS avg_bmi FROM heart_data
GROUP BY HeartDisease; 


-- Smoking vs Heart Disease
SELECT Smoking, HeartDisease, COUNT(*) AS total FROM heart_data
GROUP BY Smoking, HeartDisease; 


--  Gender wise Heart Disease
SELECT Sex, HeartDisease, COUNT(*) AS total FROM heart_data
GROUP BY Sex, HeartDisease;


-- Among Smokers Heart Disease Rate %
SELECT 
    Smoking,
    COUNT(*) AS total_people,
    SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) AS disease_cases,
    ROUND(
        SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS disease_rate_percent
FROM heart_data
GROUP BY Smoking;


-- Age Category Impact
SELECT 
    AgeCategory,
    COUNT(*) AS total,
    SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) AS disease_cases,
    (SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS disease_rate
FROM heart_data
GROUP BY AgeCategory
ORDER BY disease_rate DESC;


-- Physical Activity Impact
 SELECT 
    PhysicalActivity,
    COUNT(*) AS total,
    SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) AS disease_cases,
    (SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS disease_rate
FROM heart_data
GROUP BY PhysicalActivity;


-- GenHealth Impact
SELECT 
    GenHealth,
    COUNT(*) AS total,
    SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) AS disease_cases,
    ROUND(
        SUM(CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS disease_rate
FROM heart_data
GROUP BY GenHealth
ORDER BY disease_rate DESC;