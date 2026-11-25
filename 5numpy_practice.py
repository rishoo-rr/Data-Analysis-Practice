import numpy as np

array1 = np.array([5])
array2 = np.array([5,6,7,8,9])
array3 = np.array([[4,5,6],
                   [7,8,9]])
array4 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(array1)
print(array2)
print(array3)
print(array4)

print(f"shape : {array1.shape} , size : {array1.size}")
print(f"shape : {array2.shape} , size : {array2.size}")
print(f"shape : {array3.shape} , size : {array3.size}")
print(f"shape : {array4.shape} , size : {array4.size}")
print(f"dimension : {array1.ndim} , dt : {array1.dtype}")
print(f"dimension : {array2.ndim} , dt : {array1.dtype}")
print(f"dimension : {array3.ndim} , dt : {array1.dtype}")
print(f"dimension : {array4.ndim} , dt : {array1.dtype}")

array5  = np.zeros((3,3) ,dtype =  int)
print(array5) 

array6  = np.ones((2,3,3) , dtype = int)
print(array5) 

array7  = np.full((2,2,3) ,5)
print(array5) 

array8 = np.eye(5,4,3,dtype =  int)
print(array6)

array9 = np.empty((3,3))
print(array7)

array10 = np.arange(5,10,2) 
print(array8)

array11 = np.linspace(6, 36 ,6)
print(array9)

array12 = np.random.rand(2 ,3)
print(array10)

array13 = np.random.randint(1,6,3)
print(array11)

a = np.array([5,8,9,1,3,24,34,43] ,dtype = np.int8)

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]
              ] ,dtype = np.int8)

c = np.array([[10,20,30,40],
              [50,60,70,80],
              [90,100,110,120]] ,dtype = np.int8)

d  = np.array([  
    [[1,2,3],
     [4,5,6],
     [7,8,9]],

    [[10,11,12],
     [13,14,15],
     [16,17,18]],

    [[19,20,21],
     [22,23,24],
     [25,26,27]],

     [[82,29,30],    
      [31,32,33],
      [34,35,36]]
], dtype = np.int8)  

e = np.array([
 [[37, 38, 39],
  [40, 41, 42],
  [43, 44, 45]],

 [[46, 47, 48],
  [49, 50, 51],
  [52, 53, 54]],

 [[55, 56, 57],
  [58, 59, 60],
  [61, 62, 63]]
] , dtype = np.int8)

print(np.concatenate((c,c)))
print(np.concatenate((c,c)).shape)

data = np.split(c,[1,2], axis = 0)
print((data))

for r in data :
    print(r)

print(d+10)
print(d-10)
print(d*10)
print(d/10)

print(np.square(a))
print(np.sqrt(a))
print(np.sqrt(c))

print(np.min(c))
print(np.max(c))

rr1 = np.arange(16).reshape(4,4)
rr2 = np.arange(4).reshape(2,2)
print(rr1)
print(rr2)

print(d[0, :2, 1])
print(d.flatten())  

data = np.split((d), 3, axis = 1)

for i in data :
    print(i)

print(c + 10)
print(c - 10)
print(c * 10)
print(c / 10)

print(np.dot(b,c))

print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))

r = np.array([2.5, 0.5, 0.5, 7.5, 5.5, 15.5, 25.5, 34.5 ])

r1 = np.square(r)

r2 = np.mean(r1)

r3 = np.sqrt(r2)

print(r3)

rr = np.arange(12).reshape(3,4)
rr1 = np.array(4)

print( rr == rr1 )
print(np.array_equal(rr,rr1))

lst = [1,2,3,4,5,6,7,8]
print(lst[-4:])

print(c[ c > 5])

print(np.sum(c, axis = 0))
print(np.sum(c, axis = 1))

r = np.array([3,4,np.nan, 5, np.inf])
print(np.nan_to_num(r))

celsius = np.array([0,10,20,30,40])
fahrenhiet = (celsius*(9/5)) + 32

marks  = np.array([65,72,80,88,91])
bonus = 5
updated_marks = marks + bonus
print(marks)
print(updated_marks)

pd_price = np.array([100, 250, 400, 550, 800])
new_pd_prce = pd_price*0.9
print(new_pd_prce)

salary = np.array([30000, 35000, 40000, 45000, 50000])
new_salary = salary*1.1
print(new_salary)

marks = (78, 85, 92, 67, 88)
marks = np.array(marks)
new_marks = marks + 3
print(new_marks)

this_year_sales_records = np.array([125000, 148000, 135000, 172000])
next_year_expected_sales = this_year_sales_records*1.15
print(next_year_expected_sales)

branch_a = np.array([120, 150, 180, 100, 200])
branch_b = np.array([80, 130, 170, 120, 150])

total_inventory_of_a = sum(branch_a)
total_inventory_of_b = sum(branch_b)

diffrence = branch_a - branch_b
combine_inventory = (branch_a + 20) + (branch_b + 20)

print(total_inventory_of_a)
print(total_inventory_of_b)
print(combine_inventory)

prices = np.array([250, 400, 750, 1200])
unit_sold = np.array([12, 8, 5, 10])

revenue = prices*unit_sold
new_revenue = revenue*1.05
print(revenue)
print(new_revenue)

a = np.array([2.5, 6.8, 9.2, 4.3])

b = np.array(a, dtype = int)
c = a.astype(int)

student_marks = np.arange(25).reshape(5,5)

print(student_marks)
print(student_marks.ndim)
print(student_marks.shape)
print(student_marks.size)
print(student_marks.dtype)
print(len(student_marks)) 
print(student_marks.size)

a = np.zeros((5,4))
b = np.full((5,4), 50)

print(a)
print(b)

scores = np.array([45, 56, 67, 78, 89])
after_grace_marks = scores + 3
final_score = after_grace_marks*1.1
print(final_score)

target = np.linspace(20000, 100000  , 9)
actual_sales = np.array([18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000])
diffrence = target - actual_sales
print(target)
print(diffrence)

dataset = np.array([10, 20, 30.5, 40, 50.75])
int_dataset = dataset.astype(int)
print(dataset.dtype)
print(int_dataset*3)

price = np.array([499, 799, 1299, 1999, 2499])
increses_price = price*1.12
final_price = increses_price + 50
print(final_price)

price = np.array([1000, 2000, 3000, 4000])
after_first_discount = price*0.9
after_second_discount = after_first_discount*0.95
print(after_second_discount)

revenue = np.array([80000, 95000, 110000, 125000, 140000, 155000])
increses = revenue*0.12
forecast_revenue = revenue + increses
target = np.linspace(80000, 160000, 6)
print("revenue :",revenue)
print("increses :",increses)
print("forecast_revenue :",forecast_revenue)
print("target :",target)
print(forecast_revenue == target)

products = np.full((4,5), 100)
products[:2] += 20
products[-2:] = products[-2:]*0.9
print("middle two section :",products[1:3])
print("first thre products :",products[:, :3])
print("bottom right 2❌2 matrix :",products[2:4, 3:5])

salary = np.array([[30000, 5000],
                   [40000, 6000],
                   [50000, 8000],
                   [60000, 10000]])
print("second employee info :",salary[1])
print("all basic salary :",salary[:, :1])
print("all allowance :",salary[:, 1:])
salary[:, 1:] += 1000
salary[-2:, :1] = salary[-2:, :1] * 1.1
print(salary)

target = np.linspace(10000, 100000, 12)
month_num = np.arange(1,13)
print(target[::11])
print(target[3:8])
target *= 1.15
print(target[-4:])

numbers  = np.array([4,9,16,25])
print(np.sqrt(numbers))

x = np.array([3,5,8])
print(x**3)
print(np.square(x)*x)
a = np.power(x, 3)
print(np.cbrt(a))

numbers = np.array([-1,-4, 7, 8, -5, -9])
print(np.abs(numbers))
n = len(numbers)
for i in range(n) :
    if numbers[i] < 0 :
        numbers[i] *= -1

values = np.array([10.83754, -20.7634, 30.7654])
print(np.around(values, 2))
print(np.floor(values))
print(np.ceil(values))
print(np.trunc(values))

orders = np.array([[1000, 2, 500],
                   [1001, 3, 750],
                   [1002, 1, 1200],
                   [1003, 4, 300],
                   [1004, 2, 900]])
print(orders[2])
print(orders[:, 1])
print(orders[:, 2])
print(orders[:3])
orders[-2:, 2] = orders[-2:, 2]*1.1
orders[0, 1] += 1
separeted_array = orders[:, 1:]
print(separeted_array)
print(orders.size)
print(orders.shape)

import numpy as np 
revenue = np.array([
    120000, 135000, 128000, 145000,
    150000, 138000, 160000, 172000,
    155000, 148000, 180000, 195000
])
print(np.mean(revenue))
print(np.min(revenue))
print(np.max(revenue))
print(np.argmax(revenue))
print(np.argmin(revenue))
print(np.sum(revenue))
diffrence = np.max(revenue) - np.min(revenue)
print(diffrence)
print(revenue)

sales = np.array([
    [120, 150, 180],
    [200, 170, 160],
    [100, 140, 130],
    [180, 190, 210]
])
print(np.sum(sales, axis = 1))
print(np.mean(sales, axis = 1))
print(np.sum(sales, axis = 0))
print(np.mean(sales, axis = 0))
print(np.max(sales, axis = 1))

transactions = np.array([
                         500, -2000, 1500, -4500, 7000,
                         -12000, 25000, -3000, 8000, -18000,
                         4500, 22000,  -6000, 9000, -2500
                                                         ])
deposit = transactions[transactions > 0]

withdrawa = transactions[transactions < 0]

total_deposit = deposit.sum()

total__withdrawa = withdrawa.sum()

net_transactions = np.sum(transactions)

abs_transactions = np.abs(transactions)

avg_abs = np.mean(abs_transactions)

cust_transactions = transactions[abs_transactions > avg_abs]

largest_deposit = np.max(transactions)

largest_withdrawals = np.min(transactions)

labels = np.where(transactions > 0, "credit", "debit")

abs_count = len(abs_transactions[abs_transactions > 10000])

total_count = len(abs_transactions)
per_transactions = (abs_count * 100)/total_count

new_t = transactions.reshape(3,5)

production = np.array([[120, 135, 128, 145, 150, 138],
                       [110, 125, 118, 130, 142, 135],
                       [160, 155, 170, 165, 180, 175],
                       [95, 105, 100, 115,  108, 120]])

mashine_total_p = np.sum(production, axis = 1)
day_total_p = np.sum(production, axis = 0)

avg_machine = np.mean(production, axis = 1)

highest_avg_idx = np.argmax(avg_machine)
highest_avg = production[highest_avg_idx]

lowest_idx = np.argmin(day_total_p)
lowest_pd_day = production[:, lowest_idx]

overall_avg = np.mean(production)
value = production[production > overall_avg]

new_p = np.where(production < 120, production * 1.05, production)

alternate_days = production[:, ::2]

last_3days = production[[0,2], -3:]

label = np.where(production > overall_avg, "high", "normal")

loan_amount = np.array([100000, 250000, 500000, 750000,
                        120000, 350000, 900000, 450000])

interest_rate = np.array([8.5, 9.2, 8.8, 10.1,
                          7.9, 9.5, 10.5, 8.7])

anual_inerest = loan_amount * (interest_rate)/100 

total_interest = np.sum(anual_inerest)

avg_interest = np.mean(anual_inerest)

highest_interest = loan_amount[np.argmax(interest_rate)]

criteria = (loan_amount > 400000) & (interest_rate > 9)
loan_amount[criteria]

loan_amount = np.array([100000, 250000, 500000, 750000,
                        120000, 350000, 900000, 450000])

interest_rate = np.array([8.5, 9.2, 8.8, 10.1,
                          7.9, 9.5, 10.5, 8.7])

labels = np.where(interest_rate >= 10, "high", np.where(interest_rate >= 9, "medium", "low"))

rounded_inr = np.around(interest_rate, 2)

median = np.median(loan_amount)

avg_itr = np.mean(interest_rate)

loan = loan_amount[loan_amount > median]
interest = interest_rate[interest_rate > avg_itr]

std = np.std(interest_rate)

points = np.array([[3, 4],
                   [5, 12],
                   [8, 15],
                   [7, 24],
                   [9, 40],
                   [12, 35],
                   [15, 20],
                   [6, 8]])

distance = np.sqrt(np.sum(np.square(points), axis = 1))

x = points[:, 0]
y = points[:, 1]

rounded_distance = np.around(distance, 2)

nearest = np.min(distance)
farthest = np.max(distance)

avg_dist = np.mean(distance)
above_avg = distance[distance > avg_dist]

labels = np.where(distance >= 30, "long", np.where(distance >= 15, "medium", "short"))

to_len = len(labels)
long_len = len(labels[labels == "long"])
percentage = (long_len/to_len) * 100

flatted_array = points.flatten()

size = flatted_array.size

inventory = np.array([[12, 45, 8, 32, 20],
                      [5, 60, 15, 25, 10],
                      [30, 18, 6, 40, 22],
                      [9, 55, 12, 28, 7]])

total_int_st = np.sum(inventory, axis = 1)
total_int_pd = np.sum(inventory, axis = 0)

high_int_st = np.argmax(total_int_st) + 1
low_int_pd = np.argmin(total_int_pd) + 1

billow_10 = inventory[inventory < 10]

count = len(billow_10)

labels = np.where(inventory < 10, "reorder", "ok")

new_int = np.where(inventory < 10, inventory * 1.2, inventory)

rounded = np.around(new_int)

median = np.median(inventory)

last_tow_pd = new_int[:, -2:]

fllated = new_int.flatten()

standerd_division = np.std(new_int)

prices = np.array([820, 835, 810, 850, 875,
                   860, 890, 910, 895, 930,
                   945, 920, 960, 975, 990])

a = prices[1:]
b = prices[:-1]

movement = a - b 

abs = np.abs(movement)

largest = np.max(movement)

mean = np.mean(movement)
above_avg = movement[movement > mean]

percentage = (abs/a) * 100
rounded_p = np.around(percentage, 2)

#    days product
days = a[rounded_p > 2]
#    days index
days = np.where(rounded_p > 2)

mx = np.max(prices)
mn = np.min(prices)

reshaped_prices = prices.reshape(3,5)
avg = np.mean(reshaped_prices, axis = 1)

leads = np.array([[12000, 15000, 11000, 18000, 21000],
                  [14000, 13000, 17000, 19000, 22000],
                  [10000, 16000, 15000, 20000, 23000],
                  [18000, 17000, 19000, 21000, 25000]])

each_campaign = np.sum(leads, axis = 1)
each_channel = np.sum(leads, axis = 0)

mx_campaign = np.max(each_campaign)
mx_channel = np.max(each_channel)

avg_campaign = np.mean(leads, axis = 1)

value = leads[leads > np.mean(leads)]

new_leads = np.where(leads < 15000, leads * 1.1, leads)
rounded = np.round(new_leads)

labels = np.where(leads > np.median(leads), "high", "low")
extracted = new_leads[::2]

orderid = np.arange(101, 113)
quantity = np.array([3, 5, 2, 8, 4, 6, 3, 10, 7, 2, 5, 9])
price = np.array([1200, 800, 2500, 450, 1800, 950, 2200, 600, 1500, 3000, 750, 1250])
rating = np.array([4.5, 3.8, 4.8, 4.1, 4.5, 4.7, 4.9, 3.2, 4.6, 4.0, 3.9, 4.8])

np.set_printoptions(suppress = True)

data = np.column_stack((orderid, quantity, price, rating))

dimension = data.ndim
shape = data.shape
size = data.size

first_5 = data[0:5]
last_3 = data[-3:]

every_second_od = data[::2]

quantity = data[:, 1]
price = data[:, 2]

revenue = quantity * price

total_rv = np.sum(revenue)
avg_rv = np.mean(revenue)

max_rv_idx = np.argmax(revenue)
max_order = data[max_rv_idx]

median = np.median(revenue)

labels = np.where(revenue >= 15000, "high", np.where(revenue >= 75000, "medium", "low"))

category1 = (quantity >= 5) & (rating >= 4.5)
orders1 = data[category1]

median_price = np.median(price)

category2 = (price > median_price) & (rating < 4)
orders2 = data[category2]

discount_p = np.where(price > 1000, price * 0.9, price)
rounded_dis_p = np.round(discount_p, 2)

std_p = np.std(price)

rating = data[:, -1]

total_count = len(rating)
count = sum(rating >= 4.5)

percentage = (count/total_count) * 100

revenue = revenue.reshape(3,4)

avg_revenue = np.mean(revenue, axis = 1)

revenue = revenue.flatten()

category = (rating >= 4.5) & (revenue > avg_rv)

total_revenue = np.sum(revenue[category])

campaigns = np.array([[101, 10000, 800, 80, 5000, 7500],
[102, 15000, 1200, 150, 7000, 12000],
[103, 8000, 400, 30, 3000, 4200],
[104, 20000, 1800, 250, 9000, 18000],
[105, 12000, 600, 90, 6000, 8000],
[106, 18000, 1500, 220, 8000, 16000],
[107, 9000, 300, 20, 2500, 3000],
[108, 25000, 2200, 300, 11000, 24000]]) 

campaign_id = campaigns[:, 0]
impressions = campaigns[:, 1]
clicks = campaigns[:, 2]
conversions = campaigns[:, 3]
cost = campaigns[:, 4]
revenue = campaigns[:, 5]

highest_rv_camp = campaigns[np.argmax(revenue)]

roi = ((revenue-cost)/cost) * 100
highest_roi_camp = campaigns[np.argmax(roi)]
avg_roi = np.mean(roi)

ctr = (clicks/impressions) * 100
avg_ctr = np.mean(ctr) 

category = (ctr > avg_ctr) & (roi > avg_roi)
values = campaigns[category]

labels = np.where(roi >= 80, "Excellant", np.where(roi >= 40, "good", "poor"))

total_count = len(labels)
Excellant_count = len(labels[labels == "Excellant"])
Exlt_perc = (Excellant_count/total_count) * 100

p75 = np.percentile(revenue, 75)
above_75 = revenue[revenue > p75]