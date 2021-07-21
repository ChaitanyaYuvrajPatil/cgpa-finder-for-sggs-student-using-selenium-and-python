from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from subject_library import *

ops = Options()
ops.headless = True
Reg_No = ''
Semister_ = ''

M_Grade = ''
not_found = ''
Sub_Grade = { }

def Chage(reg,sem) :
    global Reg_No,Semister_,Sub_Grade
    Reg_No = reg
    Semister_ = sem
    Sub_Grade = { }

branches = {'bch' : 'Chem','bce': 'Civil','bcs' : 'Cse','bel':' Elec','bec':'Extc',
            'bit' : 'IT','bin' :'Instru','bme' :'Mech','bpr' :'Prod','btt' :'Textile' }

#for gpa
Semister_selection_for_gpa = {'Semister 1':'1','Semister 2':'2','Semister 3':'3','Semister 4':'4',
                              'Semister 5':'5','Semister 6':'6','Semister 7':'7','Semister 8':'8'}
Branch_selection = { 'It' : '2','Instru': '3','Mech': '4','Civil': '5','Elec': '6','Extc': '7',
                     'Chem': '8',"Textile": '9',"Cse": '10','Prod': '11' }


#for grades (select by value)
Semister_selection_for_grades = {'Semister 1':'2','Semister 2':'3','Semister 3':'4','Semister 4':'5','Semister 5':'6',
                         'Semister 6':'7','Semister 7':'8','Semister 8':'9'}


def get_branch_from_reg_no(Reg_No):
    reg = Reg_No.lower()
    reg = reg[4:7]
    if(reg == 'bch'):
        return 'Chem'
    if (reg == 'bce'):
        return 'Civil'
    if (reg == 'bcs'):
        return 'Cse'
    if (reg == 'bel'):
        return 'Elec'
    if (reg == 'bec'):
        return 'Extc'
    if (reg == 'bit'):
        return 'It'
    if (reg == 'bin'):
        return 'Instru'
    if (reg == 'bme'):
        return 'Mech'
    if (reg == 'bpr'):
        return 'Prod'
    if (reg == 'btt'):
        return 'Textile'



def get_grades(browser):
    global not_found,Reg_No,Semister_
    browser.get('https://onlinesggs.org/app/web/index.php')
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/input').send_keys(Reg_No.lower()+"@sggs.ac.in")
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/input').send_keys(Reg_No.upper())
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[3]/input').click()

    browser.find_element_by_xpath('//*[@id="status"]/option[2]').click()
    browser.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[2]/select/option['+Semister_selection_for_grades[Semister_]+']').click()

    browser.find_element_by_xpath('//*[@id="wrapper"]/form/center/input').click()

    try:
        '''if browser.find_element_by_xpath('/html/body/div[3]/ul/li[1]/center/text()').text == 'Result Not Found':
            not_found = 'Result Not Found'
            print("Not found")'''
        range2 = 15
        '''if Reg_No[4:7].lower() == 'bcs' and Semister_ == 'Semister 3':
            range2 = 14'''
        for i in range(1, range2):
            sub = browser.find_element_by_xpath(
                '/html/body/div[3]/ul/li[' + str(i) + ']/table/tbody/tr/td[' + str(1) + ']').text
            grade = browser.find_element_by_xpath(
                '/html/body/div[3]/ul/li[' + str(i) + ']/table/tbody/tr/td[' + str(2) + ']').text
            Sub_Grade[str(sub)] = str(grade)
    except:
        #print('Not Fonnd')
        pass
    print(Sub_Grade)
    return Sub_Grade

    '''if Sub_Grade['em3273Th'] == '??' :
        Sub_Grade['em3273Th'] = m3_marks()'''

def get_cgpa(browser):
    global Reg_No,Semister_
    browser.get('https://vishalibitwar.github.io/gpacalculator/')
    # branch selection
    browser.find_element_by_xpath(
        '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/select/option[' + Branch_selection[get_branch_from_reg_no(Reg_No)] + ']').click()
    # semister selection
    browser.find_element_by_xpath(
        '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/select/option[' + Semister_selection_for_gpa[Semister_] + ']').click()
    branch_semister_no_subject = str(get_branch_from_reg_no(Reg_No)).lower()+'_Semister_'+str(Semister_[9])+'_subjects'

    for i in Branch_set_dictionary[str(get_branch_from_reg_no(Reg_No)).lower()][branch_semister_no_subject]:  #we here
        name = Select(browser.find_element_by_name(Branch_set_dictionary[str(get_branch_from_reg_no(Reg_No)).lower()][branch_semister_no_subject][i]))
        name.select_by_visible_text(Sub_Grade[i])

    browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/button').click()
    sco = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/h1').text
    print(str(sco)[0:4])
    return str(sco)[0:4]

def m3_marks():
    global M_Grade,ops
    browser_M.get('https://onlinesggs.org/app/web/index.php')
    browser_M.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/input').send_keys(Reg_No.lower()+"@sggs.ac.in")
    browser_M.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/input').send_keys(Reg_No.upper())
    browser_M.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[3]/input').click()

    browser_M.find_element_by_xpath('//*[@id="status"]/option[2]').click()
    browser_M.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[2]/select/option[15]').click()
    browser_M.find_element_by_xpath('//*[@id="wrapper"]/form/center/input').click()
    mark = browser_M.find_element_by_xpath('/html/body/div[3]/ul/li[1]/table/tbody/tr/td[2]').text
    M_Grade = mark


    #return str(mark)
def m4_marks():
    global M_Grade
    browser_M.get('https://onlinesggs.org/app/web/index.php')
    browser_M.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/input').send_keys(Reg_No.lower()+"@sggs.ac.in")
    browser_M.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/input').send_keys(Reg_No.upper())
    browser_M.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[3]/input').click()

    browser_M.find_element_by_xpath('//*[@id="status"]/option[2]').click()
    browser_M.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[2]/select/option[16]').click()
    browser_M.find_element_by_xpath('//*[@id="wrapper"]/form/center/input').click()
    mark = browser_M.find_element_by_xpath('/html/body/div[3]/ul/li[1]/table/tbody/tr/td[2]').text
    M_Grade = mark

#==============================================Main=========================================

def main_Fun() :
    global browser_M, ops
    browser = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)  #
    grade = get_grades(browser)

    if 'em3273Th' in Sub_Grade:
        if Sub_Grade['em3273Th'] == '??' or Sub_Grade['em3271Th'] == '??':
            browser_M = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)
            m3_marks()
            Sub_Grade['em3273Th'] = M_Grade

    if 'em3271Th' in Sub_Grade:
        if Sub_Grade['em3271Th'] == '??':
            browser_M = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)
            m3_marks()
            Sub_Grade['em3271Th'] = M_Grade

    if 'em3272Th' in Sub_Grade:
        if Sub_Grade['em3272Th'] == '??':
            browser_M = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)
            m3_marks()
            Sub_Grade['em3272Th'] = M_Grade

    if 'm4276Th' in Sub_Grade:
        if Sub_Grade['m4276Th'] == '??':
            browser_M = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)
            m4_marks()
            Sub_Grade['m4276Th'] = M_Grade

    if 'm4274Th' in Sub_Grade:
        if Sub_Grade['m4274Th'] == '??':
            browser_M = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)
            m4_marks()
            Sub_Grade['m4274Th'] = M_Grade

    if 'em4371_2Th' in Sub_Grade:
        if Sub_Grade['em4371_2Th'] == '??':
            browser_M = webdriver.Chrome(executable_path="C:\\Users\\mypc\\Downloads\\driver\\chromedriver.exe",options=ops)
            m4_marks()
            Sub_Grade['em4371_2Th'] = M_Grade

    for j in Sub_Grade:
        print(j + " : " + Sub_Grade[j])

    cgpa = get_cgpa(browser)
    return grade,cgpa

#main_Fun()








