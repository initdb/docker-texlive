FROM ubuntu:20.04
LABEL maintainer="Benedict Schwind <benedict.schwind@stud.th-rosenheim.de>"
LABEL Description="Image for building tex documents"

WORKDIR /toolchain/texlive
ADD . /toolchain/texlive

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get -y install \
    texlive \
    latexmk \
    texlive-latex-recommended \
    texlive-lang-german \
    texlive-latex-extra \
    texlive-science \
    texlive-font-utils \
    texlive-pictures \
    texlive-bibtex-extra \
    texlive-extra-utils \
    biber \
    python3 \
    python3-pygments \
    python-is-python3 \
    graphviz \
    make && \
    apt-get clean


