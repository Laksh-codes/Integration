import requests
import re
class Request:
    #URL 
    def __init__(self):
        self.url = ""
        print("URL Tracked.")
    
    #SAVING RESPONSE
    def taking_response(self):
        response = requests.request('GET', self.url)
        self.data = response.text
        print("Data.")

    #EXTRACT ID'S
    def extract_id(self):
        pattern = r""
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
