import os
import pandas as pd
import random as rd

# 读取数据
emoji = pd.read_csv(os.path.join(os.path.dirname(__file__), "emojidata.csv"), encoding="gbk")
text = pd.read_csv(os.path.join(os.path.dirname(__file__), "textdata.csv"), encoding="gbk")

# 去掉空值
emoji_cleaned = emoji.dropna()
text_cleaned = text.dropna()


def split_and_insert(tdata, eli):
    # 生成随机拆分点
    split_points = sorted(rd.sample(range(1, len(tdata)), rd.randint(1, len(tdata) - 1)))
    split_points.insert(0, 0)  # 在开头插入 0，作为第一个拆分点
    split_points.append(len(tdata))  # 在末尾插入字符串长度，作为最后一个拆分点

    # 拆分字符串并加入特定字符
    parts = []
    for i in range(len(split_points) - 1):
        part = tdata[split_points[i]:split_points[i + 1]]
        parts.append(part)
        if i != len(split_points) - 2:  # 最后一个拆分点后不插入特定字符
            if eli:  # 如果 eli 列表不为空
                char = eli.pop(0)  # 弹出列表的第一个元素
                parts.append(char)  # 添加到拆分的部分之间

    return ''.join(parts)
def convert_to_int_or_keep_original(style):
    try:
        # 尝试将字符串转换为整数
        integer_value = int(style)
        return integer_value
    except ValueError:
        # 如果转换失败，返回原始字符串
        return style

class creatLuckText:
    @staticmethod
    def luck(style):
        style=convert_to_int_or_keep_original(style)#字符串转换
        rt = rd.randint(0, len(text_cleaned) - 1)
        tdata = text_cleaned.iloc[rt].item()  # 获取字符串值
        eli = []

        if style in range(100):
            for _ in range(style):  # 个表情内容生成
                re = rd.randint(0, len(emoji_cleaned) - 1)
                edata = emoji_cleaned.iloc[re].item()  # 获取表情值
                eli.append(f"<emoji:{edata}>")

            result = split_and_insert(tdata, eli)
            return result
        if style == '':
            return tdata
        if style == None:
            return tdata
        if type(style) == str:
            return tdata
#
# if __name__ == "__main__": #测试接口
#      text = creatLuckText.luck()
#      print(text)