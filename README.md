# gym_taxi
An agent trained by SARSA lambda reinforcement learning algorithm to play the OpenAI Gym Taxi game.

The Jupyter notebook contains the code for the SARSA lambda algorithm.
SARSA is based on the idea that we create episodes which we use to shape our policy. This is useful if we are not familiar with the whole model or covering every possibility would be impossible. Unlike in the case of the similar Monte Carlo algorithm, we take only one step in the episode and predict the remaining of the reward from the state we end up in. The policy determines in which state which action we must take to maximize the reward we get at the end of the episode. We then iteratively use numerous episodes to refine our estimation for each state-action pair.
Lambda indicates the use of the so-called decaying trace. After taking an action in a state, the trace determines how much the value of a state-action pair changes. We increase the trace of the state-action pair we just met and decrease the trace for every other state-action pair, thus the state-action pair we met the longer in the past will change the less.
During the algorithm it would make sense to pair the action to a given state that yields the maximum reward in the current situation. However, acting always greedily could prevent us from finding state-action pairs that would reward us with even larger rewards in the long run. To avoid this mistake, we utilize the idea of the epsilon greedy policy. In every state we choose the best possible action with the highest possibility but leave a small chance to choose another action. We can think of this idea as balancing between exploitation and exploration.

The model is trained during 10.000 games of Taxi, one game counts as one episode which can include up to 200 steps.
The description of Taxi can be found in the Gymnasium Documentation: https://gymnasium.farama.org/environments/toy_text/taxi/

The policy is stored as a Python dictionary which is serialized using the pickle library.
In the main program the policy is unpickled and then used to play the game for 1000 steps.
The learning and the testing are separated because not every notebook environment supports the graphical rendering of the OpenAI Gym and witnessing our agent visually is more fun. :)
The terminal displays if a round of Taxi is over, how many points our agent collected during one round and the entire 1000 steps.
The result is not perfect, in some states the agent can get stuck. To improve the agent, a larger number of episodes can be used for training or other reinforcement learning algorithms can be used.
