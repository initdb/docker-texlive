# docker-texlive
If you want to **easily** use **texlive** on different pcs and operrating systems and
If you don't want to install different tex distros on multiple platforms, then this is the container for you and me. 

This repo provides a Dockerfile and container for local and/or CI/CD texlive usage.

# Personal Highlights
tex packages I found to be very usefull
- **acronym**: as the name implies
- **minted**: for code previews

# How to get it
please have a look at the **GitHub Packages** and **Releases** to the right -> 
# How to build
If you want to build the container yourself:
```sh
docker build -t texlive-lw:latest -f Dockerfile .
```

# Visual Studio Code Setup
I personally use vscode as my tex editor. See below for a list of recommended plugins.
## Requirements
- docker
- LaTeX Workshop
## Setup
1. pull or build the container
2. go to file -> preferences -> settings and search for the following key.
enable it. 
```json
"latex-workshop.docker.enabled": true
```
3. now add the container name. it can be either your local or the image from the GitHub package registry
```json
"latex-workshop.docker.image.latex": "ghcr.io/initdb/docker-texlive:main"
```
4. add the option```"--shell-escape"``` so can properly work. 
```json
"latex-workshop.latex.tools": [
    

        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        },
```

## Plugin Recommendations
- LaTeX Utilities

# Examples

TODO


