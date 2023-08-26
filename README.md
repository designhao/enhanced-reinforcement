# Advanced Reinforcement Learning Assignment

## Overview:
The following files are essential to build and design your reinforcement learning algorithm.

- [common.py](common.py) with constants
- [util.py](util.py) with utility functions
- [game.py](game.py) with graphic display related calls
- [environment.py](environment.py) features behavioural aspects of the scenario
- [agent.py](agent.py) includes components for training like environment interaction and previous state
- [link.py](link.py) holds skeleton of methods for you to develop (This is the only file you're allowed to modify)

We have also got a illustrative GIF to better explain the scenario.

## How to Execute:

On enabling the `--debug` flag, verbose output of training and GUI's Q(s, a) colouring can be visualised. The GUI execution can alternate between standard and debug modes via SPACE key.

To test your code and determine the convergence episode, the environment.py file can be utilised:
```
python environment.py [--debug] [Map]
```

Post-convergence, to analyse the solution provided by your algorithm, initiate the GUI in debug mode and observe the colours:
```
python game.py [--debug] [Map]
```
Bright colours depict preferred directions, as a consequence of the learning phase.

## What to Implement:

The file [link.py](link.py) provides an elementary structure to establish your active reinforcement learning algorithm.

During the training phase, the following steps take place:
- An action is chosen and implemented in the environment
- Rewards are verified and learning about the executed action takes place (via a utility table)
- Upon reaching a terminal state, the convergence metric is evaluated
- Depending on whether it achieves convergence, the training either stops or the utility table's previous state is stored for another training episode.

In the provided skeleton, you are responsible for developing the method to update the utility t