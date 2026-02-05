<div align="center">
  
# [Proxy-List-Generator.](https://github.com/BrenoFariasdaSilva/Proxy-List-Generator) <img src="https://github.com/BrenoFariasdaSilva/Proxy-List-Generator/blob/main/.assets/Icons/proxy-server.png"  width="3%" height="3%">

</div>

<div align="center">
  
---

A Python tool that automatically scrapes and generates up-to-date proxy lists from multiple free proxy sources, saving them into organized text files for easy integration into your projects.
  
---

</div>

<div align="center">

![GitHub Code Size in Bytes](https://img.shields.io/github/languages/code-size/BrenoFariasdaSilva/Proxy-List-Generator)
![GitHub Commits](https://img.shields.io/github/commit-activity/t/BrenoFariasDaSilva/Proxy-List-Generator/main)
![GitHub Last Commit](https://img.shields.io/github/last-commit/BrenoFariasdaSilva/Proxy-List-Generator)
![GitHub Forks](https://img.shields.io/github/forks/BrenoFariasDaSilva/Proxy-List-Generator)
![GitHub Language Count](https://img.shields.io/github/languages/count/BrenoFariasDaSilva/Proxy-List-Generator)
![GitHub License](https://img.shields.io/github/license/BrenoFariasdaSilva/Proxy-List-Generator)
![GitHub Stars](https://img.shields.io/github/stars/BrenoFariasdaSilva/Proxy-List-Generator)
![GitHub Contributors](https://img.shields.io/github/contributors/BrenoFariasdaSilva/Proxy-List-Generator)
![GitHub Created At](https://img.shields.io/github/created-at/BrenoFariasdaSilva/Proxy-List-Generator)
![wakatime](https://wakatime.com/badge/github/BrenoFariasdaSilva/Proxy-List-Generator.svg)

</div>

<div align="center">
  
![RepoBeats Statistics](https://repobeats.axiom.co/api/embed/dbd824ba0971a5ecf52c4d83b0f8d4915709dd6e.svg "Repobeats analytics image")

</div>

## Table of Contents
- [Proxy-List-Generator. ](#proxy-list-generator-)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Clone the repository](#clone-the-repository)
  - [Installation:](#installation)
    - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [Results - Optional](#results---optional)
  - [Contributing](#contributing)
  - [Collaborators](#collaborators)
  - [License](#license)
    - [Apache License 2.0](#apache-license-20)

## Introduction

This project is a **Proxy List Generator** that automatically scrapes free proxy servers from multiple online sources and saves them into organized text files. The tool is designed for developers and security researchers who need fresh proxy lists for testing, web scraping, or privacy applications.

All output is logged to both the terminal and a log file, with colored output for better readability. The script also tracks execution time and can optionally play a sound notification when complete (on macOS and Linux).

## Requirements

This project requires the following:
- Python 3.6 or higher
- Internet connection for scraping proxy sources
- Required Python packages (installed via `make dependencies`)
    The packages include:
    - `beautifulsoup4` (4.14.3)
    - `colorama` (0.4.6)
    - `requests` (2.32.5)

## Setup

### Clone the repository

1. Clone the repository with the following command:

   ```bash
   git clone https://github.com/BrenoFariasDaSilva/Proxy-List-Generator.git
   cd Proxy-List-Generator
   ```

## Installation:

* Programing Language:

  * Manually:
      ```bash
      # Programing Language:
      sudo apt install program-language -y
      ```

  * Using Makefile:
      ```bash
      make install
      ```

  * Using ShellScript:
      ```bash
      chmod +x install.sh
      sudo ./install.sh
      ```  

### Dependencies

1. Install the project dependencies with the following command:

   ```bash
   make dependencies
   ```

## Usage

In order to run the project, run the following command:

```bash
make run
```

## Results - Optional

Discuss the results obtained in the project.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. If you have suggestions for improving the code, your insights will be highly welcome.
In order to contribute to this project, please follow the guidelines below or read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute to this project, as it contains information about the commit standards and the entire pull request process.
Please follow these guidelines to make your contributions smooth and effective:

1. **Set Up Your Environment**: Ensure you've followed the setup instructions in the [Setup](#setup) section to prepare your development environment.

2. **Make Your Changes**:
   - **Create a Branch**: `git checkout -b feature/YourFeatureName`
   - **Implement Your Changes**: Make sure to test your changes thoroughly.
   - **Commit Your Changes**: Use clear commit messages, for example:
     - For new features: `git commit -m "FEAT: Add some AmazingFeature"`
     - For bug fixes: `git commit -m "FIX: Resolve Issue #123"`
     - For documentation: `git commit -m "DOCS: Update README with new instructions"`
     - For refactorings: `git commit -m "REFACTOR: Enhance component for better aspect"`
     - For snapshots: `git commit -m "SNAPSHOT: Temporary commit to save the current state for later reference"`
   - See more about crafting commit messages in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

3. **Submit Your Contribution**:
   - **Push Your Changes**: `git push origin feature/YourFeatureName`
   - **Open a Pull Request (PR)**: Navigate to the repository on GitHub and open a PR with a detailed description of your changes.

4. **Stay Engaged**: Respond to any feedback from the project maintainers and make necessary adjustments to your PR.

5. **Celebrate**: Once your PR is merged, celebrate your contribution to the project!

## Collaborators

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://github.com/BrenoFariasdaSilva.png" width="100px;" alt="My Profile Picture"/><br>
        <sub>
          <b>Breno Farias da Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## License

### Apache License 2.0

This project is licensed under the [Apache License 2.0](LICENSE). This license permits use, modification, distribution, and sublicense of the code for both private and commercial purposes, provided that the original copyright notice and a disclaimer of warranty are included in all copies or substantial portions of the software. It also requires a clear attribution back to the original author(s) of the repository. For more details, see the [LICENSE](LICENSE) file in this repository.
