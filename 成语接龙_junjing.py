# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:25:25 2018
Updated by jesseZhang on Mon Nov 12 13:39:00 2018
Updated by jesseZhang on Mon Dec 1 15:14:00 2018
@author: pwy5150 & jesseZhang
"""
import os
import pandas as pd
import random
os.chdir('./')

class chinesePuzzleGame:
    def __init__(self):
        """
        执行构建函数的初始化操作
        :param :
        :return :
        """
        self.initialData()

    def initialData(self):
        """
        初始化成语数据
        :param :
        :return :
        """
        print("游戏开始--->")
        self.inputVar = ""
        # 构建函数初始化getChengYu, 获得所有成语, pandas格式
        self.chengYuPandas = self.read()
        # 给getChengYuList里面的字符串从最长到最短sort一下, 并获取数组中输出最长的和最短的字符串
        self.chengYuList = self.chengYuPandas.values.tolist()
        self.chengYuList.sort(key=lambda i: len(i), reverse=True)
        self.minChengyuLen, self.maxChengyuLen = len(self.chengYuList[-1]), len(self.chengYuList[0])
        # 从self.chengYuList里面随机取一个成语, 作为电脑给出的第一个成语
        self.randomWord = random.choice(self.chengYuList)
        print('电脑给你的第一个成语是{{{}}}:'.format(self.randomWord))


    def read(self):
        """
        读取excel文件, 并返回需要的成语字段
        :param :
        :return: allChineseWords 所有的成语
        """
        data = pd.read_excel('chengyu.xlsx',encoding='gbk')
        data['成语'] = data['成语'].str.replace('，', '')
        allChineseWords = data['成语']
        return allChineseWords

    def wordCheck(self, inputVar):
        """
        判断格式, 其中包括字段长短以及输入的字符串是不是纯文字
        :param inputVar: 待检查的字符串
        :param minChengyuLen: 数组中输出最短的字符串长度
        :param maxChengyuLen: 数组中输出最短的字符串长度
        :return: 1为验证到非中文, 2为验证长度过短, 3为验证长度过长, 返回inputVar为验证成功
        """
        for singleStr in str(inputVar):
            if not('\u4e00' <= singleStr <= '\u9fa5'):
                return 1
        if len(str(inputVar)) < self.minChengyuLen:
            return 2
        elif len(str(inputVar)) > self.maxChengyuLen:
            return 3
        else:
            return str(inputVar)

    def returnNewWord(self, inputVar):
        """
        通过最后一个字来获取新的成语
        :param inputVar: 待检查的字符串
        :return: None为验证失败,  returnNewWord为验证成功, 获得了新的词语
        """
        # lastWord是玩家输入文字的最后一个字
        lastWord = inputVar[-1]
        # 判断玩家输入的成语的最后一次是否可以在成语库里面找到, 找到则标记为True, 找不到则标记为False
        startWordsList = self.chengYuPandas.str.startswith(lastWord, na=False)
        # 将True的成语返回
        startWordsList = self.chengYuPandas[startWordsList]
        # 将pandas Series格式数据变成数组格式
        startWordsList = startWordsList.values.tolist()
        # 若语料库中没有以该词作为开头的词汇, 则返回None
        if not startWordsList:
            return None
        # 在返回的成语数组里面随机选择一个成语并返回
        returnNewWord = random.choice(startWordsList)
        return returnNewWord

    def run(self):
        """
        开始运行游戏
        :param:
        :return:
        """
        while self.inputVar != "quit":
            print("(输入'help'可求助于电脑or输入'quit'退出游戏!)")
            self.inputVar = input("你的输入:")
            # 退出判断
            if self.inputVar.strip() == "quit":
                break
            # 空输入判断
            if self.inputVar.strip() == "":
                print('你没有输入成语呢!')
                continue
            # 求助电脑判断
            if self.inputVar == "help":
                print("It is support time!")
                self.randomWord = self.returnNewWord(self.randomWord)
                print('电脑给你的成语是{{{}}}:'.format(self.randomWord))
                if self.randomWord is None:
                    print('电脑没词了, 厉害了我的小朋友!')
                    break
                continue
            # 验证字数长度是否符合语料库内成语的字数长度
            # 验证输入的成语的格式是否符合规则(是否为纯文字)
            wordCheck = self.wordCheck(self.inputVar)
            if wordCheck == 1:
                print('你输入的东西不是纯文字, 请再次输入!')
                continue
            elif wordCheck == 2:
                print('你输入的东西的字段长度小于成语库里面的最短成语长度, 请再次输入!')
                continue
            elif wordCheck == 3:
                print('你输入的东西的字段长度大于成语库里面的最长成语长度, 请再次输入!')
                continue
            else:
                # 成为的词头词尾文字判断
                if self.randomWord[-1] != self.inputVar[0]:
                    print("你输入的词头不符合给出成语的词尾, 请再次输入!")
                    continue
                # 词汇是否在语料库中存在
                if wordCheck in self.chengYuList:
                    self.randomWord = self.returnNewWord(wordCheck)
                    if self.randomWord is None:
                        print('电脑没词了, 厉害了我的小朋友!')
                        break
                    else:
                        print('电脑给你的成语是{{{}}}:'.format(self.randomWord))
                else:
                    print('你输入的成语没有在语料库中找到, 请再次输入:')
                    continue
        print("游戏结束.")

if __name__ == '__main__':
    startGame = chinesePuzzleGame()
    startGame.run()