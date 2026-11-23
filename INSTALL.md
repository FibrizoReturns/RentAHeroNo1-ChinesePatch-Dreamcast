# 安装与校验

## 0. 从哪拿

- 发布视频（B 站）：<https://www.bilibili.com/video/BV1cwyHztEvh/>
- 成品盘（百度网盘）：<https://pan.baidu.com/s/1uVhPdS8dgKTvV8wQxIM8EQ?pwd=qdpa> 提取码 `qdpa`

## 1. 文件清单

成品盘解压后是这 4 个文件，**必须放在同一层目录**（不要拆开、不要改名）：

```
RentAHeroV3.gdi     光盘描述文件（88 字节，纯文本）
track01.bin         音轨 1（原盘原样，13,968,528 字节）
track02.raw         音轨 2（原盘原样，1,735,776 字节）
track03.bin         数据轨（已替换字库与全部文本，1,185,760,800 字节）
```

## 2. 用 Flycast 运行（推荐）

1. 下载 Flycast（Windows 版，建议用较新的 stable 或 nightly）
2. 打开 `RentAHeroV3.gdi`（不是 track03.bin）
3. 首次进入若提示「存档不存在」，属 VMU 未初始化 —— 进游戏新建存档即可
4. BIOS 建议用日版（Region = 0），可避免部分区域判定问题

成品包里若带 `启动汉化版.bat`，双击即可（内部是调用 Flycast 并载入 gdi，
路径不对时用记事本改一下即可）。

## 3. 校验（强烈建议）

```
track03.bin
  MD5   27180546005E35BC30B9A2C6B9BC11DD
  大小  1185760800 字节
```

PowerShell：

```powershell
Get-FileHash -LiteralPath '.\track03.bin' -Algorithm MD5
```

哈希不一致 = 下载或解压损坏，请重新获取，不要拿去刻盘或喂给 GDEMU。

## 4. 常见问题

| 现象 | 处理 |
|---|---|
| 开场花屏 / 模拟器崩溃 | 换视频后端（Vulkan ↔ OpenGL），并注明模拟器版本与后端反馈 |
| 全黑但能听到声音 | 同样先换视频后端，再检查 BIOS 区域设置 |
| 提示存档不存在 | VMU 未初始化，进游戏新建即可 |
| 文本显示为方块/乱码 | 说明用了错误的 track03.bin（原版或别的版本），重新核对 MD5 |

## 5. 关于刻盘 / 实体机

本版只提供 **GDI**（模拟器与 ODE，如 GDEMU / MODE 使用）。
没有提供 CDI，也没有针对 CD-R 刻盘做验证 —— 刻盘需要自行转换并承担风险。
