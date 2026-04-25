# Multi-Utility CLI Tool (Python)

## Overview

A command-line tool built with Python that provides multiple utilities
including hashing, Base64 encoding/decoding, HMAC generation, and Morse
code encoding/decoding.

The tool uses a structured CLI interface and enhanced terminal output
for better readability.

------------------------------------------------------------------------

## Features

-   Hashing:
    -   SHA256
    -   SHA512
    -   MD5
    -   SHA1
-   Base64:
    -   Encode
    -   Decode
-   HMAC generation with custom key and algorithm
-   Morse Code:
    -   English encoding/decoding
    -   Arabic encoding/decoding
-   Arabic text normalization support
-   Styled terminal output using rich

------------------------------------------------------------------------

## Technologies Used

Python 3 argparse hashlib base64 hmac rich re unicodedata

------------------------------------------------------------------------

## Installation

    pip install rich

------------------------------------------------------------------------

## Usage

    python tool.py <command> [options]

------------------------------------------------------------------------

## Commands

### Hashing

    python tool.py hash <type> <text>

Supported types: - sha256 - sha512 - md5 - sha1

------------------------------------------------------------------------

### Base64

    python tool.py base64 -e <text>
    python tool.py base64 -d <text>

------------------------------------------------------------------------

### HMAC

    python tool.py hmac -k <key> -t <text> -ty <type>

------------------------------------------------------------------------

### Morse Code

#### English

    python tool.py morse -e -en <text>
    python tool.py morse -e -de <morse>

#### Arabic

    python tool.py morse -a -en <text>
    python tool.py morse -a -de <morse>

------------------------------------------------------------------------

## How It Works

### Hashing

Uses hashlib to generate hashes based on selected algorithm.

### Base64

Encodes or decodes text using base64 module.

### HMAC

Generates secure keyed hashes using HMAC with selected algorithm.

### Morse Code

-   Uses predefined dictionaries for English and Arabic
-   Supports encoding and decoding
-   Arabic text is normalized before encoding

------------------------------------------------------------------------

## Arabic Normalization

-   Removes diacritics
-   Normalizes letters (أ → ا, ة → ه, etc.)
-   Converts Arabic numbers to standard digits

------------------------------------------------------------------------

## Output

All results are displayed using rich panels with colored formatting.

------------------------------------------------------------------------

## Requirements

    Python 3.x

------------------------------------------------------------------------

## Security Notes

-   MD5 and SHA1 are not recommended for secure applications
-   Use SHA256 or SHA512 for better security
-   Keep HMAC keys secure

------------------------------------------------------------------------

## License

MIT License
