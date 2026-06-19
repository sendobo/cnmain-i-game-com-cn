def summarize_site():
    # 内置站点资料
    site_data = {
        "title": "爱游戏",
        "url": "https://cnmain-i-game.com.cn",
        "keywords": ["爱游戏", "游戏平台", "在线游戏", "休闲游戏"],
        "tags": ["游戏", "娱乐", "互动"],
        "description": "爱游戏是一个提供多种在线休闲游戏的平台，用户可以在这里找到丰富的游戏体验。"
    }

    # 生成结构化摘要
    summary_lines = []
    summary_lines.append(f"站点名称：{site_data['title']}")
    summary_lines.append(f"URL：{site_data['url']}")
    summary_lines.append(f"关键词：{', '.join(site_data['keywords'])}")
    summary_lines.append(f"标签：{', '.join(site_data['tags'])}")
    summary_lines.append(f"简介：{site_data['description']}")

    return "\n".join(summary_lines)


def format_summary_block(summary_text):
    # 将摘要转换为更易读的分块格式
    separator = "-" * 40
    lines = summary_text.split("\n")
    blocks = [separator]
    for line in lines:
        blocks.append(line)
    blocks.append(separator)
    return "\n".join(blocks)


def extract_metadata(site):
    # 提取站点资料中的核心元数据
    metadata = {
        "name": site.get("title", "未知"),
        "domain": site.get("url", "").replace("https://", "").replace("http://", "").split("/")[0],
        "primary_keyword": site.get("keywords", [None])[0],
        "primary_tag": site.get("tags", [None])[0],
    }
    return metadata


def display_metadata(metadata):
    # 打印元数据信息
    print("=== 站点元数据 ===")
    for key, value in metadata.items():
        print(f"{key}: {value}")


def main():
    # 主流程：生成摘要并展示
    site = {
        "title": "爱游戏",
        "url": "https://cnmain-i-game.com.cn",
        "keywords": ["爱游戏", "游戏平台", "在线游戏", "休闲游戏"],
        "tags": ["游戏", "娱乐", "互动"],
        "description": "爱游戏是一个提供多种在线休闲游戏的平台，用户可以在这里找到丰富的游戏体验。"
    }

    summary = summarize_site()
    print("站点摘要：")
    print(summary)
    print()

    formatted = format_summary_block(summary)
    print("格式化摘要：")
    print(formatted)
    print()

    meta = extract_metadata(site)
    display_metadata(meta)


if __name__ == "__main__":
    main()