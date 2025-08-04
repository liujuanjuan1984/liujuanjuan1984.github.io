# Life Is Real - 个人博客网站

这是一个基于 [Pelican](https://getpelican.com/) 静态网站生成器构建的个人博客网站，部署在 GitHub Pages 上。

## 项目概述

- **网站名称**: Life Is Real.
- **作者**: Helen
- **技术栈**: Pelican (Python 静态网站生成器) + Clean Blog 主题
- **部署平台**: GitHub Pages
- **语言**: 简体中文

## 项目结构

```
liujuanjuan1984.github.io/
├── content/                    # 博客文章内容目录
│   └── *.md                   # Markdown 格式的博客文章
├── output/                     # 生成的静态网站文件
├── pelican-themes/            # Pelican 主题目录
│   └── clean-blog/           # 使用的 Clean Blog 主题
├── pelicanconf.py            # Pelican 开发环境配置文件
├── publishconf.py            # Pelican 生产环境配置文件
├── tasks.py                  # Invoke 任务脚本
├── Makefile                  # Make 构建脚本
└── README.md                 # 项目说明文档
```

## 使用方法

### 开发模式

1. **启动本地开发服务器**:
   ```bash
   invoke serve
   ```
   或使用 Makefile:
   ```bash
   make serve
   ```

2. **实时预览模式** (推荐):
   ```bash
   invoke livereload
   ```
   此模式会在文件修改时自动重新生成网站并刷新浏览器。

### 构建网站

1. **生成静态文件**:
   ```bash
   invoke build
   ```
   或
   ```bash
   make html
   ```

2. **清理生成的文件**:
   ```bash
   invoke clean
   ```
   或
   ```bash
   make clean
   ```

### 发布到 GitHub Pages

```bash
invoke gh_pages
```
或
```bash
make github
```

## 编写新文章

1. 在 `content/` 目录下创建新的 `.md` 文件
2. 使用以下格式编写文章头部信息:

```markdown
Title: 文章标题
Date: 2024-01-01 10:00
Category: 分类名称
Tags: 标签1, 标签2
Slug: 文章别名
Author: Helen
Summary: 文章摘要

文章内容...
```

3. 保存文件后，如果使用 `invoke livereload`，网站会自动更新

## 配置说明

### pelicanconf.py (开发环境配置)
- 网站基本信息设置
- 主题配置
- 文章摘要长度控制
- 静态文件路径配置

### publishconf.py (生产环境配置)
- 生产环境特定设置
- RSS Feed 配置
- 输出目录清理设置

## 常用命令速查

| 命令 | 说明 |
|------|------|
| `invoke serve` | 启动本地开发服务器 |
| `invoke livereload` | 启动实时预览模式 |
| `invoke build` | 构建静态网站 |
| `invoke clean` | 清理生成的文件 |
| `invoke gh_pages` | 发布到 GitHub Pages |
| `make serve` | 使用 Makefile 启动服务器 |
| `make html` | 使用 Makefile 构建网站 |
| `make github` | 使用 Makefile 发布到 GitHub Pages |

