from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://brightdata.com/blog/how-tos/web-scraping-with-python?kw=&cpn=14745430544&cam=aw_blog_dynamic__547760284460&utm_term=&utm_campaign=blog&utm_source=adwords&utm_medium=ppc&utm_content=dynamic&hsa_acc=1393175403&hsa_cam=14745430544&hsa_grp=131242020607&hsa_ad=547760284460&hsa_src=g&hsa_tgt=dsa-39587879683&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiAlrSPBhBaEiwAuLSDUKQnfVG2edzMTxYu1U2UpvdNfP0HFs4AkgG0HRkzPrDSi6hI2TfSLRoCr4oQAvD_BwE')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")

    text = soup.find('div', class_='brd_blog_entry').text.split('\n')
    text=[i for i in text if i]
    text.pop()
    text= ''.join(text)
    text= text.replace('www.kayak.com/robot.txt','""kayak.com/robot.txt""').title()
    print(text)

except Exception as e:
    print(e)