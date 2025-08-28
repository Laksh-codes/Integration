import requests
import re
class Request:
    #URL 
    def __init__(self):
        self.url = "https://asiapacificbreweriestest.agiloft.com/ewws/EWSearch?$KB=Asia Pacific Breweries Test&$table=contract&$login=Admin1&$password=Integration@2025&$lang=en&search=Active%20BSA%20Contracts&field=id"
        print("URL Tracked.")
    
    #SAVING RESPONSE
    def taking_response(self):
        response = requests.request('GET', self.url)
        self.data = response.text
        print("Data.")

    #EXTRACT ID'S
    def extract_id(self):
        pattern = r"(REST_[a-zA-Z0-9_]+)\s*=\s*'([^']+)';"
        self.final = []
        mat = re.findall(pattern, self.data)

        for i, j in mat:
            self.final.append(int(j))
        print("Data Extracted.")
        return self.final

#FUNCTION   
req = Request()
req.taking_response()
final = req.extract_id()
print(final)