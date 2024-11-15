# War
A rendition of the famous card game "War" written in Python using Pygame. The goal is to be the first player to win all 52 cards.

## The Deal
The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.

## The Play
Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.

If the cards are the same rank, it is War! Each player turns up one card face down and one card face up. The player with the higher cards takes both piles (six cards). If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. The player with the higher card takes all 10 cards, and so on.

## How to Keep Score
The game ends when one player has won all the cards.

## Installation and use


## Set-up & Installation
[Python](python.org/downloads) is a pre-requisite for the project. Click on the hyper-link to install Python. Follow the steps listed below to setup the "WAR" card game:

1. Clone the repository using:
```shell
git clone https://github.com/UffanMehmoodKhan/War
```
> ***Note:** You need to have `git` installed for this command to run. You can either go install git first, or click on the download button in the top-left corner to install the project onto your local computer.*

2. Now either move to the project directory through the terminal using `cd` or just open the terminal in the root folder `.../War` and create a virtual environment (venv):
```sh
py -m venv venv # this creates the venv
```
> ***Note:** This step is only for the first time setup.*
3. Activate the `venv` in the root directory (always activate the venv when you are working on the project, this is to ensure that the dependencies are propery packaged without any clash):
```sh
.\venv\Scripts\activate # this activates the venv
```

4. All the required project dependencies are listed in `requirements.txt` file. To download all the project dependencies, run the following command while having the venv activated and being in the root folder: 
```sh
pip install -r requirements.txt
```
> ***Note:** This step is only for the first time, do not repeat unless new dependencies are added to the ```requirements.txt``` file. **ALWAYS** remember to add any new dependency/library in the ```requirements.txt``` file.*

5. To run the application, move to the ```/src``` folder and run the ```war.py``` file using python
```sh
python war.py
```

## Game Mechanics
Press the *Play War* button to start the game. Pick a player on your own and continue pressing the *Draw Card* button till a winner is declared.

##

![Screenshot 2024-11-16 021631](https://github.com/user-attachments/assets/bb7e1c17-2ae9-4c52-900e-9a9b55da07db)
![Screenshot 2024-11-16 021657](https://github.com/user-attachments/assets/69e55764-6f8c-4359-ac7f-f4e8acb400cb)
![Screenshot 2024-11-16 021720](https://github.com/user-attachments/assets/e3f8eb97-6864-45df-9d96-c089e3e13b1b)
![Screenshot 2024-11-16 021850](https://github.com/user-attachments/assets/54b03e5a-85d5-4559-a669-16c8f4d7e118)





