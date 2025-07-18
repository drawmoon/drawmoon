# TypeScript 项目集成 Git 预提交钩子

> [commitlint](https://commitlint.js.org/) 可以帮助我们在提交代码至 Git 仓库时，校验提交信息是否严格按照[约定式提交](https://www.conventionalcommits.org/zh-hans)规范进行代码提交。

安装 commitlint：

```sh
npm install --save-dev @commitlint/config-conventional @commitlint/cli
```

配置 commitlint：

```sh
echo "module.exports = { extends: ['@commitlint/config-conventional'] };" > commitlint.config.js
```

使用 [husky](https://typicode.github.io/husky/) 在提交时检查提交信息是否符合规范

安装 husky：

```sh
npm install --save-dev husky
```

添加钩子：

```sh
cat <<EEE > .husky/commit-msg
#!/bin/sh
. "\$(dirname "\$0")/_/husky.sh"

npx --no -- commitlint --edit "\${1}"
EEE
```

在 `package.json` 添加脚本：

```json
{
  "scripts": {
    "prepare": "husky install"
  }
}
```

执行脚本激活钩子：

```sh
npm run prepare
```
