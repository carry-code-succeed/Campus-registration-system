def paixu(djb):       #排序功能       #djb=登记表
    djb.sort(key=lambda djb:djb[0])     #通过lambda函数按第0列排序
#     print(djb)            #测试，打印列表
    return djb           #返回djb登记表
