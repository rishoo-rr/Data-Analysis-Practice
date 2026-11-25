import numpy as np
import pandas as pd 

df = pd.DataFrame([1,2,3,4,5], columns = ["num"]) 

rr = pd.DataFrame([["rishabh", 17, 50000], ["ruhani", 19, 100000]], columns = ["Name", "age", "salary"])

data = {
    "name" : ["rishabh", "nitesh", "ruhani", "shubham"],
    "age" :  [17, 18, 19, 20],
    "city" : ["delhi", "prayagraj", "banglor", "prayagraj"],
    "marks" : [33, 44, 92, 75],
    "salary" : [90000, 70000, 50000, 30000]         
}

df = pd.DataFrame(data)

print(df)

print(df.head(2))
print(df.tail())

print(df.shape)

print(df.columns)

df.rename(columns = {"salary" : "monthly_salary"}, inplace = True)
df.rename(columns = {"monthly_salary" : "salary"}, inplace = True)

print(df.info())
print(df.describe())

df.to_csv("test.csv", index = False)
rr = pd.read_csv(r"C:\Users\Rishu\Downloads\Telegram Desktop\order_items.csv")

print(rr)

print(rr.shape)
print(df.shape)

print(rr[["OrderID"]])

print(df[["name", "city", "salary"]])
print(df)

print(df.loc[(df.name == "rishabh") & (df.salary >= 50000)])

print(df.iloc[0 : 2])

print(df[(df["age"] >= 18) & (df["salary"] >= 70000)])

print(df.where((df["age"] >= 18) & (df["salary"] >= 70000), other = 0))

df["team"] = ['CEO', 'HR', 'CTO', 'DA']


students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Amit", "Priya", "Rahul", "Sneha", "Karan",
        "Neha", "Rohit", "Pooja", "Anjali", "Vikas"
    ],
    "Branch": [
        "CSE", "ECE", "CSE", "IT", "ME",
        "CSE", "ECE", "IT", "EEE", "CSE"
    ],
    "Marks": [82, 91, 68, 88, 76, 95, 79, 72, 85, 74],
    "Attendance": [85, 92, 78, 90, 88, 96, 83, 95, 86, 75],
    "Backlogs": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Placement_Training": [
        "Yes", "Yes", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "Yes", "No"
    ]
})
students.head()
students.tail(3)
print(students.info())
print(students.shape)
print(list(students))
print(students.describe())
students.iloc[:, 1:5]
students[(students["Marks"] >= 75) & (students["Attendance"] >= 80)]
students[students["Branch"].isin(["CSE", "IT", "ECE"])]
students[students["Backlogs"] == 0]
eligible = students[students["Placement_Training"] == "Yes"].iloc[:3]
avg = eligible["Marks"].mean()
eligible[eligible["Marks"] > avg]


students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha"],
    "Python": [80, 95, 45, 70, 30, 88],
    "SQL": [75, 90, 50, 65, 40, 92],
    "Statistics": [85, 92, 40, 80, 35, 90],
    "Attendance": [90, 95, 65, 80, 55, 98],
    "Branch": ["CSE", "IT", "CSE", "ECE", "ME", "IT"]
})
students["Acadmic_year"] = 2026
students["Mentor"] = ["Amit", "Neha", "Priya", "Rahul", "Ruhani", "Nitesh"]
students["total_marks"] = students["Python"] + students["SQL"] + students["Statistics"]
students["Percentage"] = round(students["total_marks"]/3, 2)
students["Average"] = round(students[["Python", "SQL", "Statistics"]].mean(axis =1), 2)
students["Average"] = students[["Python", "SQL", "Statistics"]].mean()
df = students[students["Python"] > students["SQL"]]
df["how_much"] = df["Python"] - df["SQL"]
students[["Python"]] = students[["Python"]] + 5
students["Python"] = np.where(students["Python"] <= 95, students["Python"] + 5, 100)


data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [55000, 700, 1500, 12000, 2500],
    "Stock": [10, 100, 50, 15, 25]
}

products = pd.DataFrame(data)

products[products["Price"] < 2000]
products[products["Stock"] < 20]
products[products["Category"] == "Electronics"]
products["Total_amount"] = products["Price"] * products["Stock"]
products[products["Stock"] < 20][["Product", "Stock"]]
products["percentage"] = round((products["Total_amount"]/(products["Total_amount"].sum())) * 100, 2)


sales = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard", "Printer"],
    "Quantity": [5, 20, 4, 10, 3],
    "Unit_Price": [50000, 800, 12000, 1500, 18000],
    "Cost": [220000, 10000, 40000, 10000, 45000]
})
sales["revenue"] = sales["Quantity"] * sales["Unit_Price"]
sales["profit"] = sales["revenue"] - sales["Cost"]
sales["category"] = np.where(sales["profit"] >= 5000, "high profit", "standard profit")


students = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Python": [85, 95, 45, 70, 55],
    "SQL": [80, 90, 50, 65, 60],
    "Statistics": [90, 92, 40, 75, 50]
})
students["total_marks"] = students["Python"] + students["SQL"] + students["Statistics"]
students["percentage"] = round(students["total_marks"]/3, 2)
students["grade"] = np.where(students["percentage"] >= 80, "A", np.where(students["percentage"] >= 60, "B", "C"))


products = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Monitor", "Keyboard"],
    "Unit_Price": [50000, 800, 12000, 1500],
    "Supplier_Contact": [
        "9876500001", 
        "9876500002", 
        "9876500003", 
        "9876500004"
    ]
})
products["Unit_Price"] = products["Unit_Price"] * 1.08
products.rename(columns = {"Unit_Price" : "Updated_Price"})
products.drop(columns = "Supplier_Contact")


students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha"],
    "Attendance": [90, 72, 75, 60, 85, 74],
    "Branch": ["CSE", "IT", "CSE", "ECE", "ME", "IT"]
})
students["Attendance_status"] = np.where(students["Attendance"] >= 75, "eligible", "sortage")
df = students.loc[students["Attendance_status"] == "eligible"]


data = pd.DataFrame({
    "Product Name": [" Laptop ", "Mouse  ", " Monitor"],
    " UNIT PRICE ": [50000,  800, 12000],
    "Quantity Sold": [2, 10, 3],
    "Supplier_Contact": ["9876500001", "9876500002", "9876500003"]
})
data.columns = data.columns.str.strip()
data.columns = data.columns.str.lower()
data.columns = data.columns.str.replace(" ", "_")

#chain method
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")


df = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Age": [20, 19, 21, 20, 22],
    "Marks": [85, 92, 76, 95, 88],
    "Attendance": [90, 95, 80, 98, 85]
})

df.sort_values(by = "Marks", ascending = False)["Student"].iloc[0]
df.sort_values(by = "Attendance")["Student"].iloc[0]
df.sort_values(by = "Age")["Student"].iloc[0]
