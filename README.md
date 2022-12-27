<h1 align="center">Data Manipulation Convention</h1>

Trip Teknologi's Data Manipulation Codebase Convention.

Getting Started
---

Initialization :

`curl -sL https://raw.githubusercontent.com/tripteki/data/main/bin/project | sh -s -- <project>`

Configuration :

    .
    ├── <project>/
    ├──── config/
    ├────── app.py
    ├────── logging.py
    ├────── database.py
    ├────── mail.py
    ├────── thirdparty.py
    ├──── database/__init__.py
    ├──── src/Extraction/Api/__init__.py
    └──── src/Extraction/Web/__init__.py

Installation :

Move your current working directory to the outer of project. <br />
Copy `<project>/pyproject.toml` to current working directory. <br />
Then install it with this command :

```
$ python3 -m pip install .
```

If you prefered to use async sqlite :

```
$ python3 -m pip install aiosqlite
```

If you prefered to use sync mysql :

```
$ python3 -m pip install pymysql
```

If you prefered to use async mysql :

```
$ python3 -m pip install asyncmy
```

If you prefered to use sync postgresql :

```
$ python3 -m pip install pygresql
```

If you prefered to use async postgresql :

```
$ python3 -m pip install asyncpg
```

If you prefered to use sync sqlserver :

```
$ python3 -m pip install pymssql
```

Usage
---

`python3 -m <project>`

Option
---

- `--help` : Usage.
- `migration:up` : Run migration up.
- `migration:down` : Run migration down.
- `extract:api` : Run the api extraction.
- `extract:web` : Run the web extraction.
- `schedule:extract` : Run the schedule of extraction.
- `repl:extract` : Run the repl of extraction.

Author
---

- Trip Teknologi ([@tripteki](https://linkedin.com/company/tripteki))
- Hasby Maulana ([@hsbmaulana](https://linkedin.com/in/hsbmaulana))
