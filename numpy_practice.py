import numpy as np
import pandas  as pd
import matplotlib.pyplot as plt


abc=pd.read_csv("FactSales.csv")
# print(abc.head(3))
# print(abc.sample(3))
# print(abc.tail(3))

#pandas
#null and na
# print(pd.isnull(abc))
# print(pd.notnull(abc))
# print(pd.isna(abc))
#print(pd.notna(abc))
#print(abc.fillna(0))
# print(abc.dropna(axis=0))
# print(abc.dropna(axis=1))
# print(abc.duplicated())
# print(abc.drop_duplicates(keep="last"))
# print(abc.drop_duplicates(keep=False))
# print(abc.replace("PayPal","UPI"))
# sd=abc.rename(columns={"Channel":"Channels"})
# print(sd)
# print(abc["SalesKey"].astype("string"))
# print(pd.to_numeric(abc["SalesKey"]))
#print(abc["Profit"].sort_index())
# print(abc["Profit"].sort_values())
# sd=abc.groupby("Channel")[["UnitPrice","Profit"]].agg(Total_unit_price=("UnitPrice","sum"),
#                                            Total_Profit=("Profit","sum"))
# df=pd.DataFrame(sd)
# print(sd)
# #print(df["Total_unit_price"])
# conditions=[df["Total_unit_price"]>=6150000,
#             (df["Total_unit_price"]<6150000)&(df["Total_unit_price"]>=3000000),
#             df["Total_unit_price"]<3000000
#             ]

#sd=abc.drop_duplicates(keep="")
# r=abc.replace("PayPal","UPI")
# l=abc.rename(columns={"Profit":"Profits"})
# print(l)
# fd=abc.groupby(["Channel","PaymentMethod"])["Profit"].agg(
#                                                             TotalProfit="sum"
# )
# fc=abc.pivot(
#         index="SalesKey",
#         columns=["Channel"],
#         values="Profit"
# )

# print(fc.fillna(0).astype(int))

# print(pd.pivot_table(
#             abc,
#             index="PaymentMethod",
#             columns="Channel",
#             values="Profit",
#             aggfunc="sum"
# ).fillna(0).astype(int))

# print(pd.crosstab(
#                 index=abc["PaymentMethod"],
#                 columns=abc["Channel"],
#                 values=abc["Profit"],
#                 aggfunc="sum"
# ))

# print(abc.pivot(
#         index="SalesKey",
#         columns="PaymentMethod",
#         values="Profit"
# ).fillna(0).astype(int))

# print(pd.pivot_table(
#             abc,
#             index="PaymentMethod",
#             columns="Channel",
#             values="Profit",
#             aggfunc="sum"
# ))
# print(pd.crosstab(
#                 abc["PaymentMethod"],
#                 abc["Channel"],
#                 abc["Profit"],
#                 aggfunc="sum"
# ).astype(int))
customers=pd.read_csv("customers.csv")
employees=pd.read_csv("employees.csv")
orders=pd.read_csv("orders.csv")
salaries=pd.read_csv("salaries.csv")
# print(customers.head(1))
# print(orders.head(1))
# print(employees.head(1))
# print(salaries.head(1))
# print(pd.merge(
#         customers,
#         orders,
#         on="CustomerID",
#         how="inner"    
# ))

# df=salaries.join(
#             employees.set_index("EmployeeID"),
#             on="EmployeeID",
#             how="inner"
# )
# print(df.pivot(
#         index="EmployeeName",
#         columns="Department",
#         values="Salary"
# ).fillna(0).astype(int))

# print(
#     pd.pivot_table(
#             df,
#             index="EmployeeName",
#             columns="Department",
#             values="Salary",
#             aggfunc="sum"
#     )
# )

# print(pd.crosstab(
#         index=df["EmployeeName"],
#         columns=df["Department"],
#         values=df["Bonus"],
#         aggfunc="sum"
# ).fillna(0).astype(int))

# cst=customers.join(
#             orders.set_index("CustomerID"),
#             on="CustomerID",
#             how="inner"
# )

# # print(pd.pivot_table(
# #             cst,
# #             index="Segment",
# #             columns="Product",
# #             values="Sales",
# #             aggfunc="sum"
# #                ).fillna(0).astype(int))

# df=pd.DataFrame({
#             "S.No":[1,2,3],
#             "Name":["Aman","Raman","Simran"],
#             "Date":["10-10-2001","15-05-2005","11-01-2002"]}
# )
# # df["Date"]=pd.to_datetime(df["Date"],  dayfirst=True)
# # print(df["Date"].dt.year)
# # print(df["Date"].dt.day)
# # print(df["Date"].dt.month)
# # print(df["Date"].dt.weekday)
# # print(customers["City"].value_counts())
# df["Date"]=pd.to_datetime(df["Date"],dayfirst=True)
# print(df["Date"].dt.day)
fd=abc.groupby("PaymentMethod",as_index=False)["Profit"].agg(Total_profit="sum").astype({"Total_profit":int})

print(fd)
#print(plt.bar(fd["PaymentMethod"],fd["Total_profit"]))
#print(plt.plot(abc["Profit"],abc["UnitPrice"]))
#print(plt.hist(abc["Profit"],bins=5))
# print(plt.scatter(abc["Profit"],abc["UnitPrice"]))
# print(plt.xlabel("Profit"))
# print(plt.ylabel("UnitPrice"))
# print(plt.title("Profit vs UnitPrice"))
# print(plt.show())
# print(plt.legend())
# print(plt.figure(figsize=(10,9)))
print(abc.head(3))


#print(fd)