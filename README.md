<a name="readme-top"></a>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [📝 License](#license)

# 📖 Simple Calculator <a name="about-project"></a>

> A command-line calculator that maintains a running total as users repeatedly enter an arithmetic operator and a number. It also supports undoing the most recent successful calculation.

This project is a beginner-friendly exercise in input handling, loops, state management, validation, and stack-based undo in Python.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

- **Language:** Python 3
- **Dependencies:** None; the project must not import libraries.

### Key Features <a name="key-features"></a>

- Apply addition, subtraction, multiplication, and division to a running total.
- Accept floating-point numbers.
- Undo the most recent successful calculation.
- Handle invalid operators, invalid numeric input, and division by zero without crashing.
- Perform operations with explicit logic; `eval()` is not used.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Live Demo <a name="live-demo"></a>

There is no live demo for this command-line project at this time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps. The commands below assume the calculator implementation will be saved as `calculator.py`; update the filename if your project uses a different one.

### Prerequisites

You need:

- Python 3 installed on your computer.
- Git, if you are cloning the repository.

### Setup

Clone the repository and move into the project directory. Replace `<repository-url>` with the URL of your copy:

```sh
git clone <repository-url>
cd <repository-directory>
```

### Install

No package installation is required. The project uses Python built-ins only and should not import libraries.

### Usage

Once the implementation is saved as `calculator.py`, start it with:

```sh
python3 calculator.py
```

Enter an operator and a number, separated by whitespace. For example:

```text
> + 5
Result: 5
> * 2
Result: 10
> undo
Result: 5
```

The calculator should continue accepting commands until its chosen exit command is entered. If an operation is invalid or a division by zero is attempted, it should display an informative message and keep the existing total unchanged.

### Run tests

Automated test files and a test command have not been added yet. Once tests are available, run the command documented by the project. At minimum, manually check the following cases:

| Case | Expected behavior |
|---|---|
| `+ 5`, then `* 2` | The total becomes 5, then 10 |
| `undo` after those operations | The total returns to 5 |
| `undo` with no previous operation | Show a “Nothing to undo” message |
| Divide by zero | Show an error; keep the total unchanged |
| Invalid operator or non-numeric input | Show an error; do not crash or change the total |
| Decimal input, such as `+ 0.5` | Accept and calculate using a floating-point number |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👥 Authors <a name="authors"></a>

👤 **Temitope Ogunleye**

- GitHub: [@togunleye](https://github.com/togunleye)
- LinkedIn: [ogunleye](https://www.linkedin.com/in/ogunleye)

> Replace the example author details with your own before publishing the repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔭 Future Features <a name="future-features"></a>

- [ ] Add automated tests for valid operations, undo, and invalid input.
- [ ] Add a clear, documented command for exiting the calculator.
- [ ] Improve the display of the current total after each command.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome. If you would like to contribute, open an issue to discuss a change or submit a pull request with a clear description of what it improves.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⭐️ Show your support <a name="support"></a>

If you find this learning project useful, consider giving the repository a star and sharing feedback or suggestions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🙏 Acknowledgements <a name="acknowledgements"></a>

- [Microverse README Template](https://github.com/microverseinc/readme-template) for the README structure and section conventions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 License <a name="license"></a>

No license has been selected for this project yet. Add a `LICENSE` file and update this section before distributing the project. Until then, do not assume the code is licensed for reuse.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
