# Diplomarbeit

Diplomarbeit "Chatbot" für das Jahr 2021/2022 von Dumfarth Felix und Lukas Starka unter Betreuung
von Herr Pof. Stütz.
## Links

[Index](https://github.com/htl-leonding-project/2021-da-chatbot/)

### Besprechungen
[1. Besprechung 22.02.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/22-02-2021)

[2. Besprechung 09.03.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/09-03-2021)

[3. Besprechung 23.03.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/23-03-2021)

[4. Besprechung 06.04.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/06-04-2021)

[5. Besprechung 20.04.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/20-04-2021)

[6. Besprechung 29.04.2021](https://htl-leonding-project.github.io/2021-da-chatbot/mom/29-04-2021)

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

