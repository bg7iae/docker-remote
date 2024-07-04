import paramiko
import asyncio
import os
import json

# 从配置文件中加载 SSH 连接参数
def load_config(config_file='config.json'):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

async def stream_container_stats(ssh):
    try:
        # 打开一个新的通道
        channel = ssh.get_transport().open_session()
        channel.get_pty()
        channel.exec_command('docker stats --format "table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}"')

        while True:
            if channel.recv_ready():
                output = channel.recv(1024).decode()
                if output:
                    # 清除终端并打印输出
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(output.strip())
            await asyncio.sleep(1)  # 避免过于频繁地读取输出，稍作延迟

    except Exception as e:
        print(f"Error: {e}")

async def monitor_containers():
    # 从配置文件中加载配置
    config = load_config()

    hostname = config.get('hostname')
    port = config.get('port', 22)
    username = config.get('username')
    password = config.get('password')
    key_filename = config.get('key_filename')

    # 创建 SSH 客户端
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 根据配置文件中的信息选择认证方式
        if key_filename:
            if os.path.isfile(key_filename):
                ssh.connect(hostname, port, username, key_filename=key_filename)
            else:
                raise ValueError(f"密钥文件 {key_filename} 不存在")
        elif password:
            ssh.connect(hostname, port, username, password=password)
        else:
            raise ValueError("必须提供密码或密钥文件以进行身份验证")

        await stream_container_stats(ssh)

    finally:
        # 关闭 SSH 连接
        ssh.close()

async def main():
    await monitor_containers()

# 运行异步主函数
asyncio.run(main())