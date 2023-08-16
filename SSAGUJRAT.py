from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

# driver Chrome
driver = webdriver.Chrome()

# getwebsite
driver.get("http://ssgujarat.org/CTELogin.aspx")

# pop up closed
popup = driver.find_element("css selector", ".closei")
if popup.is_displayed():
    popup.click()

# username & password
username_field = driver.find_element("css selector", "#TxtUName")
password_field = driver.find_element("css selector", "#TxtUPass")

username_field.send_keys("24250303803")
password_field.send_keys("N@1234")
time.sleep(10)

# write a caption
password_field.send_keys(Keys.RETURN)
time.sleep(1)

# pop up of students
try:
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    time.sleep(5)
except:
    pass

# go to managestudent
manage_student = driver.find_element("css selector", "#ctl00_ManageStudent")
manage_student.send_keys(Keys.ENTER)
time.sleep(5)

# go to class 2
class_2_student = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_GridView1_ctl02_LinkButton2")
class_2_student.click()
time.sleep(5)

# new windoe handoler

# Get the window handles
window_handles = driver.window_handles

# Switch to the newly opened tab
new_tab_handle = window_handles[-1]
driver.switch_to.window(new_tab_handle)


# take data from xls file
dataframe = pd.read_excel("D:\MOM\STD2_students.xlsx", dtype=object)

# student G.R.No  for first 5 students
#-1
grnumber_from_web_1 = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_grno")
grnumber_for_file_1 = grnumber_from_web_1.get_attribute("value")
print(grnumber_for_file_1)
print(type(grnumber_for_file_1))
time.sleep(5)

# get sepecific student data only
selected_rows_1 = dataframe[dataframe["GRNo"] == int(grnumber_for_file_1)]

time.sleep(3)

# filling datas

# wait

#rollno   
#-2              
roll_no = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_rollno")
roll_no.send_keys(selected_rows_1["Roll No."].values[0])
time.sleep(1)

#-7
# fathername same as givan
fname = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_fname")
GuardiansName = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_GuardiansName")
GuardiansName.send_keys(fname.get_attribute("value"))
time.sleep(1)

#-9.4
# HOUSENUMBER   if not add 0
# HouseNo = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_Address_HouseNo")
# HouseNo.send_keys(selected_rows_1["ADD"].values[0])
# time.sleep(1)

#-9.5
# addreace
SocietyName = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_Address_SocietyName")
SocietyName.send_keys(selected_rows_1["ADD"].values[0])
time.sleep(1)

#-9.6
Address_Landmark = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_Address_Landmark")
Address_Landmark.send_keys("MANDA")
time.sleep(1)

#-9.7
Address_Area = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_Address_Area")
Address_Area.send_keys(selected_rows_1["ADD"].values[0])
time.sleep(1)

#-9.8
Pincode = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_Pincode")
Pincode.send_keys("396155")
time.sleep(1)

#-17
AatharId = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_AatharId")
AatharId.clear()
alert = wait.until(EC.alert_is_present())
alert.accept()
print(selected_rows_1["આધાર નંબર"].values[0])
AatharId.send_keys(selected_rows_1["આધાર નંબર"].values[0])
time.sleep(1)

#-18
# adahrname 
# StudentNameAsPerAadhaarID = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_StudentNameAsPerAadhaarID")
# StudentNameAsPerAadhaarID.send_keys(selected_rows_1["આધાર name"].values[0])
# time.sleep(1)

#ddlAntyodayaAnnaYojanaBeneficiary (drop down)
from selenium.webdriver.support.ui import Select

#-22
ddlAntyodayaAnnaYojanaBeneficiary = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlAntyodayaAnnaYojanaBeneficiary")
drop_ddlAntyodayaAnnaYojanaBeneficiary = Select(ddlAntyodayaAnnaYojanaBeneficiary)
# if selected_rows_1["આધાર name"].values[0] == '0':
# drop_ddlAntyodayaAnnaYojanaBeneficiary.select_by_value("1")
# if selected_rows_1["આધાર name"].values[0] == '1':
drop_ddlAntyodayaAnnaYojanaBeneficiary.select_by_value("2")
time.sleep(1)

#-28
# atendeance and result 
ddlIfClass1StatusofPrvYear = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlIfClass1StatusofPrvYear")
drop_ddlIfClass1StatusofPrvYear = Select(ddlIfClass1StatusofPrvYear)
drop_ddlIfClass1StatusofPrvYear.select_by_value("1")
time.sleep(5)

#-30
# DaysAttendedPrvYear = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txt_DaysAttendedPrvYear")
# DaysAttendedPrvYear.clear()
# try:
#     alert = wait.until(EC.alert_is_present())
#     alert.accept()
# except:
#     pass
# DaysAttendedPrvYear.send_keys(selected_rows_1["ADD"].values[0])
# time.sleep(1)

#-31
#apprered
ddlAppeared = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlAppeared")
drop_ddlAppeared = Select(ddlAppeared)
drop_ddlAppeared.select_by_value("1")
time.sleep(5)

#-32
ddlResultOfLastExamination = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlResultOfLastExamination")
drop_ddlResultOfLastExamination = Select(ddlResultOfLastExamination)
drop_ddlResultOfLastExamination.select_by_value("1")
time.sleep(5)

#-33
# txtmarksobtained = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_txtmarksobtained")
# txtmarksobtained.send_keys(selected_rows_1["આધાર name"].values[0])

#41
ddlCheckup_Specific_Learning_Disability = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlCheckup_Specific_Learning_Disability")
drop_ddlCheckup_Specific_Learning_Disability = Select(ddlCheckup_Specific_Learning_Disability)
drop_ddlCheckup_Specific_Learning_Disability.select_by_value("2")
time.sleep(5)

#42
ddlCheckup_Autism_Spectrum_Disorder = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlCheckup_Autism_Spectrum_Disorder")
drop_ddlCheckup_Autism_Spectrum_Disorder = Select(ddlCheckup_Autism_Spectrum_Disorder)
drop_ddlCheckup_Autism_Spectrum_Disorder.select_by_value("2")
time.sleep(5)

#43
ddlCheckup_Attention_Deficit_Hyperactive_Disorder = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlCheckup_Attention_Deficit_Hyperactive_Disorder")
drop_ddlCheckup_Attention_Deficit_Hyperactive_Disorder = Select(ddlCheckup_Attention_Deficit_Hyperactive_Disorder)
drop_ddlCheckup_Attention_Deficit_Hyperactive_Disorder.select_by_value("2")
time.sleep(5)

#44
ContentPlaceHolder1_studentdata_ctl00_ddlIncentive_Benefits_Facilities_Provided_Child = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlIncentive_Benefits_Facilities_Provided_Child")
drop_ContentPlaceHolder1_studentdata_ctl00_ddlIncentive_Benefits_Facilities_Provided_Child = Select(ContentPlaceHolder1_studentdata_ctl00_ddlIncentive_Benefits_Facilities_Provided_Child)
drop_ContentPlaceHolder1_studentdata_ctl00_ddlIncentive_Benefits_Facilities_Provided_Child.select_by_value("2")
time.sleep(5)

#45
ddlSetofFreeTextbooks = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlSetofFreeTextbooks")
drop_ddlSetofFreeTextbooks = Select(ddlSetofFreeTextbooks)
drop_ddlSetofFreeTextbooks.select_by_value("1")
time.sleep(5)

#46
ddlSetofFreeUniform = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlSetofFreeUniform")
drop_ddlSetofFreeUniform = Select(ddlSetofFreeUniform)
drop_ddlSetofFreeUniform.select_by_value("0")
time.sleep(5)

#47
ddlFreeTransportFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeTransportFacility")
drop_ddlFreeTransportFacility = Select(ddlFreeTransportFacility)
drop_ddlFreeTransportFacility.select_by_value("0")
time.sleep(5)

#48
ddlFreeEscortFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeEscortFacility")
drop_ddlFreeEscortFacility = Select(ddlFreeEscortFacility)
drop_ddlFreeEscortFacility.select_by_value("0")
time.sleep(5)

#49
ddlMDMBeneficiery = driver.find_element("css selector", "#id=ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlMDMBeneficiery")
drop_ddlMDMBeneficiery = Select(ddlMDMBeneficiery)
drop_ddlMDMBeneficiery.select_by_value("1")
time.sleep(5)

#50
ddlFreeHostelFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeHostelFacility")
drop_ddlFreeHostelFacility = Select(ddlFreeHostelFacility)
drop_ddlFreeHostelFacility.select_by_value("0")
time.sleep(5)













#51
ddlFreeHostelFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeHostelFacility")
drop_ddlFreeHostelFacility = Select(ddlFreeHostelFacility)
drop_ddlFreeHostelFacility.select_by_value("0")
time.sleep(5)

#52
ddlFreeHostelFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeHostelFacility")
drop_ddlFreeHostelFacility = Select(ddlFreeHostelFacility)
drop_ddlFreeHostelFacility.select_by_value("0")
time.sleep(5)

#53
ddlFreeHostelFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeHostelFacility")
drop_ddlFreeHostelFacility = Select(ddlFreeHostelFacility)
drop_ddlFreeHostelFacility.select_by_value("0")
time.sleep(5)

#54
ddlFreeHostelFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeHostelFacility")
drop_ddlFreeHostelFacility = Select(ddlFreeHostelFacility)
drop_ddlFreeHostelFacility.select_by_value("0")
time.sleep(5)

#55
ddlFreeHostelFacility = driver.find_element("css selector", "#ctl00_ContentPlaceHolder1_studentdata_ctl00_ddlFreeHostelFacility")
drop_ddlFreeHostelFacility = Select(ddlFreeHostelFacility)
drop_ddlFreeHostelFacility.select_by_value("0")
time.sleep(5)



# quit window
time.sleep(50)
driver.quit()
