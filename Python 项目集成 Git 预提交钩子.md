# Python 项目集成 Git 预提交钩子

- [Python 项目集成 Git 预提交钩子](#python-项目集成-git-预提交钩子)
  - [概述](#概述)
  - [更多预提交钩子](#更多预提交钩子)
    - [isort](#isort)
    - [black](#black)
    - [codespell](#codespell)
    - [pyright](#pyright)

## 概述

> Git 钩子脚本对于在提交代码审查前识别简单的问题非常有用。我们在每次提交时运行钩子，自动指出代码中的问题，如缺少分号、尾部空白和调试语句。通过在代码审查前指出这些问题，这使得代码审查员能够专注于一个变化的架构，而不是在琐碎的风格问题上浪费时间。

安装：

```bash
pip install pre-commit
```

添加预提交配置

执行命令生成配置文件模板：

```bash
pre-commit sample-config >> .pre-commit-config.yaml
```

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
```

- `trailing-whitespace`: 修剪尾部的空白。
- `end-of-file-fixer`: 确保文件以换行方式结束，而且只以换行方式结束。
- `check-yaml`: 试图加载所有 yaml 文件以验证语法。
- `check-added-large-files`: 防止巨型文件被提交。

安装 GitHook 脚本：

```bash
pre-commit install
```

运行检查

```bash
pre-commit run --all-files
```

> 更多开箱即用的预提交脚本请查阅 [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

## 更多预提交钩子

### isort

> 对 `import` 代码进行排序和格式化。

```yaml
repos:
-   repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
    -   id: isort
        name: isort (python)
```

或者也可以使用本地钩子：

```yaml
repos:
-   repo: local
    hooks:
    -   id: isort
        name: isort
        entry: isort
        language: python
        require_serial: true
        types: [ python ]
        additional_dependencies: [ 'isort==5.10.1' ]
```

### black

> Black 是不折不扣的 Python 代码格式化器。

```yaml
repos:
-   repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
    -   id: black
        language_version: python3
```

或者也可以使用本地钩子：

```yaml
repos:
-   repo: local
    hooks:
    -   id: black
        name: black
        entry: black
        language: python
        language_version: python3
        require_serial: true
        types: [ python ]
        additional_dependencies: [ 'black==22.3.0' ]
```

❗ 当 `black` 与 `isort` 一起使用时，由于 `black` 也会对 `import` 代码进行格式化，但与 `isort` 的默认配置不同，这会导致更改冲突，为了解决这个问题，我们需要更改 `isort` 的默认配置，新建 `pyproject.toml` 配置文件，并添加一下代码：

```toml
[tool.isort]
profile = "black"
```

### codespell

> 修复文本文件中常见的拼写错误。它主要是为检查源代码中的拼写错误而设计的，但它也可以用于其他文件。

```yaml
repos:
-   repo: https://github.com/codespell-project/codespell
    rev: v2.1.0
    hooks:
    -   id: codespell
        args:
        -   --ignore-words-list=vas --skip="*.js"
```

或者也可以使用本地钩子：

```yaml
repos:
-   repo: local
    hooks:
    -   id: codespell
        name: codespell
        entry: codespell
        args: [ '--ignore-words-list=vas', '--skip="*.js"' ]
        language: python
        require_serial: true
        types: [ python ]
        additional_dependencies: [ 'codespell==2.1.0' ]
```

### pyright

> Python 的静态类型检查器。

```yaml
repos:
-   repo: local
    hooks:
    -   id: pyright
        name: pyright
        entry: pyright --venv-path .
        language: node
        pass_filenames: false
        types: [ python ]
        additional_dependencies: [ 'pyright@1.1.255' ]
```

新建 `pyproject.toml` 配置文件，并添加一下代码：

```toml
[tool.pyright]
include = ["your dir"]
```

通过在 Python 脚本文件的某个地方（一般在文件代码顶部）添加注释 `# pyright: strict` 来启用所有类型检查选项。
