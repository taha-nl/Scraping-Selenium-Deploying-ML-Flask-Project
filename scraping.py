import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import re
import csv
from itertools import zip_longest




if __name__=='__main__':
    
    browser=uc.Chrome()

    browser.maximize_window()
    time.sleep(3)
    for i in range(1,14):
        try:

                URL=f"https://www.glassdoor.com/Job/san-francisco-data-scientist-jobs-SRCH_IL.0,13_IC1147401_KO14,28_IP{i}.htm?includeNoSalaryJobs=true&pgc=AB4ABIEAeAAAAAAAAAAAAAAAAfgJYmIAawEDASBaCRYHHwFZknTETS4gASB3iipZ7OP60ekum4F4nmdwTKKFWCbOL%2F6KJ2530%2BtOKQoqk%2F0rHqZb4p6yCaSWsFMGBF4bmyTMZ3VqxCLZfyTjTDVOZcI%2B1RDoxj02chJCcrfuFA4h2gp4AAA%3D"


                browser.get(URL)
                time.sleep(2)
                try:
                        browser.find_element(By.XPATH,('//span[@alt="Close"]')).click() #clicking to the X.
                        print(' x out worked')
                except:
                        pass
                time.sleep(1)
                

                job_titles=browser.find_elements(By.XPATH,('//a[@class="jobLink css-1rd3saf eigr9kq2"]/span'))
                company_names=browser.find_elements(By.XPATH,('//a[@class=" css-l2wjgv e1n63ojh0 jobLink"]/span'))
                rating_zones=browser.find_elements(By.XPATH,('//div[@class="d-flex flex-column css-x75kgh e1rrn5ka3"]'))
                headquarters=browser.find_elements(By.XPATH,('//span[@data-test="emp-location"]'))
                salary=browser.find_elements(By.XPATH,('//span[@data-test="detailSalary"]'))
                links=browser.find_elements(By.XPATH,('//a[@class="jobLink css-1rd3saf eigr9kq2"]'))

                

                job_titles_text=[job.text for job in job_titles]
                company_names_text=[company_name.text for company_name in company_names]
                headquarters_text=[headquarter.text for headquarter in headquarters]
                salary_text=[salaire.text for salaire in salary[:-1]]
                rating_text=[]
                job_description=[]
                size_company=[]
                founded=[]
                type=[]
                industry=[]
                sector=[]
                revenue=[]

                
                for rating in rating_zones:
                        try:
                                rating_text.append(rating.find_element(By.XPATH,('span')).text)
                        except:
                                rating_text.append('nan')


                for link in links:
                        link.click()
                        time.sleep(2)
                        try:
                                browser.find_element(By.XPATH,('//span[@alt="Close"]')).click() #clicking to the X.
                                print(' x out worked')
                        except:
                                pass
                        time.sleep(1)
                        job_description.append(browser.find_element(By.XPATH,('//div[@class="jobDescriptionContent desc"]')).text[:100].strip())
                        try:
                                size_company.append(browser.find_element(By.XPATH,('(//div[@class="d-flex flex-wrap"]/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]/span)[2]')).text)
                        except:
                                size_company.append("nan") 
                        try:               
                                founded.append(browser.find_element(By.XPATH,('(//div[@class="d-flex flex-wrap"]/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]/span)[4]')).text)
                        except:
                                founded.append('nan')
                        try:        
                                type.append(browser.find_element(By.XPATH,('(//div[@class="d-flex flex-wrap"]/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]/span)[6]')).text)
                        except:
                                type.append("nan")
                        try:
                                industry.append(browser.find_element(By.XPATH,('(//div[@class="d-flex flex-wrap"]/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]/span)[8]')).text)
                        except:
                                industry.append("nan")
                        try:
                                sector.append(browser.find_element(By.XPATH,('(//div[@class="d-flex flex-wrap"]/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]/span)[10]')).text)
                        except:
                                sector.append("nan")
                        try:
                                revenue.append(browser.find_element(By.XPATH,('(//div[@class="d-flex flex-wrap"]/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]/span)[12]')).text)
                        except:
                                revenue.append("nan")


                info= [job_titles_text, salary_text, job_description, rating_text,company_names_text,headquarters_text, size_company, founded,type,industry,sector,revenue]
                B_data = zip_longest(*info)
                with open('glassdoor_jobs.csv', 'a') as myFile:
                        wr = csv.writer(myFile)
                        if i==1:
                                wr.writerow(["Job Title", "Salary Estimate", "Job Description", "Rating","Company Name", "Location",
                                "Size_company", "Founded", "Type of ownership","Industry","Sector","Revenue"])
                        wr.writerows(B_data)

                time.sleep(2)
                try:
                        browser.find_element(By.XPATH,('//span[@alt="Close"]')).click() #clicking to the X.
                        print(' x out worked')
                except:
                        pass
                time.sleep(2)

        except:
                pass