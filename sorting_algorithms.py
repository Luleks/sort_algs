import pygame
import random

class tower:
	def __init__(self, num):
		self.num = num
		self.color = AQUA

def insertion_sort(towers, win, is_sorted):
	for i in range(1, len(towers)):
		j = i - 1
		pom = towers[i]
		pom.color = RED
		draw(win, towers, is_sorted)
		while towers[j].num > pom.num and j >= 0:
			towers[j].color = RED
			pygame.time.delay(500)
			draw(win, towers, is_sorted)
			towers[j+1] = towers[j]
			towers[j] = pom
			pygame.time.delay(500)
			draw(win, towers, is_sorted)
			towers[j+1].color = AQUA
			j -= 1
		towers[j+1] = pom
		pygame.time.delay(500)
		draw(win, towers, is_sorted)
		towers[j+1].color = AQUA

def selection_sort(towers, win, is_sorted):
	for i in range(0, len(towers) - 1):
		mini = towers[i]
		mini.color = RED
		pygame.time.delay(500)
		draw(win, towers, is_sorted)
		index = i
		for j in range(i+1, len(towers)):
			towers[j].color = RED
			pygame.time.delay(500)
			draw(win, towers, is_sorted)
			if mini.num > towers[j].num:
				mini.color = AQUA
				mini = towers[j]
				index = j
				pygame.time.delay(500)
				draw(win, towers, is_sorted)
			else:
				towers[j].color = AQUA
				pygame.time.delay(500)
				draw(win, towers, is_sorted)
		towers[i].color = RED
		pygame.time.delay(500)
		draw(win, towers, is_sorted)
		towers[index] = towers[i]
		towers[i] = mini
		towers[index].color = AQUA
		towers[i].color = AQUA
		pygame.time.delay(500)
		draw(win, towers, is_sorted)

def bubble_sort(towers, win, is_sorted):
	change = True
	k = 1
	while change:
		change = False
		for i in range(len(towers)-k):
			towers[i].color = RED
			draw(win, towers, is_sorted)
			towers[i+1].color = RED
			pygame.time.delay(500)
			draw(win, towers, is_sorted)
			if towers[i].num > towers[i+1].num:
				towers[i], towers[i+1] = towers[i+1], towers[i]
				pygame.time.delay(500)
				draw(win, towers, is_sorted)
				change = True
			towers[i].color = AQUA
			pygame.time.delay(500)
			draw(win, towers, is_sorted)
		towers[-k].color = AQUA
		pygame.time.delay(500)
		draw(win, towers, is_sorted)
		k += 1

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
AQUA = (0, 255, 255)
RED = (255, 0, 0)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualiser Frfr")
FONT = pygame.font.SysFont("comicsans", 40)
FONT1 = pygame.font.SysFont("comicsans", 20)

def draw(win, towers, is_sorted):
	upper_row_text = [FONT.render("Insertion", True, BLACK), FONT.render("Selection", True, BLACK), FONT.render("Bubble", True, BLACK)]
	lower_row_text = [FONT.render("Quick", True, BLACK), FONT.render("Merge", True, BLACK), FONT.render("Tim", True, BLACK)]
	text = FONT.render("Sort", True, BLACK)
	text1 = FONT.render("Restart", True, BLACK)
	win.fill(WHITE)

	for i in range(3):
		win.blit(upper_row_text[i], (50 + 250 * i + 100 - upper_row_text[i].get_width()//2, 50))
		win.blit(lower_row_text[i], (50 + 250 * i + 100 - lower_row_text[i].get_width()//2, 450))
		win.blit(text, (50 + 250 * i + 100 - text.get_width()//2, 90))
		win.blit(text, (50 + 250 * i + 100 - text.get_width()//2, 490))
		pygame.draw.rect(win, BLACK, (50 + 250 * i, 50, 200, 100), 3)
		pygame.draw.rect(win, BLACK, (50 + 250 * i, 450, 200, 100), 3)

	for i in range(len(towers)):
		size = FONT1.render(str(towers[i].num), True, BLACK)
		pygame.draw.rect(win, towers[i].color, (50 + 70 * i, 200, 60, towers[i].num * 20))
		win.blit(size, (50 + 70 * i + 30 - size.get_width()//2, 200))

	if is_sorted:
		win.blit(text1, ((800 - text1.get_width()) // 2, 200 + (400 - text1.get_height()) // 2))

	pygame.display.update()
	
def main(win):
	run = True
	is_sorted = False
	towers = [tower(i) for i in range(1, 11)]
	random.shuffle(towers)
	towers_copy = towers.copy()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if 50 <= pos[0] <= 250 and 50 <= pos[1] <= 150:
					insertion_sort(towers, win, is_sorted)
					is_sorted = True
				elif 300 <= pos[0] <= 500 and 50 <= pos[1] <= 150:
					selection_sort(towers, win, is_sorted)
					is_sorted = True
				elif 550 < pos[0] <= 750 and 50 <= pos[1] <= 150:
					bubble_sort(towers, win, is_sorted)
					is_sorted = True
				elif 50 <= pos[0] <= 250 and 450 <= pos[1] <= 550:
					print("Quick")
				elif 300 <= pos[0] <= 500 and 450 <= pos[1] <= 550:
					print("Merge")
				elif 550 <= pos[0] <= 750 and 450 <= pos[1] <= 550:
					print("Time")
				elif is_sorted and 328 < pos[0] < 471 and 372 < pos[1] < 428:
					is_sorted = False
					towers = towers_copy.copy()
					draw(win, towers, is_sorted)

		draw(win, towers, is_sorted)


if __name__ == "__main__":
	main(win)
	pygame.quit()