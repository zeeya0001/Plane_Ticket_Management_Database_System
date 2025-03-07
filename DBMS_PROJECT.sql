cREATE DATABASE PLANE_TICKET_MANAGEMENT;
USE PLANE_TICKET_MANAGEMENT;

CREATE TABLE Location (
    location_ID INT PRIMARY KEY,
    location_name VARCHAR(50),
    address VARCHAR(50),
    city VARCHAR(50),
    country VARCHAR(30)
);

CREATE TABLE Passenger (
    Passenger_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_name VARCHAR(20) NOT NULL,
    Last_name VARCHAR(20) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Passport_number VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Passenger_Location (
    Passenger_ID INT,
    location_ID INT,
    PRIMARY KEY (Passenger_ID, location_ID),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ,
    FOREIGN KEY (location_ID) REFERENCES Location(location_ID) 
);

CREATE TABLE ContactN_Number_Passenger (
    Passenger_ID INT PRIMARY KEY,
    Contact_Number VARCHAR(10),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) 
);


CREATE TABLE Airline (
    Airline_ID VARCHAR(15) PRIMARY KEY,
    Airline_name VARCHAR(100) NOT NULL,
    Operating_Region VARCHAR(50) NOT NULL
);

CREATE TABLE ContactN_Number_Airline (
    Airline_ID VARCHAR(15),
    Contact_Number VARCHAR(10),
    PRIMARY KEY (Airline_ID, Contact_Number) ,
    FOREIGN KEY (Airline_ID) REFERENCES Airline(Airline_ID) 
);

CREATE TABLE Airport (
    AP_CODE VARCHAR(10) PRIMARY KEY,  
    Airport_name VARCHAR(100) NOT NULL,
    location_ID INT,
    facilities VARCHAR(50) NOT NULL,
    FOREIGN KEY (location_ID) REFERENCES Location(location_ID) 
);

CREATE TABLE Flight (
    Flight_ID INT PRIMARY KEY,
    Flight_name VARCHAR(20) NOT NULL,
    Departure_Time DATETIME NOT NULL,
    Arrival_Time DATETIME NOT NULL,
    Year_of_Services INT NOT NULL,
    Airline_ID VARCHAR(15),
    Origin_AP_CODE VARCHAR(10) ,
    Destination_AP_CODE VARCHAR(10),
    Flight_type VARCHAR(20) NOT NULL,
    Flight_Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (Airline_ID) REFERENCES Airline(Airline_ID),
    FOREIGN KEY (Origin_AP_CODE) REFERENCES Airport(AP_CODE),
    FOREIGN KEY (Destination_AP_CODE) REFERENCES Airport(AP_CODE)  
);

DROP TABLE Flight;

CREATE TABLE Flight_Location (
    Flight_ID INT,
    location_ID INT,
    PRIMARY KEY (Flight_ID, location_ID),
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID),
    FOREIGN KEY (location_ID) REFERENCES Location(location_ID)
);

CREATE TABLE Booking (
    Booking_ID INT PRIMARY KEY,
    Date DATETIME NOT NULL,
    Payment_Status VARCHAR(20),
    Boarding_time DATETIME,
    ChecK_in_time DATETIME,
    Price DECIMAL(10, 2),
    Passenger_ID INT,
    Flight_ID INT,
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE,
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID) ON DELETE CASCADE
);



CREATE TABLE Services (
    Service_ID INT PRIMARY KEY,
    Service_name VARCHAR(100) NOT NULL,
    Airport_ID VARCHAR(3),
    FOREIGN KEY (Airport_ID) REFERENCES Airport(AP_CODE) ON DELETE CASCADE
);

CREATE TABLE Booking_Services (
    Booking_ID INT,
    Service_ID INT,
    PRIMARY KEY (Booking_ID, Service_ID),
    FOREIGN KEY (Booking_ID) REFERENCES Booking(Booking_ID) ON DELETE CASCADE,
    FOREIGN KEY (Service_ID) REFERENCES Services(Service_ID) ON DELETE CASCADE
);

CREATE TABLE seat_matrix (
    Seat_ID INT PRIMARY KEY,
    Flight_ID INT,
    Seat_Number VARCHAR(5) NOT NULL,
    Class VARCHAR(20),
    Availability VARCHAR(10) NOT NULL,
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID) ON DELETE CASCADE
);

CREATE TABLE Payment (
    Payment_ID INT PRIMARY KEY,
    Amount DECIMAL(10, 2),
    Payment_Method VARCHAR(20),
    Date DATETIME,
    Booking_ID INT,
    FOREIGN KEY (Booking_ID) REFERENCES Booking(Booking_ID) ON DELETE CASCADE
);

CREATE TABLE Review (
    Review_ID INT PRIMARY KEY,
    Flight_ID INT,
    Service_ID INT,
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),
    Date DATETIME,
    Comment VARCHAR(255),
    FOREIGN KEY (Flight_ID) REFERENCES Flight(Flight_ID) ON DELETE CASCADE,
    FOREIGN KEY (Service_ID) REFERENCES Services(Service_ID) ON DELETE CASCADE
);


CREATE TABLE Notification (
    Notification_ID INT PRIMARY KEY,
    Passenger_ID INT,
    Message VARCHAR(255),
    Date DATETIME,
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE
);

CREATE TABLE Cancellation (
    Cancellation_ID INT PRIMARY KEY,
    Booking_ID INT,
    Request_time DATETIME NOT NULL,
    Issue_time DATETIME NOT NULL,
    Reason VARCHAR(255),
    FOREIGN KEY (Booking_ID) REFERENCES Booking(Booking_ID) ON DELETE CASCADE
);

INSERT INTO Location (location_ID, location_name, address, city, country) VALUES 
(1, 'John F. Kennedy International Airport', 'JFK Access Rd', 'New York', 'USA'),
(2, 'Heathrow Airport', 'Longford', 'London', 'UK'),
(3, 'Chhatrapati Shivaji Maharaj International Airport', 'Western Express Hwy', 'Mumbai', 'India'),
(4, 'Sydney Kingsford Smith Airport', 'Sir Reginald Ansett Dr', 'Sydney', 'Australia'),
(5, 'Dubai International Airport', 'Dubai Airport Rd', 'Dubai', 'UAE');

INSERT INTO Passenger (First_name, Last_name, Email, Passport_number) VALUES 
('Amit', 'Sharma', 'amit.sharma@example.com', 'P456123789'),
('Priya', 'Verma', 'priya.verma@example.com', 'P654321987'),
('Rajesh', 'Patel', 'rajesh.patel@example.com', 'P321987654'),
('Sita', 'Nair', 'sita.nair@example.com', 'P987654321'),
('Karan', 'Mehta', 'karan.mehta@example.com', 'P159753258');


INSERT INTO Passenger_Location (Passenger_ID, location_ID) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5);

INSERT INTO ContactN_Number_Passenger (Passenger_ID, Contact_Number) VALUES 
(1, '1234567890'),  
(2, '0987654321'), 
(3, '1122334455'), 
(4, '5566778899'),  
(5, '6677889900');

INSERT INTO Airline (Airline_ID, Airline_name, Operating_Region) VALUES 
('AA101', 'American Airlines', 'North America'),
('BA202', 'British Airways', 'Europe'),
('AI303', 'Air India', 'Asia'),
('QF404', 'Qantas Airways', 'Australia'),
('EK505', 'Emirates', 'Middle East');

INSERT INTO ContactN_Number_Airline (Airline_ID, Contact_Number) VALUES 
('AA101', '8001234567'), 
('BA202', '8009876543'),  
('AI303', '8004567890'),  
('QF404', '8001122334'),  
('EK505', '8009988776');

INSERT INTO Airport (AP_CODE, Airport_name, location_ID, facilities) VALUES
('JFK', 'John F. Kennedy International Airport', 1, 'Wi-Fi, Lounges'),
('LHR', 'Heathrow Airport', 2, 'Wi-Fi, Shops, Lounges'),
('BOM', 'Chhatrapati Shivaji Maharaj International Airport', 3, 'Wi-Fi, Duty-Free Shops'),
('SYD', 'Sydney Kingsford Smith Airport', 4, 'Wi-Fi, Lounges, Shops'),
('DXB', 'Dubai International Airport', 5, 'Wi-Fi, Lounges, Duty-Free');

INSERT INTO Flight (Flight_ID, Flight_name, Departure_Time, Arrival_Time, Year_of_Services, Airline_ID, Origin_AP_CODE, Destination_AP_CODE, Flight_type, Flight_Status)
VALUES 
(1, 'AA101', '2024-12-01 08:00:00', '2024-12-01 11:00:00', 10, 'AA101', 'JFK', 'LHR', 'Domestic', 'On Time'),
(2, 'BA202', '2024-12-02 09:00:00', '2024-12-02 12:30:00', 8, 'BA202', 'LHR', 'JFK', 'International', 'Delayed'),
(3, 'AI303', '2024-12-03 10:30:00', '2024-12-03 19:00:00', 15, 'AI303', 'BOM', 'DXB', 'International', 'On Time'),
(4, 'QF404', '2024-12-04 11:00:00', '2024-12-04 21:00:00', 12, 'QF404', 'SYD', 'DXB', 'International', 'Cancelled'),
(5, 'EK505', '2024-12-05 12:00:00', '2024-12-05 14:00:00', 20, 'EK505', 'DXB', 'SYD', 'International', 'On Time');



INSERT INTO Flight_Location (Flight_ID, location_ID) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO Booking (Booking_ID, Date, Payment_Status, Boarding_time, ChecK_in_time, Price, Passenger_ID, Flight_ID) VALUES 
(1, '2024-11-01 09:00:00', 'Paid', '2024-12-01 09:30:00', '2024-12-01 08:30:00', 199.99, 1, 1),
(2, '2024-11-02 10:00:00', 'Pending', '2024-12-02 15:30:00', '2024-12-02 14:30:00', 299.99, 2, 2),
(3, '2024-11-03 11:00:00', 'Paid', '2024-12-03 08:30:00', '2024-12-03 07:30:00', 399.99, 3, 3),
(4, '2024-11-04 12:00:00', 'Cancelled', '2024-12-04 18:30:00', '2024-12-04 17:30:00', 249.99, 4, 4),
(5, '2024-11-05 13:00:00', 'Paid', '2024-12-05 09:30:00', '2024-12-05 08:30:00', 159.99, 5, 5);

INSERT INTO Services (Service_ID, Service_name, Airport_ID) VALUES 
(1, 'Lounge Access', 'JFK'),
(2, 'Priority Boarding', 'LHR'),
(3, 'Duty-Free Shopping', 'DXB'),
(4, 'Baggage Wrapping', 'SYD'),
(5, 'Wi-Fi', 'BOM');

INSERT INTO Booking_Services (Booking_ID, Service_ID) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO seat_matrix (Seat_ID, Flight_ID, Seat_Number, Class, Availability) VALUES 
(1, 1, '1A', 'First Class', 'Available'),
(2, 1, '2B', 'Business Class', 'Occupied'),
(3, 2, '3C', 'Economy Class', 'Available'),
(4, 3, '4D', 'Economy Class', 'Occupied'),
(5, 4, '5E', 'First Class', 'Available');

INSERT INTO Payment (Payment_ID, Amount, Payment_Method, Date, Booking_ID) VALUES 
(1, 199.99, 'Credit Card', '2024-11-01 09:00:00', 1),
(2, 299.99, 'Debit Card', '2024-11-02 10:00:00', 2),
(3, 399.99, 'PayPal', '2024-11-03 11:00:00', 3),
(4, 249.99, 'Credit Card', '2024-11-04 12:00:00', 4),
(5, 159.99, 'Debit Card', '2024-11-05 13:00:00', 5);

INSERT INTO Review (Review_ID, Flight_ID, Service_ID, Rating, Date, Comment) VALUES
(1, 1, 1, 5, '2024-12-01 15:00:00', 'Excellent service and comfortable flight!'),
(2, 2, 2, 4, '2024-12-02 18:30:00', 'Good flight but was delayed.'),
(3, 3, 3, 3, '2024-12-03 20:00:00', 'Average experience, food could be better.'),
(4, 4, 4, 2, '2024-12-04 22:00:00', 'Flight was cancelled, very inconvenient.'),
(5, 5, 5, 5, '2024-12-05 16:00:00', 'Loved the lounge access and smooth journey.');

INSERT INTO Notification (Notification_ID, Passenger_ID, Message, Date) VALUES 
(1, 1, 'Your flight is confirmed!', '2024-11-01 10:00:00'),
(2, 2, 'Check-in opens 24 hours before departure.', '2024-11-02 10:00:00'),
(3, 3, 'Your boarding pass is ready!', '2024-11-03 11:00:00'),
(4, 4, 'Flight cancellation notice.', '2024-11-04 12:00:00'),
(5, 5, 'Your payment has been received.', '2024-11-05 13:00:00');

INSERT INTO Cancellation (Cancellation_ID, Booking_ID, Request_time, Issue_time, Reason) VALUES 
(1, 1, '2024-11-01 10:30:00', '2024-11-01 11:00:00', 'Personal reasons'),
(2, 2, '2024-11-02 11:15:00', '2024-11-02 12:00:00', 'Health issues'),
(3, 3, '2024-11-03 09:00:00', '2024-11-03 10:00:00', 'Change of plans'),
(4, 4, '2024-11-04 13:30:00', '2024-11-04 14:00:00', 'Emergency'),
(5, 5, '2024-11-05 14:00:00', '2024-11-05 15:00:00', 'Flight rescheduled');


SELECT * FROM Location;
SELECT * FROM Passenger;
SELECT * FROM Passenger_Location;
SELECT * FROM ContactN_Number_Passenger;
SELECT * FROM Airline;
SELECT * FROM ContactN_Number_Airline;
SELECT * FROM Airport;
SELECT * FROM Flight;
SELECT * FROM Flight_Location;
SELECT * FROM Booking;
SELECT * FROM Services;
SELECT * FROM Booking_Services;
SELECT * FROM Seat_matrix;
SELECT * FROM Payment;
SELECT * FROM Review;

ALTER TABLE Review 
ADD Passenger_ID INT,
ADD FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID) ON DELETE CASCADE;

INSERT INTO Review(Review_ID, Passenger_ID) VALUES
(010, 2), (022, 4), (031, 1), (046, 5), (057, 3);


-- 1. Retrieve All Flights for a Specific Destination
SELECT F.Flight_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE, A.Airport_name
FROM Flight F
JOIN Airport A ON F.Origin_AP_Code = A.AP_Code
WHERE F.Destination_AP_CODE = 'SYD';

-- 2. Get All Passengers on a Specific Flight
SELECT P.Passenger_ID, P.First_name, P.Email
FROM Passenger P
JOIN Booking B ON P.Passenger_ID = B.Passenger_ID
WHERE B.Flight_ID = 101;  

-- 3. Retrieve Booking Information for a Passenger
SELECT B.Booking_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE, B.Payment_Status
FROM Booking B
JOIN Flight F ON B.Flight_ID = F.Flight_ID
JOIN Passenger P ON B.Passenger_ID = P.Passenger_ID
WHERE P.Email = 'rajesh.patel@example.com'; 

-- 4. Get Payment Details for a Specific Booking
SELECT P.Payment_ID, P.Amount, P.Payment_method, P.Date
FROM Payment P
JOIN Booking B ON P.Booking_ID = B.Booking_ID
WHERE B.Booking_ID = 1;  

-- 5. Retrieve All Services Offered by an Airpot
SELECT S.Service_ID, S.Service_name
FROM Services S
JOIN Airport AP ON S.Service_ID = AP.AP_CODE
WHERE AP.AP_CODE = 'DXB';  

-- 6.  Get the Total Amount Paid by a Passenger
SELECT P.Passenger_ID, P.First_name, SUM(Pay.Amount) AS TotalAmountPaid
FROM Passenger P
JOIN Booking B ON P.Passenger_ID = B.Passenger_ID
JOIN Payment Pay ON B.Booking_ID = Pay.Booking_ID
WHERE P.Passenger_ID = 1 
GROUP BY P.Passenger_ID, P.First_name;

-- 7. Retrieve Cancelled Bookings and Refund Amount
SELECT C.Cancellation_ID, B.Booking_ID, F.Flight_name, C.Issue_time
FROM Cancellation C
JOIN Booking B ON C.Booking_ID = B.Booking_ID
JOIN Flight F ON B.Flight_ID = F.Flight_ID;

-- 8. Retrieve Notifications Sent to a Passenger
SELECT N.Notification_ID, N.Message
FROM Notification N
JOIN Passenger P ON N.Passenger_ID = P.Passenger_ID
WHERE P.Passenger_ID = 1; 

-- 9. Retrieve Flights from a Specific Airline
SELECT F.Flight_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE
FROM Flight F
JOIN Airline A ON F.Origin_AP_Code = A.Airline_ID
WHERE A.Airline_ID = 'BA202'; 

-- 10. Retrieve All Reviews for a Flight
SELECT R.Review_ID, P.First_name, R.Rating, R.Comment, R.Date
FROM Review R
JOIN Passenger P ON R.Passenger_ID = P.Passenger_ID
WHERE R.Flight_ID = 101;  

-- 11. Get Airports with Specific Facilities
SELECT AP.AP_Code, AP.Airport_name, AP.Facilities
FROM Airport AP
WHERE AP.Facilities LIKE 'WiFi';

-- 12. Check Seat Map for a FlightSELECT F.Flight_ID, F.Flight_name, S.SeatMap
SELECT F.Flight_ID, F.Flight_name, S.Seat_Number 
FROM Flight F
JOIN seat_matrix S ON F.Flight_ID = S.Flight_ID
WHERE F.Flight_ID = 1;

-- 13. Update Booking Status
UPDATE Booking
SET Payment_Status = 'Confirmed'
WHERE Booking_ID = 1;

-- 14. Retrieve All Airlines Operating in a Specific Region
SELECT A.Airline_ID, A.Airline_name, A.Operating_Region
FROM Airline A
WHERE A.Operating_Region = 'Asia';

-- 15. Insert a New Review for a Flight
INSERT INTO Review (Review_ID, Passenger_ID, Flight_ID, Rating, Comment, Date)
VALUES (101, 1, 1, 5, 'Excellent service and on-time arrival!', NOW());

-- 16. Retrieve All Cancellations in a Specific Date Range
SELECT C.Cancellation_ID, B.Booking_ID, C.Reason
FROM Cancellation C
JOIN Booking B ON C.Booking_ID = B.Booking_ID
WHERE C.Issue_time BETWEEN '2024-11-01' AND '2024-11-5';

-- 17. Searching for Available Flights
SELECT F.Flight_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE
FROM Flight F
JOIN Airport AP ON F.Origin_AP_Code = AP.AP_Code
WHERE F.Origin_AP_CODE = 'SYD'
  AND F.Destination_AP_CODE = 'DXB'
  AND F.Departure_Time = '2024-12-04';

-- 18. Viewing Flight Details
SELECT F.Flight_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE, A.Airline_name, AP.Airport_Name
FROM Flight F
JOIN Airline A ON F.Origin_AP_Code = A.Airline_ID
JOIN Airport AP ON F.Origin_AP_Code = AP.AP_Code
WHERE F.Flight_ID = 1;

-- 20. Booking a Flight
INSERT INTO Booking (Booking_ID, Passenger_ID, Flight_ID, Payment_Status, Date)
VALUES (101, 1, 1, 'Pending', '2024-10-10');

-- 21. Viewing Booking Information
SELECT B.Booking_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE, B.Payment_Status
FROM Booking B
JOIN Flight F ON B.Flight_ID = F.Flight_ID
WHERE B.Passenger_ID = 1;

-- 22. Making Payments for Bookings
INSERT INTO Payment (Payment_ID, Booking_ID, Date, Amount, payment_method)
VALUES (7, 1, NOW(), 500.00, 'Credit Card');
UPDATE Booking
SET Payment_Status = 'Confirmed'
WHERE Booking_ID = 1;

-- 23. Cancelling a Booking
INSERT INTO Cancellation (Cancellation_ID, Booking_ID, Request_time, Issue_time, Reason)
VALUES (6, 1, '2024-11-02 11:15:00', NOW(), 'Flight Delayed');
UPDATE Booking
SET Payment_Status = 'Cancelled'
WHERE Booking_ID = 1;

-- 24. Viewing Flight Status (On-time, Delayed, etc.)
SELECT F.Flight_ID, F.Flight_name, F.Flight_Status
FROM Flight F
WHERE F.Flight_ID = 1;

-- 25. Receiving Notifications
SELECT N.Notification_ID, N.Message, N.Date
FROM Notification N
WHERE N.Passenger_ID = 1;

-- 26. Providing Feedback or Writing a Review
INSERT INTO Review (Review_ID, Passenger_ID, Flight_ID, Rating, Comment, Date)
VALUES (8, 1, 1, 5, 'Great flight, excellent service!', NOW());

-- 27. Viewing Available Services
SELECT S.Service_ID, S.Service_name
FROM Services S;

-- 28. Modifying Passenger Information
UPDATE Passenger
SET Email = 'new_email@example.com'
WHERE Passenger_ID = 1;

-- 29. Viewing Seat Availability (Seat Map)
SELECT S.Seat_number, S.Class
FROM Seat_matrix S
WHERE S.Flight_ID = 1 
AND S.Availability = 'Available';

-- 30. Viewing Refund Information for Cancelled Flights
SELECT C.Cancellation_ID, B.Booking_ID, C.Issue_time, C.Reason
FROM Cancellation C
JOIN Booking B ON C.Booking_ID = B.Booking_ID
WHERE B.Passenger_ID = 1;

-- 31. Viewing Flight History
SELECT F.Flight_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE, B.Payment_Status
FROM Flight F
JOIN Booking B ON F.Flight_ID = B.Flight_ID
WHERE B.Passenger_ID = 1
AND B.Payment_Status = 'Paid';

-- 32. Searching Flights by Time
SELECT F.Flight_ID, F.Flight_name, F.Origin_AP_CODE, F.Destination_AP_CODE, F.Departure_time
FROM Flight F
WHERE F.Departure_time BETWEEN '2024-12-01 11:00:00' AND '2024-12-02 12:30:00';
