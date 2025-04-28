Warning! This game demo may induce motion sickness with the forced fullscreen and high speed objects moving around.

How to run:<br/>
Python 3.x and the Pygame library are required to run this demo.<br/>
Once installed, the "Dodge Game.bat" file will launch the game assuming Python has been added to the system PATH during install.<br/>

Controls:<br/>
Player 1 - left/right<br/>
Player 2 - A/D

Should'ves/Could'ves:<br/>
- I should have added more code comments while developing, but I consider this demo project completed and will not be revisiting.
- I planned to add networking play, but I settled for local 2 player. This was decided due to two main factos:<br/>
  - The framerate based logic to control the gameplay should have been time-step based to account for the network traffic fequency. The game is locked to 240 frames/sec but networking maxes out at 30-60/sec.
  - To combat the latency experience by player 2 vs the high speed objects moving, I would have needed client-side prediciton and server-side reconciliation logic to help maintain fairness.

While I could have done these things, I maintain that this was and always will be a demo. Therefore, I didn't want to spend more time than I thought was worth it on this.
