





import requests
import ssl

course_code = "ECE212"
url = "https://coursefinder.utoronto.ca/course-search/search/courseInquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId="+ course_code + "H1F20219";


def getContent(url):
    # headers = {
    #     'Accept': 'application/json',
    #     'Referer': url,
    #     'Origin': url,
    #     'Host' : "coursefinder.utoronto.ca",
    #     'P': '45673084486',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    #     'Content-Type': 'application/json;charset=UTF-8',
    # }

#     headers ={ 
# 'Host': "coursefinder.utoronto.ca",
# 'Connection': "keep-alive",
# 'sec-ch-ua': "'Google Chrome';v='95', 'Chromium';v='95', ';Not A Brand';v='99'",
# 'Accept': "application/json, text/javascript, */*; q=0.01",
# 'X-Requested-With': "XMLHttpRequest",
# 'sec-ch-ua-mobile': "?0",
# 'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
# 'sec-ch-ua-platform': "macOS",
# 'Sec-Fetch-Site': "same-origin",
# 'Sec-Fetch-Mode': "cors",
# 'Sec-Fetch-Dest': "empty",
# 'Referer': "https://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start",
# 'Accept-Encoding': "gzip, deflate, br",
# 'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
# 'Cookie': "kualiSessionId=2cbdc1e0-776d-45d5-85fa-134a3a08d821; JSESSIONID=46DF3950CF13C2765C5120417A73BB1B.w2; _gid=GA1.2.1662931369.1636176437; _ga_EFR987QNL1=GS1.1.1636209296.1.1.1636209311.0; _ga=GA1.2.950053206.1636176437; __utmc=264236318; __utmz=264236318.1636230107.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=264236318.950053206.1636176437.1636242297.1636246382.5; __utmt=1; __utmb=264236318.2.10.1636246382",
#     }

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    response = requests.request("GET",url, headers=hdr)

    # response = requests.request("GET", url, headers=headers)
    return response.content
  
print (getContent(url))
