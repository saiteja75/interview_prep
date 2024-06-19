'''
We need to develop a Feature where we need to add some Invoice and delete the invoices, generate reports and email reports
Solutions: This feature can be developed in many ways, mentioning some below:
Approach 1: Developing both the features in a single place
Approach 2: Break Down the Feature into multiple parts where each part does one job
•	One Class for add and remove invoice
•	One Class for generating Report
•	Once Class for Sending email of report

'''

# Developing both the features in a single place
class Invoice:
    def __init__(self) -> None:
        self.invoices = []

    def addInvoice(self,invoice):
        self.invoices.append(invoice)

    def deleteInvoice(self,invoice):
        self.invoices.remove(invoice)

    def generateReport(self):
        return self.invoices
    
    def emailReport(self):
        print(self.invoices)


# Breaking the class for each feature
class Invoice:
    def __init__(self) -> None:
        self.invoices = []

    def addInvoice(self,invoice):
        self.invoices.append(invoice)

    def deleteInvoice(self,invoice):
        self.invoices.remove(invoice)

class Report:
    def __init__(self,invoices) -> None:
        self.invoices = invoices
    
    def generateReport(self):
        return self.invoices
    
class Email:
    def __init__(self,data) -> None:
        self.data = data

    def sendEmail(self):
        print(self.data)