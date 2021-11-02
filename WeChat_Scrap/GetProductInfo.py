#coding:utf-8
import requests
import json,csv

verify_ssl=False
domain=r'https://api.marykayintouch.com.cn/'
cate_path=r'customerorderingcoreappservices/v4/categories/top-menu'
product_path=r'customerorderingcoreappservices/v4/categories/get'

access_token='649160e31bd847d94d11b2aad0ccbd29964a5978'
filePath=r'D:/meilinkai.csv'
testvalue=[{'name': '臻时粹颜精华油', 'retail_price': 1088.0, 'suggest_retail_price': 1580.0, 'sale_count': 14282}, {'name': '幻时佳双天后组 含：幻时佳高阶紧塑精华露 + 幻时佳高阶维C精华露（尊享装）', 'retail_price': 1088.0, 'suggest_retail_price': 1818.0, 'sale_count': 20708}, {'name': '经典护肤组 含：保湿爽肤水+滋养润肤乳液', 'retail_price': 188.0, 'suggest_retail_price': 280.0, 'sale_count': 100694}, {'name': '元気保湿组', 'retail_price': 188.0, 'suggest_retail_price': 336.0, 'sale_count': 87350}, {'name': '减加膜法组（含：高水份面膜霜，幻时5X柔润焕活晚安冻膜）', 'retail_price': 288.0, 'suggest_retail_price': 410.0, 'sale_count': 70473}, {'name': '青春明眸组（含：幻时抗皱精华素，舒活眼膜啫哩）', 'retail_price': 388.0, 'suggest_retail_price': 568.0, 'sale_count': 87412}, {'name': '抗初老王牌组', 'retail_price': 388.0, 'suggest_retail_price': 596.0, 'sale_count': 61722}, {'name': '年轻三角组 含：幻时佳多效修护眼霜 + 幻时佳活颜紧致精华霜', 'retail_price': 798.0, 'suggest_retail_price': 1500.0, 'sale_count': 33367}, {'name': '幻时佳高阶紧塑精华露买大送小（含：幻时佳高阶紧塑精华露，幻时佳高阶紧塑精华露旅行装10ml）', 'retail_price': 688.0, 'suggest_retail_price': 860.0, 'sale_count': 20708}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15044}, {'name': '怡日健DHA藻油叶黄素酯软糖凝胶糖果 2瓶', 'retail_price': 398.0, 'suggest_retail_price': 460.0, 'sale_count': 10761}, {'name': '调色润妍妆前乳 ', 'retail_price': 158.0, 'suggest_retail_price': 223.0, 'sale_count': 407}, {'name': '粉扬遮瑕膏 ', 'retail_price': 138.0, 'suggest_retail_price': 210.0, 'sale_count': 1702}, {'name': 'B族维生素片/辅酶Q10维生素E胶囊 任意2盒298元', 'retail_price': 298.0, 'suggest_retail_price': 396.0, 'sale_count': 31956}, {'name': '肠道顺畅组 含：怡日健益生菌固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1080.0, 'sale_count': 125243}, {'name': '减油解腻组 含：怡日健水溶性膳食纤维固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1350.0, 'sale_count': 46852}, {'name': '体质强健组 含：怡日健酵母β-葡聚糖固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1350.0, 'sale_count': 101285}, {'name': '强健助力组 含：怡日健固多肽固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1350.0, 'sale_count': 54126}, {'name': '人气弹弹组 含：怡日健胶原蛋白肽固体饮料（30条装）2盒', 'retail_price': 999.0, 'suggest_retail_price': 1456.0, 'sale_count': 68868}, {'name': '健康充电组 （新包装） 含：怡日健番茄红素2盒', 'retail_price': 588.0, 'suggest_retail_price': 666.0, 'sale_count': 16962}, {'name': '抗氧明星组 含：怡日健粉妍片2盒', 'retail_price': 799.0, 'suggest_retail_price': 1020.0, 'sale_count': 90456}, {'name': '肠道顺畅组 含：怡日健益生菌固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1080.0, 'sale_count': 125243}, {'name': '减油解腻组 含：怡日健水溶性膳食纤维固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1350.0, 'sale_count': 46852}, {'name': '体质强健组 含：怡日健酵母β-葡聚糖固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1350.0, 'sale_count': 101285}, {'name': '强健助力组 含：怡日健固多肽固体饮料3盒', 'retail_price': 666.0, 'suggest_retail_price': 1350.0, 'sale_count': 54126}, {'name': '健康充电组 （新包装） 含：怡日健番茄红素2盒', 'retail_price': 588.0, 'suggest_retail_price': 666.0, 'sale_count': 16962}, {'name': '抗氧明星组 含：怡日健粉妍片2盒', 'retail_price': 799.0, 'suggest_retail_price': 1020.0, 'sale_count': 90456}, {'name': '人气弹弹组 含：怡日健胶原蛋白肽固体饮料（30条装）2盒', 'retail_price': 999.0, 'suggest_retail_price': 1456.0, 'sale_count': 68868}, {'name': '多维抗皱安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 6228}, {'name': '极光透亮安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 11136}, {'name': '细肤焕颜安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 2774}, {'name': '三重水光安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 13664}, {'name': '怡日健辅酶Q10维生素E胶囊', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 31956}, {'name': '幻时佳高阶紧塑精华露买大送小（含：幻时佳高阶紧塑精华露，幻时佳高阶紧塑精华露旅行装10ml）', 'retail_price': 688.0, 'suggest_retail_price': 860.0, 'sale_count': 20708}, {'name': '玩色丝慕唇膏钻石限量版', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 522}, {'name': '立体闪耀高光粉饼钻石限量版', 'retail_price': 108.0, 'suggest_retail_price': 135.0, 'sale_count': 2057}, {'name': '轻盈纯色腮红钻石限量版粉色', 'retail_price': 108.0, 'suggest_retail_price': 135.0, 'sale_count': 783}, {'name': '怡日健DHA藻油叶黄素酯软糖凝胶糖果', 'retail_price': 230.0, 'suggest_retail_price': 230.0, 'sale_count': 10761}, {'name': '优萃鲜肌元気精华液', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 2955}, {'name': '优萃鲜肌元気水', 'retail_price': 108.0, 'suggest_retail_price': 138.0, 'sale_count': 87350}, {'name': '优萃鲜肌元気乳', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 48995}, {'name': '优萃鲜肌元気面霜', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 35319}, {'name': '莎婷乳木果洗手液', 'retail_price': 68.0, 'suggest_retail_price': 85.0, 'sale_count': 1413}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15044}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15044}, {'name': '三重水光安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 13664}, {'name': '极光透亮安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 11136}, {'name': '多维抗皱安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 6228}, {'name': '细肤焕颜安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 2773}, {'name': 'B族维生素片/辅酶Q10维生素E胶囊 任意2盒298元', 'retail_price': 298.0, 'suggest_retail_price': 396.0, 'sale_count': 28737}, {'name': '曦露花妍香水', 'retail_price': 318.0, 'suggest_retail_price': 378.0, 'sale_count': 4653}, {'name': '元気保湿组', 'retail_price': 188.0, 'suggest_retail_price': 336.0, 'sale_count': 87350}, {'name': '优萃鲜肌元気水', 'retail_price': 108.0, 'suggest_retail_price': 138.0, 'sale_count': 87350}, {'name': '优萃鲜肌元気精华液', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 2955}, {'name': '优萃鲜肌元気乳', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 48995}, {'name': '优萃鲜肌元気面霜', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 35319}, {'name': '三重水光安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 13664}, {'name': '极光透亮安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 11136}, {'name': '多维抗皱安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 6228}, {'name': '细肤焕颜安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 2774}, {'name': '减加膜法组（含：高水份面膜霜，幻时5X柔润焕活晚安冻膜）', 'retail_price': 288.0, 'suggest_retail_price': 410.0, 'sale_count': 70474}, {'name': '幻时5X晚霜', 'retail_price': 368.0, 'suggest_retail_price': 460.0, 'sale_count': 0}, {'name': '幻时5X柔润焕活晚安冻膜', 'retail_price': 208.0, 'suggest_retail_price': 260.0, 'sale_count': 33019}, {'name': '幻时5X轻盈润采粉底乳', 'retail_price': 268.0, 'suggest_retail_price': 335.0, 'sale_count': 32829}, {'name': '幻时5X多效洗面乳', 'retail_price': 238.0, 'suggest_retail_price': 298.0, 'sale_count': 4850}, {'name': '幻时5X柔润焕活精华水', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 25307}, {'name': '幻时5X日霜', 'retail_price': 368.0, 'suggest_retail_price': 460.0, 'sale_count': 19324}, {'name': '青春明眸组（含：幻时抗皱精华素，舒活眼膜啫哩）', 'retail_price': 388.0, 'suggest_retail_price': 568.0, 'sale_count': 87420}, {'name': '抗初老王牌组', 'retail_price': 388.0, 'suggest_retail_price': 596.0, 'sale_count': 61728}, {'name': '幻时®新生保湿柔肤水', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 41389}, {'name': '幻时®抗皱精华素', 'retail_price': 278.0, 'suggest_retail_price': 348.0, 'sale_count': 87420}, {'name': '幻时®抗皱保湿乳', 'retail_price': 298.0, 'suggest_retail_price': 348.0, 'sale_count': 2623}, {'name': '幻时佳高阶紧塑精华露买大送小（含：幻时佳高阶紧塑精华露，幻时佳高阶紧塑精华露旅行装10ml）', 'retail_price': 688.0, 'suggest_retail_price': 860.0, 'sale_count': 20712}, {'name': '幻时佳®活颜紧致精华霜', 'retail_price': 748.0, 'suggest_retail_price': 930.0, 'sale_count': 29337}, {'name': '幻时佳®多效修护眼霜', 'retail_price': 458.0, 'suggest_retail_price': 570.0, 'sale_count': 33370}, {'name': '幻时佳®紧颜生物纤维面膜', 'retail_price': 628.0, 'suggest_retail_price': 780.0, 'sale_count': 443}, {'name': '幻时佳高阶维C精华露（尊享装）', 'retail_price': 768.0, 'suggest_retail_price': 958.0, 'sale_count': 18393}, {'name': 'LumiVie亮采滋润乳', 'retail_price': 288.0, 'suggest_retail_price': 338.0, 'sale_count': 2468}, {'name': 'LumiVie亮采滋润霜', 'retail_price': 288.0, 'suggest_retail_price': 338.0, 'sale_count': 2688}, {'name': 'LumiVie亮采原液精华面膜', 'retail_price': 318.0, 'suggest_retail_price': 373.0, 'sale_count': 1863}, {'name': '亮采光润粉底乳SPF18 PA++', 'retail_price': 238.0, 'suggest_retail_price': 298.0, 'sale_count': 6619}, {'name': 'LumiVie亮采洁面霜', 'retail_price': 195.0, 'suggest_retail_price': 228.0, 'sale_count': 17224}, {'name': 'LumiVie亮采精华水', 'retail_price': 195.0, 'suggest_retail_price': 228.0, 'sale_count': 2974}, {'name': 'LumiVie亮采集效焕白精华液', 'retail_price': 588.0, 'suggest_retail_price': 698.0, 'sale_count': 4192}, {'name': 'LumiVie亮采精华眼霜', 'retail_price': 305.0, 'suggest_retail_price': 360.0, 'sale_count': 2282}, {'name': '舒颜洁面乳', 'retail_price': 128.0, 'suggest_retail_price': 158.0, 'sale_count': 14589}, {'name': '舒颜柔肤水', 'retail_price': 148.0, 'suggest_retail_price': 188.0, 'sale_count': 4102}, {'name': '舒颜精华露', 'retail_price': 228.0, 'suggest_retail_price': 268.0, 'sale_count': 6376}, {'name': '舒颜保湿霜', 'retail_price': 208.0, 'suggest_retail_price': 258.0, 'sale_count': 6510}, {'name': '舒颜面膜', 'retail_price': 178.0, 'suggest_retail_price': 218.0, 'sale_count': 2491}, {'name': '臻时粹颜®精华油', 'retail_price': 1350.0, 'suggest_retail_price': 1580.0, 'sale_count': 14282}, {'name': '臻时粹颜®精华乳', 'retail_price': 1680.0, 'suggest_retail_price': 1980.0, 'sale_count': 229}, {'name': '臻时粹颜面霜', 'retail_price': 1930.0, 'suggest_retail_price': 2280.0, 'sale_count': 306}, {'name': '臻时粹颜®眼霜', 'retail_price': 998.0, 'suggest_retail_price': 1180.0, 'sale_count': 1340}, {'name': '臻时粹颜精华油粉金版', 'retail_price': 1350.0, 'suggest_retail_price': 1580.0, 'sale_count': 0}, {'name': '臻时粹颜精华油十日旅行装', 'retail_price': 253.0, 'suggest_retail_price': 253.0, 'sale_count': 34}, {'name': '臻时粹颜精华乳十日旅行装', 'retail_price': 330.0, 'suggest_retail_price': 330.0, 'sale_count': 7}, {'name': '臻时粹颜眼霜十日旅行装', 'retail_price': 236.0, 'suggest_retail_price': 236.0, 'sale_count': 45}, {'name': '臻时粹颜面霜十日旅行装', 'retail_price': 319.0, 'suggest_retail_price': 319.0, 'sale_count': 5}, {'name': '减加膜法组（含：高水份面膜霜，幻时5X柔润焕活晚安冻膜）', 'retail_price': 288.0, 'suggest_retail_price': 410.0, 'sale_count': 70474}, {'name': '柔性洗面霜', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 32850}, {'name': '中性洗面乳', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 7676}, {'name': '保湿爽肤水', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 100698}, {'name': '洁净爽肤水', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 7330}, {'name': '滋养润肤乳液', 'retail_price': 158.0, 'suggest_retail_price': 160.0, 'sale_count': 84513}, {'name': '水份平衡乳液', 'retail_price': 158.0, 'suggest_retail_price': 160.0, 'sale_count': 4957}, {'name': '高水份面膜霜', 'retail_price': 138.0, 'suggest_retail_price': 150.0, 'sale_count': 70474}, {'name': '滋养面膜霜', 'retail_price': 138.0, 'suggest_retail_price': 150.0, 'sale_count': 32217}, {'name': '青春明眸组（含：幻时抗皱精华素，舒活眼膜啫哩）', 'retail_price': 388.0, 'suggest_retail_price': 568.0, 'sale_count': 87420}, {'name': '清爽卸妆液', 'retail_price': 98.0, 'suggest_retail_price': 115.0, 'sale_count': 70674}, {'name': '水柔新肤霜', 'retail_price': 150.0, 'suggest_retail_price': 150.0, 'sale_count': 5507}, {'name': '丰润滋养霜', 'retail_price': 110.0, 'suggest_retail_price': 110.0, 'sale_count': 9131}, {'name': '舒活眼膜啫哩', 'retail_price': 188.0, 'suggest_retail_price': 220.0, 'sale_count': 76599}, {'name': '柔润精华眼霜', 'retail_price': 130.0, 'suggest_retail_price': 130.0, 'sale_count': 11155}, {'name': '防晒霜 SPF20/PA++', 'retail_price': 168.0, 'suggest_retail_price': 198.0, 'sale_count': 31705}, {'name': '晒后修护露', 'retail_price': 115.0, 'suggest_retail_price': 135.0, 'sale_count': 16358}, {'name': '胸部护理霜', 'retail_price': 158.0, 'suggest_retail_price': 190.0, 'sale_count': 7561}, {'name': '莎婷®护体乳木果奢宠沐浴露', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 3538}, {'name': '莎婷®护体乳木果焕活磨砂膏', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 2549}, {'name': '莎婷®护体乳木果丝滑润肤乳', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 3499}, {'name': '莎婷®乳木果护手霜', 'retail_price': 78.0, 'suggest_retail_price': 98.0, 'sale_count': 13226}, {'name': '莎婷®手部护理套装', 'retail_price': 238.0, 'suggest_retail_price': 328.0, 'sale_count': 5126}, {'name': '莎婷®乳木果润唇膏', 'retail_price': 88.0, 'suggest_retail_price': 118.0, 'sale_count': 16342}, {'name': '莎婷®乳木果唇膜', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 5129}, {'name': '莎婷乳木果洗手液', 'retail_price': 68.0, 'suggest_retail_price': 85.0, 'sale_count': 1413}, {'name': '抗痘调理精华露', 'retail_price': 192.0, 'suggest_retail_price': 225.0, 'sale_count': 1515}, {'name': '调色润妍妆前乳 ', 'retail_price': 158.0, 'suggest_retail_price': 223.0, 'sale_count': 407}, {'name': '粉扬遮瑕膏 ', 'retail_price': 138.0, 'suggest_retail_price': 210.0, 'sale_count': 1702}, {'name': '睛彩液体眼影 ', 'retail_price': 78.0, 'suggest_retail_price': 223.0, 'sale_count': 0}, {'name': '玩色丝慕唇膏钻石限量版', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 522}, {'name': '立体闪耀高光粉饼钻石限量版', 'retail_price': 108.0, 'suggest_retail_price': 135.0, 'sale_count': 2057}, {'name': '轻盈纯色腮红钻石限量版粉色', 'retail_price': 108.0, 'suggest_retail_price': 135.0, 'sale_count': 783}, {'name': '粉扬眉笔', 'retail_price': 128.0, 'suggest_retail_price': 160.0, 'sale_count': 3610}, {'name': '印彩丝柔哑光唇膏', 'retail_price': 188.0, 'suggest_retail_price': 235.0, 'sale_count': 1238}, {'name': '润泽护唇膏', 'retail_price': 138.0, 'suggest_retail_price': 173.0, 'sale_count': 103}, {'name': '清透无痕蜜粉', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 9352}, {'name': '玩色丝慕唇膏', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 1623}, {'name': '粉扬遮瑕膏', 'retail_price': 168.0, 'suggest_retail_price': 210.0, 'sale_count': 0}, {'name': '调色润妍妆前乳', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 0}, {'name': '底妆刷', 'retail_price': 92.0, 'suggest_retail_price': 115.0, 'sale_count': 172}, {'name': 'B族维生素片/辅酶Q10维生素E胶囊 任意2盒298元', 'retail_price': 298.0, 'suggest_retail_price': 396.0, 'sale_count': 31956}, {'name': '抗氧明星组 含：怡日健粉妍片2盒', 'retail_price': 799.0, 'suggest_retail_price': 1020.0, 'sale_count': 90456}, {'name': '人气弹弹组 含：怡日健胶原蛋白肽固体饮料（30条装）2盒', 'retail_price': 999.0, 'suggest_retail_price': 1456.0, 'sale_count': 68868}, {'name': '怡日健辅酶Q10维生素E胶囊', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 31956}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15044}, {'name': '胶原蛋白肽固体饮料12条装', 'retail_price': 298.0, 'suggest_retail_price': 298.0, 'sale_count': 40530}, {'name': '益生菌固体饮料', 'retail_price': 360.0, 'suggest_retail_price': 360.0, 'sale_count': 125243}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15044}, {'name': '怡日健B族维生素片', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 28737}, {'name': '怡日健粉妍片', 'retail_price': 510.0, 'suggest_retail_price': 510.0, 'sale_count': 90456}, {'name': '怡日健 番茄红素维生素E软胶囊', 'retail_price': 333.0, 'suggest_retail_price': 333.0, 'sale_count': 16962}, {'name': '怡日健®酵母β-葡聚糖固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 101285}, {'name': '怡日健®水溶性膳食纤维固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 46852}, {'name': '怡日健®固多肽固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 54126}, {'name': '怡日健®γ－氨基丁酸固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 8142}, {'name': '怡日健®白芸豆固体饮料', 'retail_price': 498.0, 'suggest_retail_price': 498.0, 'sale_count': 719}, {'name': '怡日健DHA藻油叶黄素酯软糖凝胶糖果', 'retail_price': 230.0, 'suggest_retail_price': 230.0, 'sale_count': 10761}, {'name': '怡日健酵母β-葡聚糖乳清蛋白压片糖果', 'retail_price': 230.0, 'suggest_retail_price': 230.0, 'sale_count': 548}, {'name': '怡日健DHA藻油叶黄素酯软糖凝胶糖果 2瓶', 'retail_price': 398.0, 'suggest_retail_price': 460.0, 'sale_count': 10761}, {'name': '益生菌固体饮料5条便携装2包', 'retail_price': 120.0, 'suggest_retail_price': 120.0, 'sale_count': 72}, {'name': '元気保湿组', 'retail_price': 188.0, 'suggest_retail_price': 336.0, 'sale_count': 87359}, {'name': '优萃鲜肌元気水', 'retail_price': 108.0, 'suggest_retail_price': 138.0, 'sale_count': 87359}, {'name': '优萃鲜肌元気精华液', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 2955}, {'name': '优萃鲜肌元気乳', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 48999}, {'name': '优萃鲜肌元気面霜', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 35323}, {'name': '元気保湿组', 'retail_price': 188.0, 'suggest_retail_price': 336.0, 'sale_count': 87350}, {'name': '经典护肤组 含：保湿爽肤水+滋养润肤乳液', 'retail_price': 188.0, 'suggest_retail_price': 280.0, 'sale_count': 100694}, {'name': '柔性洗面霜', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 32848}, {'name': '中性洗面乳', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 7674}, {'name': '保湿爽肤水', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 100694}, {'name': '洁净爽肤水', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 7330}, {'name': '滋养润肤乳液', 'retail_price': 158.0, 'suggest_retail_price': 160.0, 'sale_count': 84508}, {'name': '水份平衡乳液', 'retail_price': 158.0, 'suggest_retail_price': 160.0, 'sale_count': 4957}, {'name': '高水份面膜霜', 'retail_price': 138.0, 'suggest_retail_price': 150.0, 'sale_count': 70473}, {'name': '滋养面膜霜', 'retail_price': 138.0, 'suggest_retail_price': 150.0, 'sale_count': 32215}, {'name': '三重水光安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 13664}, {'name': '舒颜精华露', 'retail_price': 228.0, 'suggest_retail_price': 268.0, 'sale_count': 6376}, {'name': '幻时5X柔润焕活晚安冻膜', 'retail_price': 208.0, 'suggest_retail_price': 260.0, 'sale_count': 33019}, {'name': '舒颜洁面乳', 'retail_price': 128.0, 'suggest_retail_price': 158.0, 'sale_count': 14589}, {'name': '舒颜柔肤水', 'retail_price': 148.0, 'suggest_retail_price': 188.0, 'sale_count': 4102}, {'name': '舒颜保湿霜', 'retail_price': 208.0, 'suggest_retail_price': 258.0, 'sale_count': 6510}, {'name': '舒颜面膜', 'retail_price': 178.0, 'suggest_retail_price': 218.0, 'sale_count': 2491}, {'name': '三重水光安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 13664}, {'name': '极光透亮安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 11136}, {'name': '多维抗皱安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 6228}, {'name': '细肤焕颜安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 2773}, {'name': 'LumiVie亮采滋润乳', 'retail_price': 288.0, 'suggest_retail_price': 338.0, 'sale_count': 2468}, {'name': 'LumiVie亮采精华眼霜', 'retail_price': 305.0, 'suggest_retail_price': 360.0, 'sale_count': 2282}, {'name': '亮采光润粉底乳SPF18 PA++', 'retail_price': 238.0, 'suggest_retail_price': 298.0, 'sale_count': 6619}, {'name': '晒后修护露', 'retail_price': 115.0, 'suggest_retail_price': 135.0, 'sale_count': 16358}, {'name': '防晒霜 SPF20/PA++', 'retail_price': 168.0, 'suggest_retail_price': 198.0, 'sale_count': 31705}, {'name': '极光透亮安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 11136}, {'name': 'LumiVie亮采集效焕白精华液', 'retail_price': 588.0, 'suggest_retail_price': 698.0, 'sale_count': 4192}, {'name': 'LumiVie亮采洁面霜', 'retail_price': 195.0, 'suggest_retail_price': 228.0, 'sale_count': 17224}, {'name': 'LumiVie亮采原液精华面膜', 'retail_price': 318.0, 'suggest_retail_price': 373.0, 'sale_count': 1863}, {'name': 'LumiVie亮采精华水', 'retail_price': 195.0, 'suggest_retail_price': 228.0, 'sale_count': 2974}, {'name': 'LumiVie亮采滋润霜', 'retail_price': 288.0, 'suggest_retail_price': 338.0, 'sale_count': 2688}, {'name': '幻时佳高阶紧塑精华露买大送小（含：幻时佳高阶紧塑精华露，幻时佳高阶紧塑精华露旅行装10ml）', 'retail_price': 688.0, 'suggest_retail_price': 860.0, 'sale_count': 20708}, {'name': '抗初老王牌组', 'retail_price': 388.0, 'suggest_retail_price': 596.0, 'sale_count': 61722}, {'name': '幻时5X轻盈润采粉底乳', 'retail_price': 268.0, 'suggest_retail_price': 335.0, 'sale_count': 17043}, {'name': '幻时®抗皱保湿乳', 'retail_price': 298.0, 'suggest_retail_price': 348.0, 'sale_count': 2623}, {'name': '幻时®新生保湿柔肤水', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 41384}, {'name': '幻时5X多效洗面乳', 'retail_price': 238.0, 'suggest_retail_price': 298.0, 'sale_count': 10393}, {'name': '幻时5X柔润焕活精华水', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 25305}, {'name': '幻时5X日霜', 'retail_price': 368.0, 'suggest_retail_price': 460.0, 'sale_count': 19324}, {'name': '幻时5X晚霜', 'retail_price': 368.0, 'suggest_retail_price': 460.0, 'sale_count': 0}, {'name': '幻时5X柔润焕活晚安冻膜', 'retail_price': 208.0, 'suggest_retail_price': 260.0, 'sale_count': 33019}, {'name': '多维抗皱安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 6228}, {'name': '幻时佳高阶维C精华露（尊享装）', 'retail_price': 768.0, 'suggest_retail_price': 958.0, 'sale_count': 18391}, {'name': '幻时®抗皱精华素', 'retail_price': 278.0, 'suggest_retail_price': 348.0, 'sale_count': 87412}, {'name': '幻时佳®活颜紧致精华霜', 'retail_price': 748.0, 'suggest_retail_price': 930.0, 'sale_count': 29335}, {'name': '幻时佳®多效修护眼霜', 'retail_price': 458.0, 'suggest_retail_price': 570.0, 'sale_count': 33367}, {'name': '臻时粹颜®精华油', 'retail_price': 1350.0, 'suggest_retail_price': 1580.0, 'sale_count': 14282}, {'name': '臻时粹颜®精华乳', 'retail_price': 1680.0, 'suggest_retail_price': 1980.0, 'sale_count': 229}, {'name': '臻时粹颜面霜', 'retail_price': 1930.0, 'suggest_retail_price': 2280.0, 'sale_count': 306}, {'name': '臻时粹颜®眼霜', 'retail_price': 998.0, 'suggest_retail_price': 1180.0, 'sale_count': 1340}, {'name': '清爽卸妆液', 'retail_price': 98.0, 'suggest_retail_price': 115.0, 'sale_count': 70674}, {'name': '舒活眼膜啫哩', 'retail_price': 188.0, 'suggest_retail_price': 220.0, 'sale_count': 76599}, {'name': '水柔新肤霜', 'retail_price': 150.0, 'suggest_retail_price': 150.0, 'sale_count': 5507}, {'name': '丰润滋养霜', 'retail_price': 110.0, 'suggest_retail_price': 110.0, 'sale_count': 9131}, {'name': '柔润精华眼霜', 'retail_price': 130.0, 'suggest_retail_price': 130.0, 'sale_count': 11155}, {'name': '胸部护理霜', 'retail_price': 158.0, 'suggest_retail_price': 190.0, 'sale_count': 7561}, {'name': '莎婷®护体乳木果奢宠沐浴露', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 3538}, {'name': '莎婷®护体乳木果焕活磨砂膏', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 2549}, {'name': '莎婷®护体乳木果丝滑润肤乳', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 3499}, {'name': '莎婷®乳木果护手霜', 'retail_price': 78.0, 'suggest_retail_price': 98.0, 'sale_count': 13230}, {'name': '莎婷®手部护理套装', 'retail_price': 238.0, 'suggest_retail_price': 328.0, 'sale_count': 5126}, {'name': '莎婷®乳木果润唇膏', 'retail_price': 88.0, 'suggest_retail_price': 118.0, 'sale_count': 16343}, {'name': '莎婷®乳木果唇膜', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 5129}, {'name': '莎婷乳木果洗手液', 'retail_price': 68.0, 'suggest_retail_price': 85.0, 'sale_count': 1413}, {'name': '中性洗面乳', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 7676}, {'name': '舒颜洁面乳', 'retail_price': 128.0, 'suggest_retail_price': 158.0, 'sale_count': 14590}, {'name': '清爽卸妆液', 'retail_price': 98.0, 'suggest_retail_price': 115.0, 'sale_count': 70674}, {'name': 'LumiVie亮采洁面霜', 'retail_price': 195.0, 'suggest_retail_price': 228.0, 'sale_count': 17224}, {'name': '幻时5X多效洗面乳', 'retail_price': 238.0, 'suggest_retail_price': 298.0, 'sale_count': 4850}, {'name': '柔性洗面霜', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 32850}, {'name': '幻时5X柔润焕活精华水', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 25305}, {'name': 'LumiVie亮采精华水', 'retail_price': 195.0, 'suggest_retail_price': 228.0, 'sale_count': 2971}, {'name': '幻时®新生保湿柔肤水', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 41384}, {'name': '保湿爽肤水', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 100694}, {'name': '洁净爽肤水', 'retail_price': 108.0, 'suggest_retail_price': 120.0, 'sale_count': 7330}, {'name': '舒颜柔肤水', 'retail_price': 148.0, 'suggest_retail_price': 188.0, 'sale_count': 4102}, {'name': '优萃鲜肌元気水', 'retail_price': 108.0, 'suggest_retail_price': 138.0, 'sale_count': 87350}, {'name': '幻时佳高阶紧塑精华露买大送小（含：幻时佳高阶紧塑精华露，幻时佳高阶紧塑精华露旅行装10ml）', 'retail_price': 688.0, 'suggest_retail_price': 860.0, 'sale_count': 20708}, {'name': '幻时®抗皱精华素', 'retail_price': 278.0, 'suggest_retail_price': 348.0, 'sale_count': 87412}, {'name': 'LumiVie亮采集效焕白精华液', 'retail_price': 588.0, 'suggest_retail_price': 698.0, 'sale_count': 4192}, {'name': '臻时粹颜®精华油', 'retail_price': 1350.0, 'suggest_retail_price': 1580.0, 'sale_count': 14282}, {'name': '舒颜精华露', 'retail_price': 228.0, 'suggest_retail_price': 268.0, 'sale_count': 6376}, {'name': '臻时粹颜®精华乳', 'retail_price': 1680.0, 'suggest_retail_price': 1980.0, 'sale_count': 229}, {'name': '抗痘调理精华露', 'retail_price': 192.0, 'suggest_retail_price': 225.0, 'sale_count': 1515}, {'name': '极光透亮安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 11136}, {'name': '三重水光安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 13664}, {'name': '多维抗皱安瓶精华液', 'retail_price': 288.0, 'suggest_retail_price': 358.0, 'sale_count': 6228}, {'name': '细肤焕颜安瓶精华液', 'retail_price': 258.0, 'suggest_retail_price': 328.0, 'sale_count': 2773}, {'name': '优萃鲜肌元気精华液', 'retail_price': 198.0, 'suggest_retail_price': 248.0, 'sale_count': 2955}, {'name': '幻时佳®多效修护眼霜', 'retail_price': 458.0, 'suggest_retail_price': 570.0, 'sale_count': 33370}, {'name': 'LumiVie亮采精华眼霜', 'retail_price': 305.0, 'suggest_retail_price': 360.0, 'sale_count': 2282}, {'name': '舒活眼膜啫哩', 'retail_price': 188.0, 'suggest_retail_price': 220.0, 'sale_count': 76599}, {'name': '柔润精华眼霜', 'retail_price': 130.0, 'suggest_retail_price': 130.0, 'sale_count': 11155}, {'name': '臻时粹颜®眼霜', 'retail_price': 998.0, 'suggest_retail_price': 1180.0, 'sale_count': 1340}, {'name': 'LumiVie亮采滋润霜', 'retail_price': 288.0, 'suggest_retail_price': 338.0, 'sale_count': 2688}, {'name': '舒颜保湿霜', 'retail_price': 208.0, 'suggest_retail_price': 258.0, 'sale_count': 6510}, {'name': '臻时粹颜面霜', 'retail_price': 1930.0, 'suggest_retail_price': 2280.0, 'sale_count': 306}, {'name': '水柔新肤霜', 'retail_price': 150.0, 'suggest_retail_price': 150.0, 'sale_count': 5507}, {'name': '丰润滋养霜', 'retail_price': 110.0, 'suggest_retail_price': 110.0, 'sale_count': 9131}, {'name': '幻时佳®活颜紧致精华霜', 'retail_price': 748.0, 'suggest_retail_price': 930.0, 'sale_count': 29335}, {'name': '幻时5X日霜', 'retail_price': 368.0, 'suggest_retail_price': 460.0, 'sale_count': 19324}, {'name': '幻时5X晚霜', 'retail_price': 368.0, 'suggest_retail_price': 460.0, 'sale_count': 0}, {'name': '优萃鲜肌元気乳', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 48995}, {'name': '优萃鲜肌元気面霜', 'retail_price': 158.0, 'suggest_retail_price': 198.0, 'sale_count': 35319}, {'name': '幻时®抗皱保湿乳', 'retail_price': 298.0, 'suggest_retail_price': 348.0, 'sale_count': 61722}, {'name': 'LumiVie亮采滋润乳', 'retail_price': 288.0, 'suggest_retail_price': 338.0, 'sale_count': 2468}, {'name': 'LumiVie亮采原液精华面膜', 'retail_price': 318.0, 'suggest_retail_price': 373.0, 'sale_count': 1863}, {'name': '幻时5X柔润焕活晚安冻膜', 'retail_price': 208.0, 'suggest_retail_price': 260.0, 'sale_count': 33019}, {'name': '舒活眼膜啫哩', 'retail_price': 188.0, 'suggest_retail_price': 220.0, 'sale_count': 76599}, {'name': '高水份面膜霜', 'retail_price': 138.0, 'suggest_retail_price': 150.0, 'sale_count': 70474}, {'name': '滋养面膜霜', 'retail_price': 138.0, 'suggest_retail_price': 150.0, 'sale_count': 32217}, {'name': '舒颜面膜', 'retail_price': 178.0, 'suggest_retail_price': 218.0, 'sale_count': 2491}, {'name': '幻时佳®紧颜生物纤维面膜', 'retail_price': 628.0, 'suggest_retail_price': 780.0, 'sale_count': 443}, {'name': '亮采光润粉底乳SPF18 PA++', 'retail_price': 238.0, 'suggest_retail_price': 298.0, 'sale_count': 6618}, {'name': '幻时5X轻盈润采粉底乳', 'retail_price': 268.0, 'suggest_retail_price': 335.0, 'sale_count': 32826}, {'name': '晒后修护露', 'retail_price': 115.0, 'suggest_retail_price': 135.0, 'sale_count': 16357}, {'name': '防晒霜 SPF20/PA++', 'retail_price': 168.0, 'suggest_retail_price': 198.0, 'sale_count': 31703}, {'name': '胸部护理霜', 'retail_price': 158.0, 'suggest_retail_price': 190.0, 'sale_count': 7561}, {'name': '莎婷®护体乳木果奢宠沐浴露', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 3538}, {'name': '莎婷®护体乳木果焕活磨砂膏', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 2549}, {'name': '莎婷®护体乳木果丝滑润肤乳', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 3499}, {'name': '莎婷®乳木果护手霜', 'retail_price': 78.0, 'suggest_retail_price': 98.0, 'sale_count': 13226}, {'name': '莎婷®手部护理套装', 'retail_price': 238.0, 'suggest_retail_price': 328.0, 'sale_count': 5126}, {'name': '莎婷®乳木果润唇膏', 'retail_price': 88.0, 'suggest_retail_price': 118.0, 'sale_count': 16342}, {'name': '莎婷®乳木果唇膜', 'retail_price': 98.0, 'suggest_retail_price': 118.0, 'sale_count': 5129}, {'name': '莎婷乳木果洗手液', 'retail_price': 68.0, 'suggest_retail_price': 85.0, 'sale_count': 1413}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15050}, {'name': '怡日健B族维生素片', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 28750}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15050}, {'name': 'B族维生素片/辅酶Q10维生素E胶囊 任意2盒298元', 'retail_price': 298.0, 'suggest_retail_price': 396.0, 'sale_count': 31964}, {'name': '怡日健 番茄红素维生素E软胶囊', 'retail_price': 333.0, 'suggest_retail_price': 333.0, 'sale_count': 17000}, {'name': '怡日健粉妍片', 'retail_price': 510.0, 'suggest_retail_price': 510.0, 'sale_count': 90486}, {'name': '抗氧明星组 含：怡日健粉妍片2盒', 'retail_price': 799.0, 'suggest_retail_price': 1020.0, 'sale_count': 90486}, {'name': '益生菌固体饮料', 'retail_price': 360.0, 'suggest_retail_price': 360.0, 'sale_count': 125243}, {'name': '怡日健®水溶性膳食纤维固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 46852}, {'name': '怡日健®酵母β-葡聚糖固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 101285}, {'name': '益生菌固体饮料', 'retail_price': 360.0, 'suggest_retail_price': 360.0, 'sale_count': 125243}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15050}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15050}, {'name': 'B族维生素片/辅酶Q10维生素E胶囊 任意2盒298元', 'retail_price': 298.0, 'suggest_retail_price': 396.0, 'sale_count': 31964}, {'name': '抗氧明星组 含：怡日健粉妍片2盒', 'retail_price': 799.0, 'suggest_retail_price': 1020.0, 'sale_count': 90486}, {'name': '人气弹弹组 含：怡日健胶原蛋白肽固体饮料（30条装）2盒', 'retail_price': 999.0, 'suggest_retail_price': 1456.0, 'sale_count': 68896}, {'name': '怡日健辅酶Q10维生素E胶囊', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 31964}, {'name': '怡日健粉妍片', 'retail_price': 510.0, 'suggest_retail_price': 510.0, 'sale_count': 90486}, {'name': '怡日健 番茄红素维生素E软胶囊', 'retail_price': 333.0, 'suggest_retail_price': 333.0, 'sale_count': 17000}, {'name': '怡日健B族维生素片', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 28750}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15050}, {'name': '怡日健®固多肽固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 54126}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15050}, {'name': '怡日健®白芸豆固体饮料', 'retail_price': 498.0, 'suggest_retail_price': 498.0, 'sale_count': 719}, {'name': '怡日健B族维生素片', 'retail_price': 198.0, 'suggest_retail_price': 198.0, 'sale_count': 28750}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15050}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15050}, {'name': '怡日健®γ－氨基丁酸固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 8142}, {'name': '益生菌固体饮料', 'retail_price': 360.0, 'suggest_retail_price': 360.0, 'sale_count': 125243}, {'name': '怡日健乳钙蛋白质粉固体饮料', 'retail_price': 368.0, 'suggest_retail_price': 368.0, 'sale_count': 15050}, {'name': '怡日健®固多肽固体饮料', 'retail_price': 450.0, 'suggest_retail_price': 450.0, 'sale_count': 54126}, {'name': '乳钙蛋白质粉固体饮料2盒', 'retail_price': 666.0, 'suggest_retail_price': 736.0, 'sale_count': 15050}, {'name': '怡日健DHA藻油叶黄素酯软糖凝胶糖果', 'retail_price': 230.0, 'suggest_retail_price': 230.0, 'sale_count': 10761}, {'name': '怡日健酵母β-葡聚糖乳清蛋白压片糖果', 'retail_price': 230.0, 'suggest_retail_price': 230.0, 'sale_count': 548}, {'name': '怡日健DHA藻油叶黄素酯软糖凝胶糖果 2瓶', 'retail_price': 398.0, 'suggest_retail_price': 460.0, 'sale_count': 10761}, {'name': '调色润妍妆前乳 ', 'retail_price': 158.0, 'suggest_retail_price': 223.0, 'sale_count': 407}, {'name': '粉扬遮瑕膏 ', 'retail_price': 138.0, 'suggest_retail_price': 210.0, 'sale_count': 1702}, {'name': '立体闪耀高光粉饼钻石限量版', 'retail_price': 108.0, 'suggest_retail_price': 135.0, 'sale_count': 2057}, {'name': '轻盈纯色腮红钻石限量版粉色', 'retail_price': 108.0, 'suggest_retail_price': 135.0, 'sale_count': 783}, {'name': '清透无痕蜜粉', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 9352}, {'name': '粉扬遮瑕膏', 'retail_price': 168.0, 'suggest_retail_price': 210.0, 'sale_count': 0}, {'name': '调色润妍妆前乳', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 0}, {'name': '玩色丝慕唇膏钻石限量版', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 522}, {'name': '润泽护唇膏', 'retail_price': 138.0, 'suggest_retail_price': 173.0, 'sale_count': 103}, {'name': '印彩丝柔哑光唇膏', 'retail_price': 188.0, 'suggest_retail_price': 235.0, 'sale_count': 1238}, {'name': '玩色丝慕唇膏', 'retail_price': 178.0, 'suggest_retail_price': 223.0, 'sale_count': 1623}, {'name': '睛彩液体眼影 ', 'retail_price': 78.0, 'suggest_retail_price': 223.0, 'sale_count': 0}, {'name': '粉扬眉笔', 'retail_price': 128.0, 'suggest_retail_price': 160.0, 'sale_count': 3610}, {'name': '底妆刷', 'retail_price': 92.0, 'suggest_retail_price': 115.0, 'sale_count': 172}, {'name': '曦露花妍香水', 'retail_price': 318.0, 'suggest_retail_price': 378.0, 'sale_count': 4653}, {'name': '旅情®护体乳', 'retail_price': 82.0, 'suggest_retail_price': 95.0, 'sale_count': 21823}, {'name': '璀璨人生香水', 'retail_price': 338.0, 'suggest_retail_price': 428.0, 'sale_count': 3582}, {'name': '男士洁面乳', 'retail_price': 108.0, 'suggest_retail_price': 130.0, 'sale_count': 7193}, {'name': '男士保湿乳SPF30', 'retail_price': 168.0, 'suggest_retail_price': 218.0, 'sale_count': 1440}, {'name': '男士爽肤水', 'retail_price': 118.0, 'suggest_retail_price': 150.0, 'sale_count': 2650}, {'name': '男士保湿乳液', 'retail_price': 158.0, 'suggest_retail_price': 200.0, 'sale_count': 4217}]

def getCategory():
    cate_url=domain+cate_path
    data={'access_token':access_token}
    print(cate_url)
    r=requests.get(url=cate_url,params=data,verify=verify_ssl)
    print(r.status_code)
    if r.status_code==401:
        print(r.content)
        return {}
    elif r.status_code==200:
        return r.json()

def settleCate(catelist):
    result_list=[]
    for item in catelist['top_menu']:
        result_list.append({'Name':item['name'],'id':item['id']})
    return result_list

def settleSubCate(sublist):
    result_list=[]
    for item in sublist['categories'][0]['sub_categories']:
        for subitem in item['sub_categories']:
            result_list.append({'Name':subitem['name'],'id':subitem['id']})
    return result_list

def getProduct(category_id):
    product_url=domain+product_path
    data={'access_token':access_token,'category_id':category_id}
    r = requests.get(url=product_url, params=data, verify=verify_ssl)
    print(r.status_code)
    if r.status_code==401:
        print(r.content)
        return {}
    elif r.status_code==200:
        return r.json()

def collectProduct(productList,product):
    print(product)
    for i in product['categories'][0]['products']:
        productList.append({'name':i['name'],'retail_price':i['retail_price'],'suggest_retail_price':i['suggest_retail_price'],'sale_count':i['sale_count']})
    return productList

def cfgRead():
	with open('config.ini','r') as newfile:
		return json.load(newfile)


def cfgRecord(content):
	#print (json.dumps(content))
	with open('config.ini','w') as newfile:
		newfile.write(json.dumps(content))
	return

# def writeCSV(file,content):
# 	with open(file,'w') as csvfile:
#         csv_writer=csv.writer(csvfile)
# 		csv_writer.writerow(content)
# 	return





if __name__=='__main__':
    # ProductList=[]
    # CategoryList_origin=getCategory()
    # print('originCate:',CategoryList_origin)
    # if CategoryList_origin!={}:
    #     CategoryList_settle=settleCate(CategoryList_origin)
    #     print('settleCate:',CategoryList_settle)
    #     for i in CategoryList_settle:
    #         product_origin=getProduct(i['id'])
    #         if len(product_origin['categories'][0]['sub_categories'])>0:
    #             print('It\'s subcategory')
    #             SubList=settleSubCate(product_origin)
    #             print(SubList)
    #             for j in SubList:
    #                 product_origin=getProduct(j['id'])
    #                 print('originProduct:', product_origin)
    #                 ProductList=collectProduct(ProductList,product_origin)
    #         elif len(product_origin['categories'][0]['products'])>0:
    #             print('originProduct:',product_origin)
    #             ProductList = collectProduct(ProductList, product_origin)
    #
    # print('FinalResult=',ProductList)


    csv_file = open(filePath, mode='w+',encoding='gb18030')

    title=testvalue[0].keys()
    print(title)
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(title)
    for i in testvalue:
        print(i.values())
        csv_writer.writerow(i.values())
    csv_file.close()