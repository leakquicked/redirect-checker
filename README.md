# Redirect Checker

Review a manually copied redirect chain for scheme changes and unexpected hosts.

## Requirements
Python 3.10+, standard library only.

## Usage
`python redirect_checker.py sample.txt`

The program reads a local text file only. It performs no network requests, scanning, or enrichment. Treat output as a summary, not a security verdict.

## Tests
`python -m unittest discover -s tests -v`
