<h1 align="center">
    BrowserForge-local
</h1>

<p align="center">
    <a href="README.md">English</a>
</p>

<h4 align="center">
    🎭 智能浏览器请求头与指纹生成器（离线可用）
</h4>

---

## 项目简介

BrowserForge-local 是一个浏览器请求头与指纹生成器，按照真实世界中不同浏览器、操作系统与设备的分布生成合理的指纹与 HTTP 头。

本项目基于 Python 复刻了 [Apify 的 fingerprint-suite](https://github.com/apify/fingerprint-suite)，并 fork 自 [`daijro/browserforge`](https://github.com/daijro/browserforge)。

### 本项目相较于源项目的改动

- 运行时不依赖网络：数据样本随包内置，优先本地读取。
- 取消所有运行时的下载与更新检查：样本随版本发布更新。
- 新增构建期数据更新脚本：发布前可一键从上游同步最新样本并打包。
- 遵循 Apache-2.0 许可：在 `NOTICE` 中注明上游致谢与来源。

## 特性

- 使用贝叶斯生成网络模拟真实流量分布
- 运行速度快（0.1-0.2 毫秒）
- 简洁易用，支持浏览器/系统/设备/语言/HTTP 版本定制
- 类型安全
- 离线可用：数据随包分发，不在运行时下载

## 安装

```
pip install browserforge-local[all]
```

## 构建期数据更新（可选）

若希望在发布前打包最新数据样本：

```
python3 -m pip install apify_fingerprint_datapoints
python3 scripts/update_datapoints.py
poetry build && poetry publish
```

## 使用示例

### 生成请求头

```py
from browserforge.headers import HeaderGenerator

headers = HeaderGenerator()
print(headers.generate())
```

### 结合 requests 使用

```py
import requests
from browserforge.headers import HeaderGenerator

session = requests.Session()
session.headers = HeaderGenerator().generate()
```

### 生成浏览器指纹

```py
from browserforge.fingerprints import FingerprintGenerator

fp = FingerprintGenerator().generate()
print(fp.headers['User-Agent'])
```

## 许可证

本项目以 Apache-2.0 许可发布。数据样本来源于 Apify 的 fingerprint-suite，详见根目录 `NOTICE` 文件。