# Advent of Code 2023

Solving the [Advent of Code 2023](https://adventofcode.com/2023) in Python.

## AOC Downloader

The `aoc_downloader.py` can be used to create a folder and download the input for a specific day.

### Usage

The [session cookie](https://github.com/wimglenn/advent-of-code-wim/issues/1) needs to be stored in a file `config.json` in this format:

```
{
    "session_cookie": "your-session-cookie-here"
}
```

Additionally, the path inside `py_template.txt` should be changed to fit the path to the advent-of-code directory.

Running `python path/to/aoc_downloader.py` creates a directory with the input file inside.

Passing the optional parameter `--day` or `--year` forces the download for a specific date, otherwise it defaults to the current date (The month is always assumed to be December).
The optional parameter `--py` adds a templated python file to the created directory.

For example, running

```
python path/to/aoc_downloader.py --day 17 --year 2021 --py
```

creates the folder and files as follows:

```
advent-of-code/
|
|-- day17/
|     |
|     |-- input.txt
|     |-- day17.py
|
|-- aoc_downloader.py

```