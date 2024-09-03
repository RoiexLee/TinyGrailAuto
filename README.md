# TinyGrailAuto

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

一个用于自动完成 Tiny Grail 签到任务的 Github 工作流，使用 GitHub Actions 和 Python

- [README CHINESE](./README.md)

## 目录

- [安装](#安装)
- [使用](#使用)
- [徽章](#徽章)
- [维护者](#维护者)
- [证书](#证书)

## 安装

### 本地安装

你可以通过下述步骤进行本地安装

```shell
$ git clone https://github.com/RoiexLee/TinyGrailAuto.git
$ cd TinyGrailAuto
$ pip install -r requirements.txt
```

之后，你可以按照 [本地使用](#本地使用) 运行脚本

### GitHub Actions 安装

你同样也可以使用 Github Actions 安装本项目

查看 [GitHub Actions 使用](#github-actions-使用) 部分获得更多信息

## 使用

### 获得 cookies

### 本地使用

```shell
$ python checkin.py --cookies=<cookies>
```

其中 `--cookies` 为必须参数，支持多个 cookie，用 `&` 分隔

### GitHub Actions 使用

1. Fork 这个仓库
2. 在仓库设置中添加 secrets，移动到 Fork 后的仓库，依次点击 `Settings > Secrets and variables > Actions > New Repository secret`
    - `COOKIES`: 必须，`Secret` 填写 `COOKIES` 的值
3. Star Fork 之后的仓库以启动 GitHub Actions

## 徽章

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## 维护者

[@RoiexLee](https://roiexlee.github.io)

## 证书

[GPL-3.0](./LICENSE) © [RoiexLee](https://roiexlee.github.io) 