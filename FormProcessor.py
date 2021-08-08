import os,sys,time
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import  PatternFill

FileDirectory='D:\\PrivateWork\\'    #文件路径
Form1Name=r'机关2021.3.15-2021.6.9from刘陈(1).xlsx'
Form2Name=r'进项明细7.24（动态变动）.xlsx'
Form1Path=FileDirectory+Form1Name
Form2Path=FileDirectory+Form2Name
blackwords=['盒']
Cartridges={'CE411-413A':['CE411A','CE412A','CE413A'],'CF501-503A':['CF501A','CF502A','CF503A'],'CF401-403A':['CF401A','CF402A','CF403A']}
SplitSign_And=[',','，',' ','；',';']
SplitSign_Or=['/']
Brand_OnlyCheckName=['迪欧']

class FormProcessor():
    wb1 = Workbook()
    wb2 = Workbook()

    ''' 备份表 '''
    def BackupFile(self,OriginFile,TargetFile):
        cmd='copy '+OriginFile+' '+FileDirectory+TargetFile
        print(cmd)
        os.popen(cmd)
        return

    ''' 读取表文件 '''
    def GetFile(self,FilePath):
        wb = load_workbook(FilePath)
        return wb

    def GetForm(self,wb,Sheet):
        work_sheet=wb[Sheet]
        return work_sheet

    ''' 寻找表1表2的关联 '''
    def CheckForm(self, form1, form2):
        ''' 首次检索 '''
        tmp=[]
        count=0
        for i1 in range(3,form1.max_row):   #检索表1的每一行
            for j1 in range(3,6):
                if form1.cell(row=i1,column=j1).value==None:
                    tmp.append('')
                else:
                    tmp.append(str(form1.cell(row=i1,column=j1).value).upper())
            # print(tmp)

            for i2 in range(3,form2.max_row):   #检索表2的每一行
                form2_name=str(form2.cell(row=i2,column=1).value).upper()
                form2_model=str(form2.cell(row=i2,column=2).value).upper()
                if form2.cell(row=i2, column=2).value != None:  #判断表2的型号是否非空
                    if tmp[1] in form2_model:    #判断表1的型号与表2是否匹配
                        if (tmp[0] in form2_name) and (tmp[2] in form2_name):
                            # print("in form2:", i2)
                            count+=1
                            form1.cell(row=i1, column=11).value = i2
                            break
                        else:
                            # print("in form2:", i2)
                            count+=1
                            form1.cell(row=i1, column=11).value = i2
                            break
                    else:
                        if (tmp[0] in form2_name) and (tmp[1] in form2_name) and (tmp[2] in form2_name):
                            # print("in form2:", i2)
                            count += 1
                            form1.cell(row=i1,column=11).value=i2
                            break
                        else:
                            pass
                            # print(tmp, " unmatch to ", i2)

                else:   #判断表1的所有值是否在表2的商品名称中
                    if (tmp[0] in form2_name) and (tmp[1] in form2_name) and (tmp[2] in form2_name):
                        # print("in form2:", i2)
                        count += 1
                        form1.cell(row=i1, column=11).value = i2
                        break
                    else:
                        pass
                        # print(tmp," unmatch to ",i2)
            tmp = []
        print('count1=',count)

        ''' 第2次检索：在库存名称里检索型号和商品名称 '''
        count=0
        for i1 in range(3,form1.max_row):   # 检索表1的每一行
            if form1.cell(row=i1,column=11).value==None:
                for j1 in range(3,6):
                    if form1.cell(row=i1,column=j1).value==None:
                        tmp.append('')
                    else:
                        tmp.append(str(form1.cell(row=i1,column=j1).value).upper())
                # print(tmp)
                for i2 in range(3, form2.max_row):  # 检索表2的每一行
                    form2_name = str(form2.cell(row=i2, column=1).value).upper()
                    if  (tmp[1] in form2_name) and (tmp[2] in form2_name):
                        # print("in form2:", i2)
                        count += 1
                        form1.cell(row=i1, column=11).value = i2
            tmp = []
        print('count2=', count)

        ''' 第3次检索：将逗号与空格拆分后与表2去空格后的库存名称进行匹配 '''
        count=0
        for i1 in range(3,form1.max_row):   #检索表1的每一行
            tmp_sub_and = []
            tmp_sub_or = []
            if form1.cell(row=i1,column=11).value==None:
                for j1 in range(3,6):
                    if form1.cell(row=i1,column=j1).value==None:
                        tmp.append('')
                    else:
                        tmp.append(str(form1.cell(row=i1,column=j1).value).upper())
                # print(tmp)
                if tmp[0]=='' and tmp[1]=='':
                    tmp=[]
                    continue
                if ',' in tmp[1]:
                    tmp_sub_and=[]
                    word=''
                    for char in range(len(tmp[1])):
                        if tmp[1][char]!=',' :
                            word+=tmp[1][char]
                        else:
                            tmp_sub_and.append(word)
                            word=''
                    if word!='':
                        tmp_sub_and.append(word)
                    # print(tmp_sub_and)

                elif '，' in tmp[1]:
                    tmp_sub_and=[]
                    word=''
                    for char in range(len(tmp[1])):
                        if tmp[1][char]!='，' :
                            word+=tmp[1][char]
                        else:
                            tmp_sub_and.append(word)
                            word=''
                    if word!='':
                        tmp_sub_and.append(word)
                    # print(tmp_sub_and)

                elif ' ' in tmp[1]:
                    tmp_sub_and=[]
                    word=''
                    for char in range(len(tmp[1])):
                        if tmp[1][char]!=' ' :
                            word+=tmp[1][char]
                        else:
                            tmp_sub_and.append(word)
                            word=''
                    if word!='':
                        tmp_sub_and.append(word)
                    # print(tmp_sub_and)

                elif '/' in tmp[1]:
                    tmp_sub_or=[]
                    word=''
                    for char in range(len(tmp[1])):
                        if tmp[1][char]!='/' :
                            word+=tmp[1][char]
                        else:
                            tmp_sub_or.append(word)
                            word=''
                    if word!='':
                        tmp_sub_or.append(word)

                if len(tmp_sub_and) > 0:
                    for i2 in range(3, form2.max_row):  # 检索表2的每一行
                        form2_name = str(form2.cell(row=i2, column=1).value).upper()
                        finalName =''
                        for char in range(len(form2_name)):
                            if form2_name[char]!=' ':
                                finalName+=form2_name[char]

                        for x in tmp_sub_and:
                            if x not in finalName:
                                break
                        else:
                            if  (tmp[0] in finalName) :
                                # print("in form2 by name(and):", i2)
                                count += 1
                                form1.cell(row=i1, column=11).value = i2
                                break

                elif len(tmp_sub_or) > 0:
                    for i2 in range(3, form2.max_row):  # 检索表2的每一行
                        form2_name = str(form2.cell(row=i2, column=1).value).upper()
                        form2_model = str(form2.cell(row=i2, column=2).value).upper()
                        finalName =''
                        for char in range(len(form2_name)):
                            if form2_name[char]!=' ':
                                finalName+=form2_name[char]
                        for x in tmp_sub_or:
                            if x in blackwords:
                                continue
                            if x in finalName:
                                # print("in form2 by name(or):", i2)
                                # print(x)
                                count += 1
                                form1.cell(row=i1, column=11).value = i2
                                break
                            if x in form2_model:
                                # print("in form2 by model(or):", i2)
                                # print(x)
                                count += 1
                                form1.cell(row=i1, column=11).value = i2
                                break

            tmp = []
        print('count3=', count)

        ''' 第4次检索 '''
        count=0
        for i1 in range(3,form1.max_row):   #检索表1的每一行
            if form1.cell(row=i1,column=11).value==None:
                for j1 in range(3,6):
                    if form1.cell(row=i1,column=j1).value==None:
                        tmp.append('')
                    else:
                        tmp.append(str(form1.cell(row=i1,column=j1).value).upper())
                # print(tmp)
                if tmp[0]=='' and tmp[1]=='':
                    tmp=[]
                    continue
                for i2 in range(3, form2.max_row):  # 检索表2的每一行
                    form2_name = str(form2.cell(row=i2, column=1).value).upper()
                    form2_model = str(form2.cell(row=i2, column=2).value).upper()
                    if  (tmp[0] in form2_name) and (tmp[1] in form2_name):
                        # print("in form2:", i2)
                        count += 1
                        form1.cell(row=i1, column=11).value = i2
                        break
            tmp = []
        print('count4=', count)


    def FormSave(self,wb,TargetFile):
        Path=FileDirectory+TargetFile
        wb.save(Path)

    def CheckFormOnce(self,form1,form2):
        OriginData = {}
        count = 0
        result ={}

        ''' Step1 '''
        for i1 in range(3, form1.max_row):  # 检索表1的每一行
            ''' 准备表1数据 '''
            if form1.cell(row=i1, column=3).value!=None:
                OriginData['Brand']=str(form1.cell(row=i1, column=3).value).upper()
            else:
                OriginData['Brand']=''
            if form1.cell(row=i1, column=4).value!=None:
                OriginData['Model']=str(form1.cell(row=i1, column=4).value).upper()
            else:
                OriginData['Model']=''
            OriginData['Name']=str(form1.cell(row=i1, column=5).value).upper()
            OriginData['Model_sub_and']=SplitWord(OriginData['Model'],SplitSign_And)
            OriginData['Model_sub_or']=SplitWord(OriginData['Model'],SplitSign_Or)

            ''' Step2 '''
            for i2 in range(3,form2.max_row):   #检索表2的每一行
                ''' 准备表2数据 '''
                if form2.cell(row=i2,column=1).value!=None:
                    form2_name=str(form2.cell(row=i2,column=1).value).upper()
                else:
                    form2_name=''
                if form2.cell(row=i2,column=2).value!=None:
                    form2_model=str(form2.cell(row=i2,column=2).value).upper()
                else:
                    form2_model=''
                form2_name_rip=''
                for char in range(len(form2_name)):
                    if form2_name[char] != ' ':
                        form2_name_rip += form2_name[char]

                ''' 开始检索 '''
                # 如果'型号'能匹配成功，则用'品牌+名称'匹配库存名称
                if (OriginData['Model'] in form2_model) and (OriginData['Brand'] in form2_name) and (OriginData['Name'] in form2_name):  # 判断表1的型号与表2是否匹配
                    count += 1
                    form1.cell(row=i1, column=11).value = i2
                    result[i1]=i2
                    break

                # 如果'品牌+型号+名称'与库存名称能匹配成功
                elif (OriginData['Brand'] in form2_name) and (OriginData['Model'] in form2_name) and (OriginData['Name'] in form2_name):
                    count += 1
                    form1.cell(row=i1, column=12).value = i2
                    result[i1] = i2
                    break

                # 如果'型号+名称'与库存名称能匹配成功
                elif (OriginData['Model'] in form2_name) and (OriginData['Name'] in form2_name):
                    count += 1
                    form1.cell(row=i1, column=13).value = i2
                    result[i1] = i2
                    break

                # 如果'品牌+型号'与库存名称能匹配成功
                elif (OriginData['Brand'] in form2_name) and (OriginData['Model'] in form2_name) and OriginData['Brand']!='' and OriginData['Model']!='' :
                    count += 1
                    form1.cell(row=i1, column=14).value = i2
                    result[i1] = i2
                    break

                # 拆分Model，进行组合匹配
                elif ListIn(OriginData['Model_sub_and'],form2_name_rip,'and',[]) and ((OriginData['Name'] in form2_name_rip) or (OriginData['Brand'] in form2_name_rip)):
                    count += 1
                    form1.cell(row=i1, column=16).value = i2
                    result[i1] = i2
                    break

                # 拆分Model，进行模糊匹配
                elif (ListIn(OriginData['Model_sub_or'],form2_model,'or',blackwords) or ListIn(OriginData['Model_sub_or'],form2_name_rip,'or',blackwords)) and (OriginData['Name'] in form2_name_rip):
                    count += 1
                    form1.cell(row=i1, column=17).value = i2
                    result[i1] = i2
                    break

                # 型号和品牌为空时，只匹配名称
                elif OriginData['Name'] in form2_name_rip and OriginData['Model']=='' and OriginData['Brand']=='':
                    count += 1
                    form1.cell(row=i1, column=18).value = i2
                    result[i1] = i2
                    break

                # 只匹配名称+品牌
                elif (OriginData['Name'] in form2_name_rip) and (OriginData['Brand'] in form2_name_rip):
                    count += 1
                    form1.cell(row=i1, column=19).value = i2
                    result[i1] = i2
                    break

                # 硒鼓专门匹配
                elif OriginData['Name'] == '硒鼓':
                    MatchKey = ''
                    for key in Cartridges:
                        for x in OriginData['Model_sub_or']:
                            if x in Cartridges[key]:
                                MatchKey = key
                                break
                    if (MatchKey != '') and (MatchKey in form2_model):
                        # print('MatchKey=',MatchKey,'form2Model=',form2_model)
                        count += 1
                        form1.cell(row=i1, column=15).value = i2
                        result[i1] = i2
                        break

        total=form1.max_row-2
        print('Total data:',total)
        print('Totally matched Count:', count)
        print('Match rate:',count/total)

        return result


    def CheckMatchResult(self,form):
        count=0
        for i in range(3, form.max_row):
            for j in range(11,20):
                if form.cell(row=i, column=j).value!=None:
                    count+=1
        print('Real matched count:',count)

    def CheckUnit(self,form1,form2):
        count=0
        UnitList={}
        for i in range(3, form1.max_row):
            for j in range(11, 20):
                if form1.cell(row=i, column=j).value != None:
                    form2_row=form1.cell(row=i, column=j).value
                    form1_unit=form1.cell(row=i, column=6).value
                    form2_unit=form2.cell(row=form2_row,column=3).value
                    if form1_unit==form2_unit:
                        form1.cell(row=i, column=21).value = 'unit matched'
                    else:
                        count+=1
                        form1.cell(row=i, column=21).value = 'unit Unmatched'
                        name1=str(form1.cell(row=i, column=5).value)+'_'+str(form1.cell(row=i, column=6).value)
                        name2=str(form2.cell(row=form2_row,column=3).value)
                        if name1 not in UnitList:
                            UnitList[name1]=name2
                        elif UnitList[name1]!=name2:
                            print("new unit of same name!!!!  " + name1 + ':'+ UnitList[name1] +'/'+name2)
        print('Unmatched count:',count)
        return UnitList

def SplitWord(content,symbols):
    result = []
    word = ''
    for char in range(len(content)):
        if content[char] not in symbols:
            word += content[char]
        else:
            result.append(word)
            word = ''
    if word != '':
        result.append(word)
    return result

def ListIn(origin,target,type,b_words):
    if len(origin)==0:
        return False
    elif type.lower()=='and':
        for item in origin:
            if item not in target:
                return False
        else:
            return True
    else:
        for item in origin:
            for x in b_words:
                if x in item:
                    continue
            if item in target:
                return True

class rewrite():
    """写表2！！将表1统计出的每个商品数量，写入表2"""
    def __init__(self):
        self.special_things_a=["小胶带","复印纸","胶带","宽胶带"]
        self.special_things_b=["纸箱","擦桌布"]  #都是5个一组
# 纸箱_组（5个）': '个', '（1组=5个）
# 擦桌布_包（5条）': '条', '（包=条）


# 荧光笔_个': '盒', '（型号：33111，6个=1盒）
# 小胶带_卷': '筒', '（6卷=1筒）
# 复印纸_包': '箱', '（5包=1箱）
# 胶带_卷': '筒', '（6卷=1筒）
# 宽胶带_卷': '筒', '（6卷=1筒）
#双面胶_个': '袋', '（型号：30400/30411/30412，袋=卷；型号：30401,24卷=1袋;型号:30403,12卷=1袋，）

    def statistics_a(self,form1,name,x,model="0"): #计算表1中的数量关系,参数x为换算关系
        count =0
        for i in range(3, form1.max_row):#迭代表1，统计特殊商品的总数量
            if model==0:
                if name == form1.cell(row=i,column=5).value: #没有特殊型号,直接计算累加
                    print ("222222")
                    count+=form1.cell(row=i,column=8).value
            else:
                if name == form1.cell(row=i,column=5).value and str(model) in str(form1.cell(row=i,column=4).value):
                    print ("3333")
                    count+=form1.cell(row=i,column=8).value
        if count%x !=0:
            print ("name=",name,"数量",count,"型号",model,"需要手填进入表2")
            return 0
        else:
            print ("name=",name,"数量",count,"model",model)
            return count/x



    def get_Form1_count(self,form1,row):

        things_count=form1.cell(row=row,column=8).value
        # if form1.cell(row=row,column=5).value =="荧光笔" and form1.cell(row=row,column=4).value =="33111":
        #     things_count=0
        if form1.cell(row=row,column=5).value =="双面胶" and form1.cell(row=row,column=4).value =="30401":
            things_count=0
        elif form1.cell(row=row,column=5).value =="双面胶" and form1.cell(row=row,column=4).value =="30403":
            things_count=0       
        elif form1.cell(row=row,column=5).value in self.special_things_a:
            #print ("spec_all",things_count)
            things_count=0
            #print ("spec_all",things_count)
        elif form1.cell(row=row,column=5).value in self.special_things_b:  #b里的都是5个一组，所以统一乘5
            return things_count*5
        else:
            #print ("11111",row,things_count)
            return things_count

    def rewrite_Form2_normal(self,form2,row,things_count):  #将普通商品的数量写进表2中
        form2_count=form2.cell(row=row, column=10).value
        #print ("22222222,things_count")
        #print ("form2_count_a",form2_count)
        #print (type(form2_count))
        if type(form2_count)!=type(1):
            form2_count = 0
        if type(things_count)!=type(1):
            things_count=0
           
        #print ("22222222",things_count)    
        form2_count-= int(things_count)
        form2.cell(row=row, column=10).value= form2_count
        #print ("form2_count",form2_count,"form1_count",things_count)
        return form2_count

    def rewrite_Form2_special(self,form2,name,things_count,model=0):  #需要1个查询函数，将特殊商品重写进表2中
        for i in range(3, form2.max_row):
            if model==0:
                if name==form2.cell(row=i, column=1).value:  #只找第一个
                    form2.cell(row=i, column=10).value= things_count
                    break
            else:
                if name==form2.cell(row=i, column=1).value and str(model) in str(form2.cell(row=i, column=2).value):
                    form2.cell(row=i, column=10).value= things_count
                    break
        return

    def rewrite_Form1(self,form1,form2,row_form1,row_form2):#将表2的名称复写进表1
        red_fill = PatternFill("solid", fgColor="FF0000")
        form1.cell(row=row_form1, column=5).value=form2.cell(row=row_form2, column=1).value  #表2的名称复写进表1
        form1.cell(row=row_form1, column=6).value=form2.cell(row=row_form2, column=3).value  #表2的单位复写进表1
        form1.cell(row=row_form1, column=5).fill=red_fill  #给复写的名称设置一个颜色
        form1.cell(row=row_form1, column=6).fill=red_fill  #给复写的单位设置一个颜色
        return 



    def main(self,matched_result,form1,form2): 
        for form1_row,form2_row in matched_result.items():
            res=self.rewrite_Form2_normal(form2,row=form2_row,things_count=self.get_Form1_count(form1,form1_row))  #将表1数量，根据查询结果，写进表1
            self.rewrite_Form1(form1,form2,row_form1=form1_row,row_form2=form2_row)
            #print (form1_row,form2_row,res)
        #############开始全局计算特殊商品的总数量，并复写form2
        #yin_guang_bi=self.statistics_a(form1,"荧光笔",6,"33111")  #33111的型号量词是正确的，不用单独考虑了
        xiao_jiao_dai=self.statistics_a(form1,"小胶带",6,"30029")
        fu_yin_zhi=self.statistics_a(form1,"复印纸",5)
        jiao_dai=self.statistics_a(form1,"胶带",6)
        kuai_jiao_dai=self.statistics_a(form1,"宽胶带",6)
        shuang_mian_jiao_30401=self.statistics_a(form1,"双面胶",24,"30401")
        shuang_mian_jiao_30403=self.statistics_a(form1,"双面胶",12,"30403")
        ##############计算完成，复写form2
        #self.rewrite_Form2_special(form2,"荧光笔",yin_guang_bi,model="33111")  #33111的型号是对应的，不用单独考虑了
        self.rewrite_Form2_special(form2,"小胶带",xiao_jiao_dai)
        self.rewrite_Form2_special(form2,"复印纸",fu_yin_zhi)
        self.rewrite_Form2_special(form2,"胶带",jiao_dai)
        self.rewrite_Form2_special(form2,"宽胶带",kuai_jiao_dai)
        self.rewrite_Form2_special(form2,"双面胶",shuang_mian_jiao_30401)
        self.rewrite_Form2_special(form2,"双面胶",shuang_mian_jiao_30403)


        

if __name__=='__main__':
    FP=FormProcessor()
    FP.BackupFile(Form1Path, 'Form1.xlsx')
    FP.BackupFile(Form2Path, 'Form2.xlsx')
    Form1Path = FileDirectory + 'Form1.xlsx'
    Form2Path = FileDirectory + 'Form2.xlsx'
    print(Form1Path)
    print(Form2Path)
    time.sleep(1)
    FP.wb1 = FP.GetFile(Form1Path)
    FP.Form1=FP.GetForm(FP.wb1 , '3月-6月（机关汇总表）')
    FP.wb2 = FP.GetFile(Form2Path)
    FP.Form2=FP.GetForm(FP.wb2,'Sheet1')
    # FP.CheckForm(FP.Form1, FP.Form2)
    result=FP.CheckFormOnce(FP.Form1,FP.Form2)
    UnmatchList=FP.CheckUnit(FP.Form1,FP.Form2)
    FP.FormSave(FP.wb1,"NewForm1.xlsx")
    FP.CheckMatchResult(FP.Form1)
    #**************************
    #写form1和fomr2
    rewrite().main(result,FP.Form1,FP.Form2)
    FP.FormSave(FP.wb2,"NewForm2.xlsx")
    FP.FormSave(FP.wb1,"Result_Form2.xlsx")
    #print('result=',result)
    #print('UnmatchUnit=',UnmatchList)





