class Movie:
    def __init__(self, movie_id, title, genre, duration, language):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.duration = duration
        self.language = language
    
    def __str__(self):
        return f"{self.title} ({self.language}) - {self.genre}, {self.duration} mins"



class Theater:
    def __init__(self, theater_id, name, location):
        self.theater_id = theater_id
        self.name = name
        self.location = location
        self.screens = []

    def add_screen(self, screen):
        self.screens.append(screen)
        print(f"Screen {screen.screen_id} added to theater '{self.name}'.")

    def get_shows_by_movie(self, movie_id):
        shows = []
        for screen in self.screens:
            shows.extend(screen.get_shows_by_movie(movie_id))

        return shows

    def __str__(self):
        """
        Return a string representation of the theater.
        """
        return f"Theater: {self.name}, Location: {self.location}, Screens: {len(self.screens)}"


class Screen:
    def __init__(self, screen_id, capacity):
        self.screen_id = screen_id
        self.capacity = capacity
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)
        print(f"Show '{show.show_id}' for movie '{show.movie.title}' added to Screen {self.screen_id}.")

    def get_shows_by_movie(self, movie_id):
        return [show for show in self.shows if show.movie.movie_id == movie_id]
    

    def __str__(self):
        return f"Screen {self.screen_id} with Capacity: {self.capacity}, Shows: {len(self.shows)}"


class Show:
    def __init__(self, show_id, movie, screen, time):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.time = time
        self.available_seats = set(range(1, screen.capacity + 1))

    def get_available_seats(self):
        return sorted(self.available_seats)

    def book_seat(self, seat_id):
        if seat_id in self.available_seats:
            self.available_seats.remove(seat_id)
            print(f"Seat {seat_id} booked for show '{self.show_id}' of movie '{self.movie.title}'.")
            return True
        else:
            print(f"Seat {seat_id} is not available for show '{self.show_id}'.")
            return False

    def __str__(self):
        """
        Return a string representation of the show.
        """
        return f"Show {self.show_id}: '{self.movie.title}' at {self.time}, Available Seats: {len(self.available_seats)}"




def main():
    # Step 1: Create Movies
    movie1 = Movie(movie_id=1, title="Inception", genre="Sci-Fi", duration=148, language="English")
    movie2 = Movie(movie_id=2, title="Parasite", genre="Thriller", duration=132, language="Korean")
    print("Movies created:")
    print(movie1)
    print(movie2)
    print()

    # Step 2: Create a Theater
    theater = Theater(theater_id=1, name="Grand Cinema", location="Downtown")
    print(f"Theater created: {theater}")
    print()

    # Step 3: Add Screens to the Theater
    screen1 = Screen(screen_id=1, capacity=50)
    screen2 = Screen(screen_id=2, capacity=75)
    theater.add_screen(screen1)
    theater.add_screen(screen2)
    print()

    # Step 4: Schedule Shows
    show1 = Show(show_id=101, movie=movie1, screen=screen1, time="3:00 PM")
    show2 = Show(show_id=102, movie=movie2, screen=screen1, time="6:00 PM")
    show3 = Show(show_id=103, movie=movie1, screen=screen2, time="4:00 PM")
    screen1.add_show(show1)
    screen1.add_show(show2)
    screen2.add_show(show3)
    print()

    # Step 5: Display Shows for a Movie
    movie_shows = theater.get_shows_by_movie(movie_id=1)
    print(f"Shows for Movie 'Inception':")
    for show in movie_shows:
        print(f"- Show ID: {show.show_id}, Time: {show.time}, Screen: {show.screen.screen_id}")
    print()

    # Step 6: Seat Booking
    print("Available seats for Show 101:", show1.get_available_seats())
    show1.book_seat(1)  # Book Seat 1
    show1.book_seat(2)  # Book Seat 2
    print("Available seats after booking:", show1.get_available_seats())
    show1.book_seat(1)  # Try booking an already booked seat
    print()

    # Step 7: Final Summary
    print(f"Theater Details:\n{theater}")
    print(f"Screen 1 Details:\n{screen1}")
    print(f"Show 101 Details:\n{show1}")

if __name__ == "__main__":
    main()
