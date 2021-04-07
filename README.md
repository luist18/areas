# mast-tool<!-- omit in toc -->

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/luist18/mast-tool/Deploy%20Docker%20image?logo=github)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/luist188/mast-tool?logo=docker)
[![GitHub license](https://img.shields.io/github/license/luist18/mast-tool?color=blue)](https://github.com/luist18/mast-tool/blob/main/LICENSE)

Microprocessors and Personal Computers ARM subroutine tester tool.

The MAST tool is originally a fork from [João Damas'](https://github.com/cyrilico) [Automatic Observation and (grade) Calculation for (subroutine) Operations tool](https://github.com/cyrilico/aoco-code-correction). It is a tool to automate student's grading in the assignments done during the Microprocessor and Personal Computers course unit.

### Differences with the original tool<!-- omit in toc -->

To ease the communication between the backend server and the tool the output demanded changes. Output `.txt` and `.csv` files are now combined in a more complete `.json` file. Structure of the `.zip` input file is simplified. Unsupported data types such as long and double are now supported. A new input parameter - weight - is introduced.

---

## Table of contents<!-- omit in toc -->

- [1. Installation](#1-installation)
- [2. Running](#2-running)
- [3. Usage](#3-usage)
- [4. File syntax and structure](#4-file-syntax-and-structure)
  - [4.1. Available data types](#41-available-data-types)
    - [4.1.1. Primitive data types](#411-primitive-data-types)
    - [4.1.2. Array data types](#412-array-data-types)
  - [4.2. subroutines.yaml](#42-subroutinesyaml)
  - [4.3. tests.yaml](#43-testsyaml)
  - [4.4. submission.zip](#44-submissionzip)
- [5. Results](#5-results)

## 1. Installation

Using Docker:
```bash
$ docker pull luist188/mast-tool
```

## 2. Running

1. Place the input files inside any directory.
2. Run the image with a shared volume pointing to the input directory: `docker run -v input:destination -it luist188/mast-tool` (you can learn more about `docker run` usage [here](https://docs.docker.com/engine/reference/run/))
3. Run the alias command (assure you are using `/bin/bash`) `mast` or run `python main.py` in the tool's source.

## 3. Usage

```console
$ mast [-h] -sr SR -t T -sm SM [SM ...] [-gfd GFD] [-ffd FFD] [-grf GRF] [-tout TOUT] [-fpre FPRE]

$ mast [args]

Options:
  --help, -h                Show help                                         [boolean]
  -sr <subroutines.yaml>    .yaml file containing subroutine declaration      [required] [string]
  -t <tests.yaml>           .yaml file containing the test cases              [required] [string]
  -sm <submission.zip...>   .zip files containing user submission             [required] [string array]
  -gfd <directory>          path to the directory to store temporary files
    (e.g., compiled binaries)                                                 [default:grading] [string]
  -ffd <directory>          path to the directory to store the grading for
    each submission                                                           [default:feedback] [string]
  -tout <timeout>           float timeout value                               [default:2.0] [float]
  -fpre <precision>         floating point threshold for comparing floating
    points in test cases                                                      [default:1e-6] [float]
```

## 4. File syntax and structure

### 4.1. Available data types

#### 4.1.1. Primitive data types

- `int`
- `long`
- `float`
- `double`
- `char`

#### 4.1.2. Array data types

- `char*/string`
- `array int`
- `array long`
- `array float`
- `array double`
- `array char`

### 4.2. subroutines.yaml

The input file for the subroutine declaration has to follow a specific structure and syntax described as follows:

```yaml
foo: 
  params: 
    - int
    - array char
    - array int
    - array int
  return: 
    - int
    - array int

bar: 
  params: 
    - long
  return: 
    - long
```

The subroutine name has to match the `.s` to test and is case insensitive. Thus, the subroutine `foo` or `bar` is going to check any `.s` file that matches its name case insensitive. All subroutines must contain an array of parameters, `params`, and an array of returns, `return`.

### 4.3. tests.yaml

The input file for the test cases declaration has to follow a specific structure and syntax described as follows:

```yaml
bar:
  - inputs:
    - 6
    outputs: 
    - 36
    weight: 0.5
  - inputs:
    - 5
    outputs: 
    - 25
    weight: 0.5
```

The root declaration of a test case must match the name declared in the `subroutines.yaml` file. Test cases have an array of inputs that has a list of outputs and a test weight. The sum of the test weights must be 1.0.

### 4.4. submission.zip

The submission `zip` file must contain a `.s` file in its root. For example, for the subroutine `foo` and `bar` the `zip` structure should be as follows:

```tree
submission.zip
├── foo.s
└── bar.s
```

## 5. Results

For each submission file a `.json` file is created in the feedback directory with the same name of the `.zip` file. The file contains all information about compilation status and test cases. In addition, a simplified version of the result of all submissions is created in a `result.json`. The content of the files look as follows:

File **submission.json**

```json
[
    {
        "name": "foo",
        "compiled": true,
        "ok": true,
        "passed_count": 2,
        "test_count": 2,
        "score": 1,
        "tests": [
            {
                "weight": 1,
                "run": true,
                "input": [
                    6,
                    ["-", "+", "+", "-", "-", "+"],
                    [1, 2, 3, 0, 1, -25],
                    [13, 2, 8, 4, 5, 25]
                ],
                "output": [
                    "0",
                    ["12", "4", "11", "4", "4", "0"]
                ],
                "passed": true
            }
        ]
    },
    {
        "name": "bar",
        "compiled": true,
        "ok": true,
        "passed_count": 2,
        "test_count": 2,
        "score": 1,
        "tests": [
            {
                "weight": 0.5,
                "run": true,
                "input": [
                    6
                ],
                "output": [
                    "36"
                ],
                "passed": true
            },
            {
                "weight": 0.5,
                "run": true,
                "input": [
                    5
                ],
                "output": [
                    "25"
                ],
                "passed": true
            }
        ]
    }
]
```

File **result.json**

```json
[
    {
        "submission_name": "submission",
        "subroutines": [
            {
                "name": "foo",
                "score": 0
            },
            {
                "name": "bar",
                "score": 0.5
            }
        ]
    },
    {
        "submission_name": "submission2",
        "subroutines": [
            {
                "name": "foo",
                "score": 1
            },
            {
                "name": "bar",
                "score": 1
            }
        ]
    }
]
```

## License<!-- omit in toc -->

[MIT](https://choosealicense.com/licenses/mit/)
