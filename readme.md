# Rasa Prototype
## Talking to Your Assistant

To talk to your newly-trained assistant, run this command:

````
docker run -it -v $(pwd):/app rasa/rasa:2.8.0-full shell
````

## Training a Model

If you edit any training data, start for the first time or edit the `config.yml` file, you'll need to retrain your Rasa model. You can do so by running:

````
docker run -v $(pwd):/app rasa/rasa:2.8.0-full train --domain domain.yml --data data --out models
````
