# HackZurich 2022 - KiNG
[![made-with-python](https://img.shields.io/badge/made%20with-Python%20%3E3-1f425f.svg?color=blueviolet&style=plastic&logo=python)](https://www.python.org/)
[![ide](https://img.shields.io/badge/IDE-VSCode-yellowgreen?style=plastic&logo=visual-studio-code)](https://code.visualstudio.com/)
![code-size](https://img.shields.io/github/languages/code-size/black-fractal/HackZurich2022_KiNG?style=plastic)
![total-lines](https://img.shields.io/tokei/lines/github/black-fractal/HackZurich2022_KiNG?style=plastic&color=green)
![commit-activity](https://img.shields.io/github/commit-activity/m/black-fractal/HackZurich2022_KiNG?color=brightgreen&style=plastic)
![last-commit](https://img.shields.io/github/last-commit/black-fractal/HackZurich2022_KiNG?color=9cf&style=plastic)
![downloads](https://img.shields.io/github/downloads/black-fractal/HackZurich2022_KiNG/total?style=plastic)
![license](https://img.shields.io/github/license/black-fractal/HackZurich2022_KiNG?style=plastic)

**A `python` script that allows you to have all formations of HackZurich2022_KiNG puzzle!**

## Brief Summary
![Logo!](https://github.com/black-fractal/n-queens/blob/main/img/n-queens-logo.png)
The n-queens puzzle is the problem of placing n chess queens on an n×n chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. Solutions exist for all natural numbers n with the exception of `n=2` and `n=3`.

<p align="left">
  <img width="300" src="https://upload.wikimedia.org/wikipedia/commons/1/1f/Eight-queens-animation.gif"></br>
  <i>fig.1: A sample iterations for finding a correct formation of 8 queens.</i>
</p>

## Counting Solutions
The following tables give the number of solutions for placing n queens on an n × n board, both fundamental (sequence [A002562](https://oeis.org/A002562) in the [OEIS](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences)) and all (sequence [A000170](https://oeis.org/A000170) in the [OEIS](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences)).

| `n` | `fundamental` | `all` |
| :-: | :-----------: | :---: |
| 1 | 1 | 1 |
| 2 | 0 | 0 |
| 3 | 0 | 0 |
| 4 | 1 | 2 |
| 5 | 2 | 10 |
| 6 | 1 | 4 |
| 7 | 6 | 40 |
| 8 | 12 | 92 |
| 9 | 46 | 352 |
| 10 | 92 | 724 |
| 11 | 341 | 2,680 |
| 12 | 1,787 | 14,200 |
| 13 | 9,233 | 73,712 |
| 14 | 45,752 | 365,596 |
| 15 | 285,053 | 2,279,184 |
| 16 | 1,846,955 | 14,772,512 |
| 17 | 11,977,939 | 95,815,104 |
| 18 | 83,263,591 | 666,090,624 |
| 19 | 621,012,754 | 4,968,057,848 |
| 20 | 4,878,666,808 | 39,029,188,884 |
| 21 | 39,333,324,973 | 314,666,222,712 |
| 22 | 336,376,244,042 | 2,691,008,701,644 |
| 23 | 3,029,242,658,210 | 24,233,937,684,440 |
| 24 | 28,439,272,956,934 | 227,514,171,973,736 |
| 25 | 275,986,683,743,434 | 2,207,893,435,808,352 |
| 26 | 2,789,712,466,510,289 | 22,317,699,616,364,044 |
| 27 | 29,363,495,934,315,694 | 234,907,967,154,122,528 |

The six queens puzzle has fewer solutions than the five queens puzzle.
There is no known formula for the exact number of solutions, or even for its asymptotic behaviour. The [27×27](https://github.com/preusser/q27) board is the highest-order board that has been completely enumerated.

## Installation Steps
1. Clone 'HackZurich2022_KiNG' from git:\
`git clone https://github.com/black-fractal/HackZurich2022_KiNG.git`

2. Change the directory:\
`cd HackZurich2022_KiNG`

3. Install the requirements:\
`pip3 install -r requirements.txt`

4. Enjoy the program:+1:

## Update to latest version:
Use following command to update to latest version:\
`git pull`

## Usage
- To run with the ASCII visualizer:\
`cd src`\
`python3 manage.py runserver`\
![output-of-n-queens](https://github.com/black-fractal/n-queens/blob/main/img/output-of-n-queens.gif)\
*Sample output*

## License
This tools is licensed under the GPL-3.0 License. take a look at the [LICENSE](https://github.com/black-fractal/wikipedia-philosophy-game/blob/main/LICENSE) for information about it.

![watch](https://img.shields.io/github/watchers/black-fractal/n-queens?label=watch&style=social)
[![twitter](https://img.shields.io/twitter/follow/V4HlD?color=yellow&label=twitter%20follow&style=social)](https://twitter.com/V4HlD)

