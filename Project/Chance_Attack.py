import game_framework
import pico2d

import Title_Logo

Main_Screen_WIDTH,Main_Screen_HEIGHT=1020,767

pico2d.open_canvas(Main_Screen_WIDTH,Main_Screen_HEIGHT)
game_framework.run(Title_Logo)
pico2d.close_canvas() 