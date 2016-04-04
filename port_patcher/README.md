# Generating parser

    grako ./FreeBSDPort.ebnf > FreeBSDPortParser.py

# Invoking parser for manual testing

    python FreeBSDPortParser.py /path/to/actual/Makefile MAKEFILE

where MAKEFILE is the name of the starting rule in the grammar.

# Requirements

## Build
- grako

## Runtime
- semantic_version

# Notes
- When parsing targets it is assumed that they are separated with a  blank line. While this assumption is not strictly correct, in most cases it is true.

