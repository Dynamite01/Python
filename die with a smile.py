import time

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


lyrics = [
    ("So I'ma love you every night like it's the last night", 0.05, 0.2),  
    ("Like it's the last night", 0.07, 0.3),                               
    ("If the world was ending", 0.1, 0.1),                                    
    ("I'd wanna be next to you", 0.23, 0.7),                                 
    ("If the party was over", 0.13, 0.5),                                   
    ("And our time on Earth was through", 0.21, 0.5),                  
    ("I'd wanna hold you just for a while", 0.08, 0.5),              
    ("And die with a smile", 0.15, 0.15),                               
    ("If the world was ending", 0.2),                                  
    ("I'd wanna be next to you", 0.25, 0.7),                           
    ("If the world was ending", 0.2, 0.2),                            
    ("I'd wanna be next to you", 0.10, 0.7)                          
]


for line in lyrics:
    if len(line) == 2:  
        slow_print(line[0], line[1])
    elif len(line) == 3:  
        slow_print(line[0], line[1])
        time.sleep(line[2])

