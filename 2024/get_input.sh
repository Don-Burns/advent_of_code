#!/bin/bash

set -eoux pipefail

source .env

YEAR=2024
DAY=$1
# see link for how to get cookie https://github.com/wimglenn/advent-of-code-wim/issues/1
wget --header="Cookie: ${AOC_COOKIE}" https://adventofcode.com/${YEAR}/day/${DAY}/input --output-document=input/day_${DAY}.txt
