# ListFilter-and-OCamlDemos

This repository contains a Python program designed to process lists of integers, filtering out elements based on specific criteria, alongside interesting OCaml code samples demonstrating concise and functional programming techniques.

## Features

**Filtered List in Python:**
- Accepts a list of integers and performs filtering based on the following rules:
  - Emits an error if the list's length is not a multiple of 10.
  - Returns a new list with items at positions that are multiples of 2 or 3 removed.

**OCaml Samples:**
- `fib_first_10.ml`: Calculates the first 10 Fibonacci numbers.
- `levenshtein_distance.ml`: Computes the Levenshtein distance between two strings, showcasing algorithm implementation in OCaml.

## Spotlight: The Fibonacci Sequence

The `fib_first_10.ml` sample pays tribute to the ancient Fibonacci sequence's enduring relevance in mathematics and computer science. Introduced by Leonardo of Pisa, known as Fibonacci, in his 1202 book "Liber Abaci," this sequence starts with 0 and 1, with each subsequent number being the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, ...).

Beyond its mathematical significance, the Fibonacci sequence finds applications in computer algorithms, financial models, and natural phenomena, such as leaf arrangement and tree branching. Its simplicity unveils profound patterns in the natural and computational realms, demonstrating how foundational mathematical concepts can inform programming.

Implemented in OCaml, this sample showcases the elegance of functional programming for expressing mathematical ideas concisely. The Fibonacci sequence's recursive nature illustrates recursion, a fundamental computer science concept. By exploring this OCaml implementation, users witness how ancient numerical sequences continue to shape modern computational solutions, highlighting the synergy between mathematics and programming.

## Spotlight: The Levenshtein Distance

The `levenshtein_distance.ml` sample explores the history of spell check technology and the influence of mathematical concepts. Vladimir Levenshtein introduced the Levenshtein distance in 1965, quantifying the minimum single-character edits needed to transform one word into another.

Levenshtein's work preceded widespread personal computing. In the 1960s, the digital landscape was nascent, and spell checkers were in their infancy. Levenshtein's rigorous algorithm laid the foundation for modern spell checkers.

Levenshtein's approach differed from early spell-checking, like Gorin's 1-distance checker in the 70s. Gorin's method flagged words with a "distance" of one, while Levenshtein's distance offered precise similarity measurement.

It's possible early developers, like Gorin, weren't aware of Levenshtein's work, given limited information exchange.

Levenshtein's algorithm was inefficient due to recursion. Wagner and Fischer's dynamic programming idea, which alchemized it into a matrix/grid-like solution, improved it to make efficient spell checkers possible, shaping today's text analysis tools.

The OCaml implementation pays homage to these roots, showcasing how pioneering concepts remain relevant, inspiring future innovations.

## Getting Started

### Prerequisites

- Python 3.8 or later for running the Python scripts.
- OCaml environment for compiling and running OCaml programs. OPAM is recommended for managing OCaml installations.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/<your-username>/ListFilter-and-OCamlDemos.git
cd ListFilter-and-OCamlDemos
```

## Running the Programs

### Running the Python Program

To run the Python program for filtered list processing, use the following command:

```bash
python Filtered_List.py
```

### Running OCaml Programs

To compile and run an OCaml program, follow these steps:

1. Compile the OCaml program using the ocamlc compiler:
```bash
ocamlc -o fib_first_10 fib_first_10.ml
```

2. Execute the OCaml program:
```bash
./fib_first_10
```

3. Repeat the same process for the levenshtein_distance.ml program:
```bash
ocamlc -o levenshtein_distance levenshtein_distance.ml

./levenshtein_distance
```


## Running Tests

To run the tests for the Python list filtering program, use the following command:

```bash
python Filtered_List_unittesting.py
```

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## License
Distributed under the Hemlock License. Contact for more information.

## Credits

This project was inspired by a coding challenge from the Spring 2024 Mentorship Program, organized by The Linux Foundation. The challenge, titled "Sailing Downstream," aimed to streamline the flow of current from the RISC-V Sail specification to downstream implementations, eliminating manual steps, and enhancing accessibility.

**Background:**
The current flows from RISC-V Sail specification to downstream implementations have manual steps that are time-consuming and prone to errors. This challenge recognized the need to bridge the gap for those unfamiliar with Sail and OCaml, making it more accessible for automated downstream implementations, including emulators, simulators, compilers, assemblers, disassemblers, instruction stream tools, and documentation.

This coding challenge highlighted the importance of streamlining and automating complex processes in the world of software development and served as an inspiration for this project.

*The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage/). Linux is a registered trademark of Linus Torvalds.*



