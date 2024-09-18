# Exercise 1

## 1. what are the "max_bright" and "min_bright" values you found?
- The value I found for `max_bright` was 63000 which was found when in a bright sunny room.
- The value I found for `min_bright` was 5000 which was found when covered completely in that bright room.

# Exercise 2

## 1. Using the code in exercise_sound.py as a starting point, modify the code to play several notes in a sequence from a song of your choosing.
- I used the code in `exercise_sound.py` to play the song Jingle Bells.

# Exercise 3

## 1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
- To do this, I had to change `N` to 10 and modify the `scorer` function to populate a `dict` with the appropriate fields.

## 2. Have the Pi Pico automatically upload the response time data (say via HTTP POST to a REST server to a cloud server of your choice (e.g. Firebase, Heroku, etc.))
- For this, I used a a Firebase Realtime Database. Because my database was locked in production mode, I needed to store my authentication token on the Pi. I stored and read this token as JSON to make requests to the appropriate link.