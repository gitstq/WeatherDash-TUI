<!-- Language Switcher -->
<p align="center">
  <a href="#简体中文">简体中文</a> •
  <a href="#繁體中文">繁體中文</a> •
  <a href="#english">English</a>
</p>

---

<a name="简体中文"></a>
## 🎉 项目介绍

**WeatherDash-TUI** 是一款精美的终端天气仪表盘，专为开发者和终端爱好者设计。它使用 Rust 编写，具有超快的启动速度和极低的资源占用。

### ✨ 核心特性

- 🌤️ **实时天气数据** - 使用 Open-Meteo API，免费且无需 API Key
- 🎨 **ASCII 艺术图标** - 精美的终端天气图标，支持切换模式
- 📍 **多城市支持** - 收藏喜爱的城市，快速切换查看
- 💾 **离线缓存** - 自动缓存天气数据，支持离线模式
- ⚡ **超快响应** - Rust 编写，毫秒级启动
- 🎯 **零配置** - 开箱即用，无需复杂设置
- 📊 **详细指标** - 温度、湿度、风速、气压等完整数据
- 🖥️ **精美 TUI** - 基于 Ratatui 的现代化终端界面

### 🚀 快速开始

#### 环境要求

- Rust 1.75+ (用于编译)
- 终端支持 UTF-8

#### 安装

```bash
# 从源码编译
git clone https://github.com/yourusername/weatherdash-tui.git
cd weatherdash-tui
cargo build --release

# 安装到系统
cargo install --path .
```

#### 运行

```bash
# 启动天气仪表盘
weatherdash-tui

# 指定城市
weatherdash-tui -c "Shanghai"

# 离线模式
weatherdash-tui --offline
```

### 📖 详细使用指南

#### CLI 命令

```bash
# 添加城市到收藏
weatherdash-tui --add "Beijing"

# 删除收藏城市
weatherdash-tui --remove "Beijing"

# 列出所有收藏
weatherdash-tui -l

# 设置刷新间隔（秒）
weatherdash-tui --refresh 60
```

#### 键盘快捷键

| 按键 | 功能 |
|------|------|
| `r` | 刷新天气数据 |
| `n` | 下一个收藏城市 |
| `p` | 上一个收藏城市 |
| `a` | 切换 ASCII 艺术模式 |
| `f` | 切换天气预报 |
| `h` | 显示帮助 |
| `q` | 退出程序 |

### 💡 设计思路

WeatherDash-TUI 的设计理念是**简洁、高效、美观**：

1. **零配置优先** - 使用免费的 Open-Meteo API，无需注册和配置 API Key
2. **离线友好** - 自动缓存数据，网络不佳时也能查看
3. **终端原生** - 完全在终端中运行，适合 SSH 远程使用
4. **资源节约** - Rust 编写，内存占用 < 10MB

### 📦 打包与部署

```bash
# 编译发布版本
cargo build --release

# 跨平台编译（Linux）
cargo build --release --target x86_64-unknown-linux-gnu

# 跨平台编译（macOS）
cargo build --release --target x86_64-apple-darwin

# 跨平台编译（Windows）
cargo build --release --target x86_64-pc-windows-gnu
```

### 🤝 贡献指南

欢迎提交 PR 和 Issue！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 📄 开源协议

本项目采用 MIT 协议开源 - 详见 [LICENSE](LICENSE) 文件

---

<a name="繁體中文"></a>
## 🎉 專案介紹

**WeatherDash-TUI** 是一款精美的終端天氣儀表板，專為開發者和終端愛好者設計。它使用 Rust 編寫，具有超快的啟動速度和極低的資源佔用。

### ✨ 核心特性

- 🌤️ **即時天氣資料** - 使用 Open-Meteo API，免費且無需 API Key
- 🎨 **ASCII 藝術圖示** - 精美的終端天氣圖示，支援切換模式
- 📍 **多城市支援** - 收藏喜愛的城市，快速切換查看
- 💾 **離線快取** - 自動快取天氣資料，支援離線模式
- ⚡ **超快回應** - Rust 編寫，毫秒級啟動
- 🎯 **零設定** - 開箱即用，無需複雜設定
- 📊 **詳細指標** - 溫度、濕度、風速、氣壓等完整資料
- 🖥️ **精美 TUI** - 基於 Ratatui 的現代化終端介面

### 🚀 快速開始

#### 環境要求

- Rust 1.75+ (用於編譯)
- 終端支援 UTF-8

#### 安裝

```bash
# 從原始碼編譯
git clone https://github.com/yourusername/weatherdash-tui.git
cd weatherdash-tui
cargo build --release

# 安裝到系統
cargo install --path .
```

#### 執行

```bash
# 啟動天氣儀表板
weatherdash-tui

# 指定城市
weatherdash-tui -c "Taipei"

# 離線模式
weatherdash-tui --offline
```

### 📖 詳細使用指南

#### CLI 命令

```bash
# 新增城市到收藏
weatherdash-tui --add "Taipei"

# 刪除收藏城市
weatherdash-tui --remove "Taipei"

# 列出所有收藏
weatherdash-tui -l

# 設定刷新間隔（秒）
weatherdash-tui --refresh 60
```

#### 鍵盤快速鍵

| 按鍵 | 功能 |
|------|------|
| `r` | 刷新天氣資料 |
| `n` | 下一個收藏城市 |
| `p` | 上一個收藏城市 |
| `a` | 切換 ASCII 藝術模式 |
| `f` | 切換天氣預報 |
| `h` | 顯示說明 |
| `q` | 離開程式 |

### 💡 設計思路

WeatherDash-TUI 的設計理念是**簡潔、高效、美觀**：

1. **零設定優先** - 使用免費的 Open-Meteo API，無需註冊和設定 API Key
2. **離線友善** - 自動快取資料，網路不佳時也能查看
3. **終端原生** - 完全在終端中執行，適合 SSH 遠端使用
4. **資源節約** - Rust 編寫，記憶體佔用 < 10MB

### 📦 打包與部署

```bash
# 編譯發布版本
cargo build --release

# 跨平台編譯（Linux）
cargo build --release --target x86_64-unknown-linux-gnu

# 跨平台編譯（macOS）
cargo build --release --target x86_64-apple-darwin

# 跨平台編譯（Windows）
cargo build --release --target x86_64-pc-windows-gnu
```

### 🤝 貢獻指南

歡迎提交 PR 和 Issue！

1. Fork 本儲存庫
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 建立 Pull Request

### 📄 開源協議

本專案採用 MIT 協議開源 - 詳見 [LICENSE](LICENSE) 檔案

---

<a name="english"></a>
## 🎉 Introduction

**WeatherDash-TUI** is a beautiful terminal weather dashboard designed for developers and terminal enthusiasts. Written in Rust, it features ultra-fast startup and minimal resource usage.

### ✨ Key Features

- 🌤️ **Real-time Weather Data** - Uses Open-Meteo API, free and no API key required
- 🎨 **ASCII Art Icons** - Beautiful terminal weather icons with switchable modes
- 📍 **Multi-city Support** - Save favorite cities and switch between them quickly
- 💾 **Offline Caching** - Automatically caches weather data, supports offline mode
- ⚡ **Ultra-fast Response** - Written in Rust, millisecond-level startup
- 🎯 **Zero Configuration** - Works out of the box, no complex setup needed
- 📊 **Detailed Metrics** - Temperature, humidity, wind speed, pressure, and more
- 🖥️ **Beautiful TUI** - Modern terminal interface based on Ratatui

### 🚀 Quick Start

#### Requirements

- Rust 1.75+ (for compilation)
- Terminal with UTF-8 support

#### Installation

```bash
# Build from source
git clone https://github.com/yourusername/weatherdash-tui.git
cd weatherdash-tui
cargo build --release

# Install system-wide
cargo install --path .
```

#### Usage

```bash
# Start weather dashboard
weatherdash-tui

# Specify city
weatherdash-tui -c "New York"

# Offline mode
weatherdash-tui --offline
```

### 📖 Detailed Usage Guide

#### CLI Commands

```bash
# Add city to favorites
weatherdash-tui --add "London"

# Remove city from favorites
weatherdash-tui --remove "London"

# List all favorites
weatherdash-tui -l

# Set refresh interval (seconds)
weatherdash-tui --refresh 60
```

#### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `r` | Refresh weather data |
| `n` | Next favorite city |
| `p` | Previous favorite city |
| `a` | Toggle ASCII art mode |
| `f` | Toggle weather forecast |
| `h` | Show help |
| `q` | Quit program |

### 💡 Design Philosophy

WeatherDash-TUI is designed with **simplicity, efficiency, and beauty** in mind:

1. **Zero-config First** - Uses free Open-Meteo API, no registration or API key setup needed
2. **Offline Friendly** - Automatic data caching, works even with poor network
3. **Terminal Native** - Runs entirely in terminal, perfect for SSH remote usage
4. **Resource Efficient** - Written in Rust, memory usage < 10MB

### 📦 Build & Deploy

```bash
# Build release version
cargo build --release

# Cross-compile for Linux
cargo build --release --target x86_64-unknown-linux-gnu

# Cross-compile for macOS
cargo build --release --target x86_64-apple-darwin

# Cross-compile for Windows
cargo build --release --target x86_64-pc-windows-gnu
```

### 🤝 Contributing

PRs and Issues are welcome!

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
