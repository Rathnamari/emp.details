class emp:
  def _init_ (self,Name,Company_Name,Salary,Id,DOB,Branch,Location,Aadhar):
    self.ne = Name
    self.ce = Company_Name
    self.sy = Salary
    self.id = Id
    self.dob = DOB
    self.bh = Branch
    self.ln = Location
    self.aad = Aadhar
class tcs(emp):   # tcs Input format("Name","Company_Name","Salary","Id","DOB","Branch","Location","Aadar or None")
  def salary_format(self):
    self.sy = "{:.2f}".format(self.sy)
  def show(self):
    print("Name - ",self.ne,"\nCompany name - ",self.ce,"\nSalary - ",self.sy,"\nid no. - ",self.id,"\nDOB - ",self.dob,"\nbranch - ",self.bh,"\nlocation - ",self.ln,self.aad)

class hcl(emp):
  def Salary_Format(self):
    self.id = self.id - ((self.id*10)/100)
  def update(self,first_name):
    self.ne = first_name
  def update(self,last_name):
    self.ce = last_name
  def update(self,company_name):
    self.sy = company_name
  def update(self,salary):
    self.id = salary
  def update(self,id):
    self.dob = id
  def update(self,gender):
    self.bh = gender
  def update(self,bloodgroup):
    self.ln = bloodgroup
  def update(self,doj):
    self.aad = doj
  def show(self):
    print("First name-",self.ne,"\nLast name - ",self.ce,"\ncompany name - ",self.sy,"\nsalary - ",self.id,"\nid no. - ",self.dob,"\ngender - ",self.bh,"\nbloodgroup - ",self.ln,"\nDOJ - ",self.aad)
class infosys(emp):
  def salary_Format(self):
    self.sy = self.sy*12
  def update(self,experience):
    self.dob = experience
  def update(self,mobile_number):
    self.bh = mobile_number
  def update(self,address):
    self.ln = address
  def show(self):
    print("Name",self.ne,"\ncompany name -",self.ce,"\nSalary - ",self.sy,"\nid no. - ",self.id,"\nexperience - ",self.dob,"\nmobile number - ",self.bh,"\naddress - ",self.ln,"\naadhar - ",self.aad)
print("TCS emp. details")
e1 = tcs("rathna","tcs",25000,5,"26.03.2020","siruseri","chennai","None")  
e1.salary_format()
e1.show()
print("--------------------------")
print("HCL emp. details")
e2 = hcl("chocka","lingam","hcl",30000,26,"male","B+ive","05.6.2023")
e2.Salary_Format()
e2.show()
print("--------------------------")
print("Infosys emp. details")
e3 = infosys("sangeetha","infosys",30000,27,"3 yrs",9524723113,"18 Suthamali,Tirunelveli",123456789)
e3.salary_Format()
e3.show()
