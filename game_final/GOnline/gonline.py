import pygame

size = [1100, 800]
blue = (100, 149, 237)
black = (0, 0, 0)
brown = (165,42,42)
white = (255, 255, 255)
green =(0,100,0)
red = (255,0,0)
dark_red = (200,0,0)
grey = (100,100,100)
other_grey = (0,0,100)
background = 'Mahogany.jpg'
pass_count = 0
player = 1
clock = pygame.time.Clock()

class Player():
	def ___init__(self,id=1):
		self.id = 1

class Position():
	def position(self):
		x = mouse.get_pos()[0]
		y = mouse.get_pos()[1]
		return (x,y)
class Stone(object):
	def __init__(self,board,position,color):
		self.board = board
		self.position = position
		self.color = color
		self.placeStone()
	def placeStone(self):
		coords = (self.position[0] * 50,  self.position[1] * 50)
		pygame.draw.circle(self.board,self.color,coords,20,0)
	
		pygame.display.update()
	def remove(self):
		blit_coords = (self.position[0] - 20, self.position[1] - 20)
		area_rect = pygame.Rect(blit_coords, (40, 40))
		screen.blit(background, blit_coords, area_rect)
		pygame.display.update()
		self.remove()	
	
		
class Board(object):	
	def draw_board(self):
		for i in range(12):
				for j in range(12):
					rect = pygame.Rect(55 + (50 * i), 100 + (50 * j), 50, 50)
					pygame.draw.rect(background, blue, rect, 1)
		screen.blit(background, (0,0))
		pygame.display.update()
		
	def text_objects(self,text, font):
		textSurface = font.render(text, True, black)
		
		return textSurface, textSurface.get_rect()

	def button(self,msg,x,y,w,h,ic,ac,action = None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(screen, ac,(x,y,w,h))
			
			if click[0] == 1 and action != None:
				action()
		else:
			pygame.draw.rect(screen, ic,(x,y,w,h))

		smallText = pygame.font.Font("freesansbold.ttf",20)
		textSurf, textRect = self.text_objects(msg, smallText)
		textRect.center = ( (x+(w/2)), (y+(h/2)) )
		screen.blit(textSurf, textRect)
	
	def quit_game(self):
		pygame.quit()
		quit()
	
	def removefromboard(self,stones,score):
		for stone in stones:
			x = stone[0]
			y = stone[1]
			if stone[2] == white:
				if (((x-1,y,black) in stones) and ((x+1,y,black) in stones) and ((x,y+1,black) in stones) and ((x,y-1,black) in stones)):
					score += 5
					stones.remove(stone)
					self.draw_board()
					for stone in stones:
						Stone(screen,(stone[0],stone[1]),stone[2])
			elif stone[2] == black:
				if (((x-1,y,white) in stones) and ((x+1,y,white) in stones) and ((x,y+1,white) in stones) and ((x,y-1,white) in stones)):
					score += 5
					stones.remove(stone)
					self.draw_board()
					for stone in stones:
						Stone(screen,(stone[0],stone[1]),stone[2])
						
	def pass_turn(self):
		global pass_count
		pass_count += 1
		if pass_count == 2:
			self.quit_game()
	def add_score(self,score):
		score = score + 1
	def score(self,player_text, score):
		return player_text + str(score)		

	def game_intro(self):

		intro = True
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			screen.blit(background, (0,0))
			largeText = pygame.font.SysFont("comicsansms",60)
			TextSurf, TextRect = self.text_objects("GONLINE", largeText)
			TextRect.center = ((1100/2),(800/2))
			screen.blit(TextSurf, TextRect)

			self.button("Play!",200,500,100,100,grey,other_grey,self.play_game)
			self.button("Quit!",700,500,100,100,red,dark_red,self.quit_game)

			pygame.display.update()
			clock.tick(15)
	def play_game(self):
		global pass_count
		width = 20
		height = 20 
		space_between = 5 
		score1 = 0
		score2 = 0.5
		global player
		finish = False
		stones = []
		self.draw_board()
		while not finish:

			self.button("Quit!",950,200,100,100,red,dark_red,self.quit_game)
			self.button(self.score("Player 1: ", score1),750,400,300,110,white,white)
			self.button(self.score("Player 2: ",score2),750,600,300,110,white, white)
			pass_button = pygame.draw.rect(screen,grey,(750,200,100,100))
			font = pygame.font.Font("freesansbold.ttf",20)
			pass_text = font.render("Pass!", True, black)
			screen.blit(pass_text, (773,239))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:  
					finish = True  
				elif event.type == pygame.MOUSEBUTTONDOWN and player == 1:
					position = pygame.mouse.get_pos()
					if (event.button == 1) and (position[0] > 55 and position[0] < 710) and (position[1] > 100 and position[1] < 750):
						x = int(round(((position[0]) / 50.0), 0))
						y = int(round(((position[1]) / 50.0), 0))
						stones.append((x,y,white))
						Stone(screen,(x,y),white)
						score1 += 1
						player = 2
						self.removefromboard(stones,score1)
						pass_count = 0
						
					elif (event.button == 1) and (position[0] >= 750 and position[0] <= 850) and (position[1] > 200 and position[1] < 300):

						self.pass_turn()
						player = 2
				elif event.type == pygame.MOUSEBUTTONDOWN and player == 2:
					position = pygame.mouse.get_pos()
					if (event.button == 1) and(position[0] > 55 and position[0] < 710) and (position[1] > 100 and position[1] < 750):
						x = int(round(((position[0]) / 50.0), 0))
						y = int(round(((position[1] ) / 50.0), 0))
						stones.append((x,y,black))
						Stone(screen,(x,y),black)
						score2 += 1
						player = 1
						self.removefromboard(stones,score2)
						pass_count = 0
								
							
							
					elif (event.button == 1) and (position[0] >= 750 and position[0] <= 850) and (position[1] > 200 and position[1] < 300):

						self.pass_turn()
						player = 1
			
			
			
			
			clock.tick(60)
			

			pygame.display.update()
			
		 
		pygame.quit()
	
def main():
	pygame.init()
	global screen
	screen = pygame.display.set_mode(size, 0, 32) 
	pygame.display.set_caption("Go_Online")
	global background
	background = pygame.image.load(background).convert()
	board = Board()
	board.game_intro()	
	
if __name__ == "__main__":
	main()