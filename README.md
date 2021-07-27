# Diplomarbeit

Diplomarbeit "ML-based Chatbot" für das Jahr 2021/2022 von Dumfarth Felix und Lukas Starka unter Betreuung
von Herrn Professor Stütz.
## Links

[Index](https://github.com/htl-leonding-project/2021-da-chatbot/)

### Besprechungen
[1. Besprechung 22.02.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-02-22)

[2. Besprechung 09.03.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-03-09)

[3. Besprechung 23.03.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-03-23)

[4. Besprechung 06.04.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-04-06)

[5. Besprechung 20.04.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-04-20)

[6. Besprechung 29.04.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-04-29)

[7. Besprechung 11.05.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-05-11)

[8. Besprechung 01.06.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-06-01)

[9. Besprechung 17.06.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-06-17)

[10. Besprechung 22.07.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/2021-07-22)

# asciidoctor-docker-template

## Overview

This is a template-project for

* generating AsciiDoc-Files to html-files and
* deploying the html-files to gh-pages,
* where the gh-pages are located in an branch of the repo called `gh-pages`.

AsciiDoctor - the software for converting the .adoc-files to .html-files - is executed in a Docker container.
So you have nothing to install on your local machine, except Docker

## Option 1: Run script outside Docker - in your host OS

Two scripts are available:

* `build-html-docker.sh` -> builds the .html-pages in the folder gh-pages
* `publish-gh-pages.sh` -> builds and deploys the gh-pages

additionally is a script `build-pdf-docker.sh` for creating a pdf document.


## Option 2: [preferred] Run script inside Docker-container

* First create a `.env`-file with
```
GIT_GLOBAL_MAIL=<your email>
GIT_GLOBAL_USER_NAME=<your git - username>
```
* Then run the script `run-inside-docker.sh`.
* The url of the created gh-page will be displayed. 

## How to use Asciidoctor

Download the latest [release](https://github.com/htl-leonding-college/asciidoctor-docker-template/releases) in your project and run the shell-scripts.

## Demo Documents

You can find demo documents in the `asciidocs.demo`-folder:

- System Specification (Pflichtenheft)
- Minutes of Meeting
- some additional demos

