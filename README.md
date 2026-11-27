# OpenFic 插件模板

用于开发 OpenFic 插件的 GitHub 模板，内含一个可安装的 Python 示例插件。

## 如何使用

1. 在 GitHub 仓库页面点击 **Use this template → Create a new repository**。
2. 将新仓库克隆到本地，在 `src/` 目录下编写插件代码。
3. 准备测试时，安装 `uv`，然后在插件仓库根目录运行以下命令。CLI 由 OpenFic 的后端项目提供。

   ```sh
   git clone https://github.com/syrizelink/OpenFic.git ../OpenFic
   uv run --project ../OpenFic/backend --frozen --no-dev openfic plugin pack . --output dist/plugin.zip
   ```

4. 在 OpenFic 的插件管理中上传 `dist/plugin.zip` 并启用插件。

> [!TIP]
> 在 GitHub 发布插件时，请为仓库添加 `openfic-plugin` 话题（Topic），方便其他人发现。
