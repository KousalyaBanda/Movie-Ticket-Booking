import mysql.connector


# ==============================
# DATABASE CONNECTION
# ==============================

connection = mysql.connector.connect(
    host="localhost",
    user="test",
    password="Kousalya@1125",
    database="movie_ticket_booking"
)

cursor = connection.cursor()

print("Database connected successfully!")


# ==============================
# REGISTER
# ==============================

def register():

    print("\n===== REGISTER =====")

    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    query = """
    INSERT INTO users (name, email, password)
    VALUES (%s, %s, %s)
    """

    values = (name, email, password)

    cursor.execute(query, values)
    connection.commit()

    print("Registration successful!")


# ==============================
# LOGIN
# ==============================

def login():

    print("\n===== LOGIN =====")

    email = input("Enter email: ")
    password = input("Enter password: ")

    query = """
    SELECT user_id, name, role
    FROM users
    WHERE email = %s AND password = %s
    """

    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    if user:

        print("Login successful!")
        print("Welcome", user[1])

        return user

    else:

        print("Invalid email or password")

        return None


# ==============================
# ADD MOVIE
# ==============================

def add_movie():

    print("\n===== ADD MOVIE =====")

    title = input("Movie title: ")
    genre = input("Genre: ")
    language = input("Language: ")
    duration = int(input("Duration in minutes: "))
    release_date = input("Release date (YYYY-MM-DD): ")
    description = input("Description: ")

    query = """
    INSERT INTO movies
    (title, genre, language, duration, release_date, description)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        title,
        genre,
        language,
        duration,
        release_date,
        description
    )

    cursor.execute(query, values)
    connection.commit()

    print("Movie added successfully!")


# ==============================
# VIEW MOVIES
# ==============================

def view_movies():

    print("\n===== MOVIES =====")

    query = """
    SELECT movie_id, title, genre, language, duration, release_date
    FROM movies
    """

    cursor.execute(query)

    movies = cursor.fetchall()

    if len(movies) == 0:

        print("No movies available.")

    else:

        for movie in movies:

            print("----------------------------")
            print("Movie ID:", movie[0])
            print("Title:", movie[1])
            print("Genre:", movie[2])
            print("Language:", movie[3])
            print("Duration:", movie[4], "minutes")
            print("Release Date:", movie[5])


# ==============================
# ADD THEATRE
# ==============================

def add_theatre():

    print("\n===== ADD THEATRE =====")

    name = input("Theatre name: ")
    location = input("Location: ")

    query = """
    INSERT INTO theatres
    (theatre_name, location)
    VALUES (%s, %s)
    """

    cursor.execute(query, (name, location))

    connection.commit()

    print("Theatre added successfully!")


# ==============================
# VIEW THEATRES
# ==============================

def view_theatres():

    print("\n===== THEATRES =====")

    query = """
    SELECT theatre_id, theatre_name, location
    FROM theatres
    """

    cursor.execute(query)

    theatres = cursor.fetchall()

    if len(theatres) == 0:

        print("No theatres available.")

    else:

        for theatre in theatres:

            print(
                theatre[0],
                theatre[1],
                theatre[2]
            )


# ==============================
# ADD SCREEN
# ==============================

def add_screen():

    print("\n===== ADD SCREEN =====")

    view_theatres()

    theatre_id = int(
        input("Enter theatre ID: ")
    )

    screen_name = input(
        "Enter screen name: "
    )

    total_seats = int(
        input("Enter number of seats: ")
    )

    query = """
    INSERT INTO screens
    (theatre_id, screen_name, total_seats)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            theatre_id,
            screen_name,
            total_seats
        )
    )

    screen_id = cursor.lastrowid

    # Create seats automatically

    for i in range(1, total_seats + 1):

        seat_number = "S" + str(i)

        if i <= total_seats // 2:

            seat_type = "Regular"

        else:

            seat_type = "Premium"

        query = """
        INSERT INTO seats
        (screen_id, seat_number, seat_type)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (
                screen_id,
                seat_number,
                seat_type
            )
        )

    connection.commit()

    print("Screen added successfully!")
    print("Seats created automatically!")


# ==============================
# ADD SHOW
# ==============================

def add_show():

    print("\n===== ADD SHOW =====")

    view_movies()

    movie_id = int(
        input("Enter movie ID: ")
    )

    print("\nAvailable Screens")

    query = """
    SELECT screen_id, screen_name
    FROM screens
    """

    cursor.execute(query)

    screens = cursor.fetchall()

    for screen in screens:
        print(
            "Screen ID:", screen[0],
            "| Screen Name:", screen[1]
        )
    screen_id = int(
        input("Enter screen ID: ")
    )

    show_date = input(
        "Show date (YYYY-MM-DD): "
    )

    start_time = input(
        "Start time (HH:MM:SS): "
    )

    end_time = input(
        "End time (HH:MM:SS): "
    )

    ticket_price = float(
        input("Ticket price: ")
    )

    query = """
    INSERT INTO shows
    (movie_id, screen_id, show_date,
     start_time, end_time, ticket_price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        movie_id,
        screen_id,
        show_date,
        start_time,
        end_time,
        ticket_price
    )

    cursor.execute(query, values)

    connection.commit()

    print("Show added successfully!")


# ==============================
# VIEW SHOWS
# ==============================

def view_shows():

    print("\n===== SHOWS =====")

    query = """
    SELECT
        s.show_id,
        m.title,
        t.theatre_name,
        sc.screen_name,
        s.show_date,
        s.start_time,
        s.ticket_price

    FROM shows s

    JOIN movies m
        ON s.movie_id = m.movie_id

    JOIN screens sc
        ON s.screen_id = sc.screen_id

    JOIN theatres t
        ON sc.theatre_id = t.theatre_id

    ORDER BY s.show_date, s.start_time
    """

    cursor.execute(query)

    shows = cursor.fetchall()

    if len(shows) == 0:

        print("No shows available.")

    else:

        for show in shows:

            print("----------------------------")

            print("Show ID:", show[0])
            print("Movie:", show[1])
            print("Theatre:", show[2])
            print("Screen:", show[3])
            print("Date:", show[4])
            print("Time:", show[5])
            print("Price:", show[6])


# ==============================
# AVAILABLE SEATS
# ==============================

def available_seats(show_id):

    query = """
    SELECT
        se.seat_id,
        se.seat_number,
        se.seat_type

    FROM seats se

    JOIN shows sh
        ON se.screen_id = sh.screen_id

    WHERE sh.show_id = %s

    AND se.seat_id NOT IN

    (
        SELECT bs.seat_id

        FROM booking_seats bs

        JOIN bookings b
            ON bs.booking_id = b.booking_id

        WHERE b.show_id = %s
    )
    """

    cursor.execute(
        query,
        (show_id, show_id)
    )

    return cursor.fetchall()


# ==============================
# BOOK TICKET
# ==============================

def book_ticket(user_id):

    print("\n===== BOOK TICKET =====")

    view_shows()

    show_id = int(
        input("Enter show ID: ")
    )

    seats = available_seats(show_id)

    if len(seats) == 0:

        print("No seats available.")

        return

    print("\nAvailable Seats")

    for seat in seats:

        print(
            seat[0],
            "-",
            seat[1],
            "(",
            seat[2],
            ")"
        )

    seat_input = input(
        "Enter seat IDs separated by comma: "
    )

    seat_ids = []

    for value in seat_input.split(","):

        seat_ids.append(
            int(value.strip())
        )

    available_ids = []

    for seat in seats:

        available_ids.append(
            seat[0]
        )

    for seat_id in seat_ids:

        if seat_id not in available_ids:

            print(
                "Seat",
                seat_id,
                "is not available."
            )

            return

    # Get ticket price

    query = """
    SELECT ticket_price
    FROM shows
    WHERE show_id = %s
    """

    cursor.execute(
        query,
        (show_id,)
    )

    result = cursor.fetchone()

    ticket_price = float(
        result[0]
    )

    total_amount = (
        ticket_price * len(seat_ids)
    )

    print(
        "Total amount: ₹",
        total_amount
    )

    confirm = input(
        "Confirm booking? (Y/N): "
    )

    if confirm.upper() != "Y":

        print("Booking cancelled.")

        return

    # Create booking

    query = """
    INSERT INTO bookings
    (user_id, show_id, total_amount)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            user_id,
            show_id,
            total_amount
        )
    )

    booking_id = cursor.lastrowid

    # Add seats

    for seat_id in seat_ids:

        query = """
        INSERT INTO booking_seats
        (booking_id, seat_id)
        VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (
                booking_id,
                seat_id
            )
        )

    connection.commit()

    print("\n============================")
    print("     BOOKING SUCCESSFUL")
    print("============================")
    print("Booking ID:", booking_id)
    print("Tickets:", len(seat_ids))
    print("Total: ₹", total_amount)


# ==============================
# MY BOOKINGS
# ==============================

def my_bookings(user_id):

    print("\n===== MY BOOKINGS =====")

    query = """
    SELECT
        b.booking_id,
        m.title,
        t.theatre_name,
        s.show_date,
        s.start_time,
        b.total_amount

    FROM bookings b

    JOIN shows s
        ON b.show_id = s.show_id

    JOIN movies m
        ON s.movie_id = m.movie_id

    JOIN screens sc
        ON s.screen_id = sc.screen_id

    JOIN theatres t
        ON sc.theatre_id = t.theatre_id

    WHERE b.user_id = %s
    """

    cursor.execute(
        query,
        (user_id,)
    )

    bookings = cursor.fetchall()

    if len(bookings) == 0:

        print("No bookings found.")

    else:

        for booking in bookings:

            print("----------------------------")

            print(
                "Booking ID:",
                booking[0]
            )

            print(
                "Movie:",
                booking[1]
            )

            print(
                "Theatre:",
                booking[2]
            )

            print(
                "Date:",
                booking[3]
            )

            print(
                "Time:",
                booking[4]
            )

            print(
                "Amount: ₹",
                booking[5]
            )


# ==============================
# CANCEL BOOKING
# ==============================

def cancel_booking(user_id):

    print("\n===== CANCEL BOOKING =====")

    my_bookings(user_id)

    booking_id = int(
        input("Enter booking ID: ")
    )

    query = """
    SELECT booking_id
    FROM bookings
    WHERE booking_id = %s
    AND user_id = %s
    """

    cursor.execute(
        query,
        (booking_id, user_id)
    )

    booking = cursor.fetchone()

    if booking is None:

        print("Booking not found.")

        return

    # Delete booking seats first

    query = """
    DELETE FROM booking_seats
    WHERE booking_id = %s
    """

    cursor.execute(
        query,
        (booking_id,)
    )

    # Delete booking

    query = """
    DELETE FROM bookings
    WHERE booking_id = %s
    """

    cursor.execute(
        query,
        (booking_id,)
    )

    connection.commit()

    print("Booking cancelled successfully!")


# ==============================
# VIEW ALL BOOKINGS - ADMIN
# ==============================

def view_all_bookings():

    print("\n===== ALL BOOKINGS =====")

    query = """
    SELECT
        b.booking_id,
        u.name,
        m.title,
        t.theatre_name,
        s.show_date,
        s.start_time,
        b.total_amount
    FROM bookings b
    JOIN users u
        ON b.user_id = u.user_id
    JOIN shows s
        ON b.show_id = s.show_id
    JOIN movies m
        ON s.movie_id = m.movie_id
    JOIN screens sc
        ON s.screen_id = sc.screen_id
    JOIN theatres t ON sc.theatre_id = t.theatre_id ORDER BY b.booking_date DESC"""
    cursor.execute(query)
    bookings = cursor.fetchall()
    if len(bookings) == 0:
        print("No bookings found.")
    else:
        for booking in bookings:
            print("----------------------------")
            print("Booking ID:", booking[0])
            print("Customer:", booking[1])
            print("Movie:", booking[2])
            print("Theatre:", booking[3])
            print("Date:", booking[4])
            print("Time:", booking[5])
            print("Amount:", booking[6])
# ==============================
# ADMIN MENU
# ==============================

def admin_menu():
    while True:
        print("\n==============================")
        print("         ADMIN MENU")
        print("==============================")

        print("1. Add Movie")
        print("2. View Movies")
        print("3. Add Theatre")
        print("4. View Theatres")
        print("5. Add Screen")
        print("6. Add Show")
        print("7. View Shows")
        print("8. View All Bookings")
        print("9. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            add_theatre()
        elif choice == "4":
            view_theatres()
        elif choice == "5":
            add_screen()
        elif choice == "6":
            add_show()
        elif choice == "7":
            view_shows()
        elif choice == "8":
            view_all_bookings()
        elif choice == "9":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")
# ==============================
# USER MENU
# ==============================
def user_menu(user_id):
    while True:
        print("\n==============================")
        print("          USER MENU")
        print("==============================")
        print("1. View Movies")
        print("2. View Shows")
        print("3. Book Ticket")
        print("4. My Bookings")
        print("5. Cancel Booking")
        print("6. Logout")
        choice = input(
            "Enter choice: "
        )
        if choice == "1":
            view_movies()
        elif choice == "2":
            view_shows()
        elif choice == "3":
            book_ticket(user_id)
        elif choice == "4":
            my_bookings(user_id)
        elif choice == "5":
            cancel_booking(user_id)
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")
# ==============================
# MAIN MENU
# ==============================
while True:
    print("\n==============================")
    print("    MOVIE TICKET BOOKING")
    print("==============================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        user = login()
        if user:
            user_id = user[0]
            role = user[2]
            if role == "admin":
                admin_menu()
            else:
                user_menu(user_id)
    elif choice == "3":
        print("Thank you for using Movie Ticket Booking!")
        break
    else:
       print("Invalid choice.")
# ==============================
# CLOSE CONNECTION
# ==============================
cursor.close()
connection.close()