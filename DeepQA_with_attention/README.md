# Spock to Barney: A Neural Machine Chatbot

S2B is a deep-learning based chatbot model that attempts at mimicing the personality, tone and style of speaking of various fictional characters. Some of these characters include Darth Vader (from the Original Star Wars Trilogy), Barney Stinson (from the How I Met Your Mother TV Series) and Spock (from the Star Trek TV Series and Movies).

Given below are a list of dependancies required to run the model. Please ensure that all of these dependancies are satisfied before attempting to run the model.

## Dependancies and Requirements

  - Python v3.6
  - Tensorflow v1.12.0
  - Git LFS

Once you are satisfied that these requirements are met, you can go ahead and clone this repository. Beware! Some of the files in this repository exceed 1.0 GB (neural model weights). Please do ensure that your system has enough space.

Perform the following steps in the prescribed order to get this model to run.

- Clone the Repository
- In ```bash```, move one directory up to the ```DeepQA_with_attention``` folder.
```sh
$ cd DeepQA_with_attention/
```
- Run the ```install.sh``` script. This script downloads the ```Python``` packages required for the correct functioning of this repository. The script will also download an ```nltk``` package called ```punkt``` required for data-processing. Please ensure that there are no firewalls set up that may prevent the ```nltk``` download from succeeding.
```sh
$ ./install.sh
```
- To run an interactive shell with either one of ```barney```, ```spock``` or ```vader```, run the command 
```sh
./testModel.sh <character-name>
```
where ```character-name``` is one of the prescribed options.
- You will now enter into an interactive shell where you can communicate with the desired chatbot. Please do not have unreasonable expectations from this rudimentary model. Try and keep your input statements shorter than 10 words (including punctuation).

# Have fun!
