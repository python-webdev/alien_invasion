"""Ship management for the Alien Invasion game.

Defines the Ship class, which loads the ship image, tracks its
position, and handles movement and rendering each frame.
"""

from pathlib import Path

import pygame

IMAGES_DIR = Path(__file__).resolve().parent / "images"


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(str(IMAGES_DIR / "ship.bmp"))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag: start with the ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
