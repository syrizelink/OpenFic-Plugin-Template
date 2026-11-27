# OpenFic 示例插件模板

这个模板适用于 OpenFic 0.14.0 的实验性插件系统（插件 API v1）。示例在「扩展」侧栏提供原生面板。点击「标记试用完成」会保存状态，重新打开面板后仍可看到结果。点击「重置试用状态」可以恢复初始状态。

## 从模板开始

1. 在 GitHub 上点击 **Use this template → Create a new repository**，选择 **Private**，然后克隆新仓库。
2. 修改 `plugin.json` 中的 `id`、`name`、`description` 和视图标题。插件 ID 应以小写字母开头，仅使用小写字母、数字和连字符。发布新版时递增 `version`，以便已安装的插件可以更新。
3. 在 `main.py` 中修改 `render()` 和 `action()`。`register()` 中注册的命令名应与清单中的 `render` 和 `action` 字段一致。

`ui` 用于挂载面板和通知宿主刷新，`storage` 用于保存插件自己的状态。新增运行时文件时，把它们加入 `plugin.dev.json` 的 `package.include`。如果文件需要由宿主作为公开资源提供，也要在 `plugin.json` 的 `resources` 中声明对应路径。

## 检查、打包和安装

使用带有 `openfic plugin` 子命令的 OpenFic CLI，在模板仓库根目录运行：

```sh
openfic plugin check .
openfic plugin pack . --output dist/openfic-example.zip
```

检查器会提示动态视图需要运行时验证。私有仓库请使用 ZIP 安装。打开 OpenFic 的插件管理，选择「安装插件包」→「从文件安装」，上传 `dist/openfic-example.zip` 并启用插件。从侧栏「扩展」打开「示例插件」，试用保存和重置。

插件包结构和扩展接口见 [OpenFic 插件 SDK 文档](https://github.com/syrizelink/OpenFic/blob/main/packages/plugin-sdk/README.md)。
