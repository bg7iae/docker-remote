
# Remote Docker Monitor

Remote Docker Monitor 是一个通过 SSH 连接到远程服务器，并实时监控 Docker 容器运行状态的应用。

## 项目结构

```plaintext
.
├── config
├── remotedocker.py
├── sample_config.json
├── sample-onlykey_config.json
└── sample-pwkey_config.json
```

- `config/`: 用于存放实际的配置文件。
- `remotedocker.py`: 主应用脚本。
- `sample_config.json`: 样例配置文件（使用密码进行认证）。
- `sample-onlykey_config.json`: 样例配置文件（仅使用密钥文件进行认证）。
- `sample-pwkey_config.json`: 样例配置文件（使用密码和密钥文件进行认证）。

## 依赖安装

在运行此项目之前，请确保已安装必要的 Python 库。您可以使用以下命令安装依赖：

```bash
pip install paramiko asyncio
```

## 配置文件说明

配置文件使用 JSON 格式存储 SSH 连接参数。根据不同的认证方式，配置文件可以有以下几种形式：

### 使用密码进行认证

`config/config.json`

```json
{
  "hostname": "192.168.1.100",
  "port": 22,
  "username": "your_username",
  "password": "your_password",
  "key_filename": null
}
```

### 使用密钥文件进行认证

`config/config.json`

```json
{
  "hostname": "192.168.1.100",
  "port": 22,
  "username": "your_username",
  "password": null,
  "key_filename": "/path/to/your/private/key"
}
```

### 使用密码和密钥文件进行认证

`config/config.json`

```json
{
  "hostname": "192.168.1.100",
  "port": 22,
  "username": "your_username",
  "password": "your_password",
  "key_filename": "/path/to/your/private/key"
}
```

## 运行应用

请确保配置文件位于 `config` 目录下，并且命名为 `config.json`。然后使用以下命令运行应用：

```bash
python remotedocker.py
```

## 样例配置文件

项目中提供了三个样例配置文件，分别展示了不同的认证方式。您可以根据需要复制并修改其中一个样例文件为实际的配置文件：

- `sample_config.json`: 使用密码进行认证的样例配置文件。
- `sample-onlykey_config.json`: 仅使用密钥文件进行认证的样例配置文件。
- `sample-pwkey_config.json`: 使用密码和密钥文件进行认证的样例配置文件。

将其中一个样例文件复制到 `config` 目录，并重命名为 `config.json` 后，即可使用对应的认证方式运行应用。

## 注意事项

- 确保 `paramiko` 和 `asyncio` 库已经安装。
- 确保 SSH 连接参数正确。
- 如果使用密钥文件，请确保密钥文件路径正确且文件存在。

## 许可证

本项目遵循 MIT 许可证。详情请参阅 LICENSE 文件。
