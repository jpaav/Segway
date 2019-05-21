import sys

import pygame as pg

import game

if __name__ == '__main__':
	game_obj = game.Game()
	exit_code = game_obj.start()
	pg.quit()
	sys.exit(exit_code)
