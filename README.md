to run the game use the following command:
python game.py


MOTIVATION:
In our endeavor to develop a game centered around the theme of political
accountability, we recognize the foundational importance of responsibility
within society. A key tenet of this principle is the notion that individual
well-being is intrinsically tied to the health and happiness of the collective. To
cultivate a thriving societal ecosystem, two primary facets demand attention:
the creation of a pollution-free environment and the cultivation of an
accountable governmental framework conducive to national development.
Addressing the imperative of environmental sustainability necessitates the
conscientious management of waste materials, which are significant
contributors to pollution. By imparting knowledge and practical skills related to
waste classification and recycling methods, individuals are empowered to
actively mitigate environmental degradation, fostering a cleaner and healthier
habitat for all.
Simultaneously, the quest for effective governance hinges upon the selection
of responsible and capable leaders. In this context, the game aims to educate
participants on the electoral process, equipping them with the understanding
and discernment required to make informed choices devoid of undue influence
or manipulation. By fostering civic awareness and promoting ethical
engagement in the political sphere, the game endeavors to cultivate a
generation of conscientious citizens poised to contribute positively to societal
progress.
In India, a prevalent lack of awareness regarding waste classification often
results in indiscriminate disposal of waste onto roads and into surrounding
areas. Despite this, municipal authorities provide designated dustbins for the
segregation of waste based on its type, including organic waste, medical waste,
hazardous waste, and recyclable waste. Recognizing the critical need to
address this issue, we developed a game aimed at educating players about
the various types of waste and the corresponding color-coded dustbins for
proper disposal.
Furthermore, in the realm of governance, there exists a vital need to cultivate
informed and active citizenship. To this end, we designed a game simulating
the voting process, thereby immersing players in a virtual environment where
they can engage in casting their votes for upcoming elections. Through this
interactive experience, players gain practical insights into the electoral process,
empowering them to make informed decisions and participate meaningfully in
shaping the future of their community and nation.GAMIFYING THE CAUSE:
In the game,player when started is given two options to choose a game. The
first option is to classify the waste in accordance to the dustbins. Waste is
pushed on a conveyor belt and there are four dustbins present and at the end
of the conveyor belt and the player is supposed to click on the dustbin so that
the waste falls into it. so in this way player gets to know about waste
management and is awarded score based on his performance. we tried to
include levels of difficulty for the speed of the items on the conveyor belt. the
higher the difficulty the greater the speed of the waste on the conveyor belt.
The second game is a simulation for voting process in elections. Player is
required to interact with the character in the game using mouse and keyboard.
Using arrow keys player moves the character in the game and follows the
instructions accordingly and the character in the game is involved in the
elections. so player gets an idea on how elections take place and might
become responsible because of the interest in this field. We tried to implement
points for the player in the game based on his decisions. like for example we tried to include electoral bribery and if the player accepts it then his social
accountability decreases. but this was not possible due to time constraints.
The language we choosed is python and the library we choosed to use is
pygame which is a wrapper of SDL in python.
IMPLEMENTATION HIGHLIGHTS:
This game was mainly focussed to be perfect in tems of precision and UI and some good
game logic. Ui is most responsive and doesn’t have lag in terms of feedback. the action is
immediately shown in the game. Game has zero latency and great responsiveness.In the
election simulation part the game logic is written in such a way that adding any number of
players is possible and we can automove them if there path is decided beforehand. Player
is given messages in the form of message box such that he gets information about the
particular part of the game. this is designed in such a way that once a player is given a
message at a particular location he doesn’t get the message again if he re visits the place
bakc because he already knows the instrucitions. while some of the messages are left
wantledly away from this category because the player might want to know some
information regarding a particular character in the game again . so he can come back and
can still get the information.So these form some good game logic components of the
game that we implemented.Some sophisticated game mechanism which we impemented
was using states. there are a lot of states in the game and handling them was a good
game logic.
We might feel some irresponsiveness in some of the parts of the game that the character
in the game is not moving but this shouldn’t be considered as a bad feedback. his
movement is restricted because that part of the game requires the player to stand still
without any movement. this shouldn’t be considered as a lag in feedback.The waste classification game also has sophisticated logic. This was implemented using
states of the game and has good ui and feedback. feedback is very fast and the game is
very responsive and doesn’t have and delay in the feedback.So this game has zero
latency and has great responsiveness.The object when rotated on the conveyor belt
vertically shouldn’t fall off the belt. but in the game it moves exactly as the belt moves. so
making this involves a good sophisticated game logic.
Due to lack of time some of the metrics which we traded off were scoring mechanisms in
the election simulation game and some game logic was sacrificed due to time in waste
classification game in which we thought to implement seperating of waste from a single
object into multiple waste and then trashing it.
