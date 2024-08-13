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
        # close tab when "p" is pressed
        if keyboard.is_pressed('p'):
            #print("Quitting The Game...")
            driver.quit()
            break
        
        # get dino positions 
        dino_position = driver.execute_script("return Runner.instance_.tRex.xPos;")
        obstacles = driver.execute_script("return Runner.instance_.horizon.obstacles;")

        # get the speed of t-rex
        current_speed = driver.execute_script("return Runner.instance_.currentSpeed;")
        
        #print(f"Current Speed: {current_speed:.1f}")  # to check current speed

        if obstacles: #gather some obstacle data if obstacles exists
            obstacle = obstacles[0]
            obstacle_position = obstacle['xPos']
            obstacle_y_position = obstacle['yPos']  
            obstacle_type = obstacle['typeConfig']['type']
            obstacle_height = obstacle['typeConfig']['height']
            obstacle_width = obstacle['typeConfig']['width']

            #print(f"Obstacle Type: {obstacle_type}, Height: {obstacle_height}, Width: {obstacle_width}") #to check obstacle info

            if 6 <= current_speed <= 8:     

                 #print(f"6-8 {obstacle_type} {current_speed:.2f}")      
                 
                 specific_position_to_jump = 152  #because there are some obstacles with a small gap between them so t-rex should jump earlier
    
                 if obstacle_position <= specific_position_to_jump and obstacle_y_position != 50:   # if obstacle_y_position == 50 means there is a PTERODACTY higher than t-rex so we don't need to jump 
                    
                    #print(f"{obstacle_position}") to check how far is the obstacle

                    body.send_keys(Keys.SPACE)
                    time.sleep(0.1)
                    body.send_keys(Keys.NULL)

            if 8 < current_speed <= 11:

                #print(f"8-11 {obstacle_type} {current_speed:.2f}") to check     
                
                specific_position_to_jump = 147 # no more small gaps between obstacles but there might be multiple large cactuses 
    
                if obstacle_position <= specific_position_to_jump and obstacle_y_position != 50:   
                   
                   #print(f"{obstacle_position} uzaklıktan zıplanıyor.")
                   body.send_keys(Keys.SPACE)
                   time.sleep(0.1)
                   body.send_keys(Keys.NULL)         
    

            elif current_speed > 11: 

                specific_position_to_jump = 190 

                if obstacle_position <= specific_position_to_jump and obstacle_y_position != 50:

                    #print(f"High Speed. Obstacle Position: {obstacle_position}, Time to Sleep: {time_to_sleep}") #to check

                    body.send_keys(Keys.SPACE)
                    time.sleep(0.5)
                    body.send_keys(Keys.NULL)

        # wait a while 
        time.sleep(0.01)
    except:
        print("")
