asteroids
=========

A basic asteroids game using PyGame.

The program consists of three modules:

* asteroids.py      - Contains the game loop and runs the game
* ship.py           - A class to create, update, and draw the ship
* asteroid.py       - A class to create, update, and draw an asteroid

To-do
-----

1. Implement leading-edge wrapping for asteroids, in all directions.
2. Distribute creation of asteroids around the edge of the whole screen, with random inward velocities.
3. Add user control of ship rotation, using left and right arrow keys. Start turning on key_down, stop turning on key_up.
4. Add thrusters to the ship, using up arrow key. Start thrusters on key_down, stop thrusters on key_up.
5. Implement "inertia-based" motion with acceleration and a constant top-speed.
6. Implement trailing-edge wrapping for the ship, in all directions.
7. Implement ship/asteroid collisions.
8. Implement bullets, with wrapping, and a maximum life.
9. Implement bullet/asteroid collisions.
