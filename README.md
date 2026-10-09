# 🎬 Movie Ticket Booking System

A console-based Movie Ticket Booking System developed using **Python and MySQL**. This project allows users to view movies and shows, check seat availability, book tickets, and manage their bookings. Administrators can manage movies, theatres, screens, shows, and view all bookings.

## ✨ Features

### 👨‍💼 Admin Features
- Add and view movies
- Add and view theatres
- Add screens and automatically generate seats
- Schedule movie shows with dates, timings, and ticket prices
- View all customer bookings

### 👤 User Features
- User registration and login
- View available movies and shows
- Check available seats
- Book multiple seats
- Calculate the total ticket price
- View booking history
- Cancel bookings

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Database:** MySQL
- **Database Connector:** mysql-connector-python
- **Development Environment:** Visual Studio Code

## 📂 Project Structure

```text
Movie-Ticket-Booking/
│
├── main.py
├── README.md
├── .gitignore
└── env/                 # Local virtual environment (not tracked by Git)
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Movie-Ticket-Booking
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

Activate it on Windows:

```bash
env\Scripts\activate
```

### 3. Install the Required Package

```bash
pip install mysql-connector-python
```

### 4. Create the MySQL Database

Open MySQL Workbench and create the database:

```sql
CREATE DATABASE movie_ticket_booking;
```

Create the required tables before running the application. The application expects tables for users, movies, theatres, screens, seats, shows, bookings, and booking_seats, with the necessary relationships.

### 5. Configure the Database Connection

Update the MySQL connection settings in `main.py` with your local database credentials.

**Security note:** Do not commit database passwords or other sensitive credentials to GitHub.

### 6. Run the Application

```bash
python main.py
```

## 🚀 How to Use

1. Start the application.
2. Register a user account or log in.
3. Log in using an account with the `admin` role to access administrative features.
4. Administrators can add movies, theatres, screens, and shows.
5. Users can view shows, select available seats, and book tickets.
6. Users can view or cancel their bookings.

## 🗄️ Database Tables

The application uses the following tables:

| Table | Purpose |
|---|---|
| `users` | Stores user account details and roles |
| `movies` | Stores movie information |
| `theatres` | Stores theatre details |
| `screens` | Stores screens associated with theatres |
| `seats` | Stores seats available on each screen |
| `shows` | Stores movie show schedules and ticket prices |
| `bookings` | Stores customer booking details |
| `booking_seats` | Links booked seats to individual bookings |

## 🔒 Git and Security

The local virtual environment and sensitive configuration files should not be uploaded to GitHub.

Add the following to `.gitignore`:

```gitignore
env/
venv/
.venv/
__pycache__/
*.pyc
.env
```

## 🎯 Project Objective

The objective of this project is to demonstrate Python programming, MySQL database connectivity, SQL queries, CRUD operations, relational database design, and a basic ticket booking workflow.

## 👩‍💻 Author

**Kousalya Banda**

GitHub: [Visit My GitHub Profile](https://github.com/)

Portfolio: [Visit My Portfolio](https://kousalyabanda.github.io/portfolio/)
