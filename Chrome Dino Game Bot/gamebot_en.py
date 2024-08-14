from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard  

# Initiate WebDriver
driver = webdriver.Chrome()
driver.get('https://offline-dino-game.firebaseapp.com/')

# Wait for page to load
time.sleep(1)

# Press space to start the game
body = driver.find_element("xpath", "//body")
body.send_keys(Keys.SPACE)

while True:
    try:

        # Close the tab when "p" is pressed
        if keyboard.is_pressed('p'):
            driver.quit()
            break
        
        # Get dino and obstacle positions
        dino_position = driver.execute_script("return Runner.instance_.tRex.xPos;")
        obstacles = driver.execute_script("return Runner.instance_.horizon.obstacles;")
        current_speed = driver.execute_script("return Runner.instance_.currentSpeed;")

        if obstacles:
            obstacle = obstacles[0]
            obstacle_position = obstacle['xPos']
            obstacle_y_position = obstacle['yPos']
            obstacle_type = obstacle['typeConfig']['type']

            # Determine jump position based on speed and number of obstacles will be on the screen

            if 6 <= current_speed <= 8:
                jump_position = 155 if len(obstacles) > 1 else 120

            elif 8 < current_speed <= 11:
                jump_position = 145 if len(obstacles) > 1 else 125

            else:
                jump_position = 190
            
            # Check if it's time to jump

            if obstacle_position <= jump_position and obstacle_y_position != 50:
                body.send_keys(Keys.SPACE)
                time.sleep(0.1 if current_speed <= 11 else 0.5)
                body.send_keys(Keys.NULL)
        
        time.sleep(0.01)
    
    except Exception as e:
        print(f"Error occurred: {e}")
