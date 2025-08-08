# Editoris Melicorum (EMEL)

Editors of Melodies - GSI's music typesetting toolkit

Part of the FAVI System: https://github.com/guild-st-isidore-TO/fabrica-virtualis

---

![Editoris Melicorum mascot image](./static/edi_melicorum_pic.png "Editoris Melicorum mascot image")

Editoris Melicorum is a digital music typesetting toolkit for music ministries in Catholic
parishes. The toolkit helps build musical arrangements around traditional hymns in Gregorian notation.
As well as laying them out into documents, both for the congregation and the choir/musicians.

Check out an [example document here](./static/marian-hymns-0.1.pdf)

## USAGE

1. Be in the root directory of this repo
1. Run `python3 src/editorismelicorum/editor_melicus.py`

### Setup

#### Requirements

**gabctk** -- GABC conversion toolkit

https://github.com/jperon/gabctk/blob/master/README-en.md

**LilyPond** -- Digital music typesetting

https://lilypond.org/download.html

#### Suggestions

**Frescobaldi** -- Lilypond viewer and editor

https://github.com/frescobaldi/frescobaldi/wiki

## SERVER USAGE

### Operating Systems

EMEL has been tested on:

MacOS Ventura 13.2.1

### Installation/Setup

Open this repo's directory in the terminal and run:

```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Running/Deploying the Server

Building docker image

```
docker build -t editoris-melicorum .
```

Listing docker images

```
docker images
```

Run docker image

```
docker run -d -p 5050:5050 editoris-melicorum
```

Listing docker image/container status

```
docker ps -a
```

## CONFIGURATION

These configs can be found in `data/`:

- `configs.json` -- Configurations for the editorismelicorum system
- `input-configs.json` -- Configurations for documents being written and edited by the system

### gabctk path

`configs.json` looks like:

```
{
    "version": "0.0.2",
    "paths": {
        "gabctkDirectory": "../gabctk",
        "dataTemplatesDirectory": "data/templates",
        "outputDirectoryLyData": "build/ly-data",
        "outputDirectoryLy": "build/ly",
        "outputDirectoryMidi": "build/midi",
        "outputDirectoryPdf": "build/pdf",
        "outputDirectoryXml": "build/xml"
    },
    "opModes": ...
}
```

The `gabctkDirectory` value needs to point to the `gabctk` local repo (and location of `gabctk.py`). But relative to the the root of this local repo. If the repos are siblings (same directory), `gabctkDirectory` should be `../gabctk`

Output paths can be changed as well, if necessary

### documents

`input-configs.json` looks like:

```
{
    "documents": [
        {
            "name": "Editoris Melicorum Example",
            "id": "ed_meli_example",
            "author": "rjsalvadorr",
            "mainDocument": "edi_melicorum_example.ly",
            "gabcFiles": [
                "examples/01-ave-maria.gabc",
                "examples/02-crux_fidelis.gabc",
                "examples/03-sanctus_xi.gabc",
                "examples/04-dominus_dixit.gabc",
                "examples/05-kyrie_xvi.gabc",
                "examples/06-pange_lingua.gabc",
                "examples/07-ascendit_deus.gabc",
                "examples/08-nos_autem.gabc",
                "examples/11-regina-caeli.gabc"
            ]
        },
        {
            "name": "Another doc example",
            "id": "another_doc_example",
            "author": "otherperson",
            "mainDocument": "otherdoc/another_doc_example.ly",
            "gabcFiles": [
                "otherdoc/01-kyrie.gabc",
                "otherdoc/02-gloria.gabc",
                ...
            ]
        },
        ...
    ]
}
```

This is where users can specify details about the documents they're making. And the GABC scores that will be included in them. Please note that :

- The path value of `mainDocument` is relative to the `document/` directory. 
- The file paths in `gabcFiles` are relative to the `data/` directory.

Files in those directories can be organized into sub-dirs and accounted for in their paths.

## WORKFLOWS

### Composing, arranging

Uses `gabctk`

1. Use the arranging workflow and provide:
    - source hymns (`.gabc` files from GregoBase, etc)
    - base style/template (`.ly` LilyPond files)
1. Software creates a PDF with blank arrangement sheets for each hymn, with space to write out accompaniments on guitar and on keyboard (2 extra staves below melody)

### Publishing

Uses `gabctk` and `pandoc`

1. Typeset accompaniments into `.ly` files
1. Use the publishing workflow and provide:
    - source hymns (`.gabc` files from GregoBase, etc)
    - base style/template (`.ly` LilyPond files)
    - corresponding arrangements for those hymns (`.ly` LilyPond files)
1. Software creates two PDFS:
    - congregation hymnal -- The hymns, with only the melody line (Gregorian notation)
    - choir hymnal -- The hymns, with melody line, guitar line, and general accompaniment line (all in Standard notation)

## IMPLEMENTATION

The Editoris toolkit works mainly through a set of Python scripts that do a few things like:

1. read GABC files
1. read user inputs
1. assemble documents
1. etc. 

### Philosophy

The module can be thought of as a publishing house (**Editoris Melicorum**) run by several people:

1. **Editor**, _(in Chief)_  
Sets up jobs, sends deliverables
1. **Lector**, _the Reader_  
Reads source documents, prepares them for further arrangement
1. **Scriptor**, _the Writer (Engraver)_  
Combines source documents and prepared arrangements, and engraves new copies
1. **Scholasticus**, _the Scholar_  
Knowledge resource for the rest of the team

The module has been structured to reflect these personas and their division of responsibilities.

### Data Flow

![Editoris Melicorum data flow (Jul 2025)](./static/design/data-flow-v2.svg "Editoris Melicorum data flow (Jul 2025)")

## CONTRIBUTING

Want to contribute to the _Editoris_ project? Shoot an email to `salvador.workshop@gmail.com`

## Notes

- The ``(`)`` symbol in GABC input code causes errors in `gabctk`, and should be removed