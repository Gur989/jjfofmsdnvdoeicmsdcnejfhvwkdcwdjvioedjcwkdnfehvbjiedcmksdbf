import pandas as pd
import numpy as np

customers=pd.read_csv("customers.csv")
orders=pd.read_csv("orders.csv")
employees=pd.read_csv("employees.csv")
FactSales=pd.read_csv("FactSales.csv")
salaries=pd.read_csv("salaries.csv")

# print(customers.info())
# print(customers.size)
# #Data size
# print(customers.shape)
# print(customers.dtypes)
# print(customers.index)
# print(customers.ndim)

# #missing data
# print(pd.isna(customers).sum())
# print(pd.isnull(customers).sum())

# #customers cities
# print(customers["City"].value_counts())
# print(customers)
# print(orders)
# print(salaries)
# print(employees)
# print(FactSales)\
# print(FactSales["PaymentMethod"].value_counts()
#                    .reset_index(name="ct").sort_values("ct",ascending=False))

# print(FactSales["SalesKey"].duplicated().sum())
# print(FactSales["Profit"].quantile(.20))   
# print(FactSales["SalesAmount"].max())
# print(FactSales["SalesAmount"].mean()) 
# print(orders["Product"].value_counts())
# print(FactSales["SalesAmount"].sum())
# print(FactSales.groupby("Channel")["SalesAmount"].agg("sum").reset_index().sort_values("SalesAmount",ascending=False))
# print(FactSales.groupby("PaymentMethod")["Profit"].sum().reset_index(name="Prof").sort_values("Prof",ascending=False))
weather_data=pd.read_csv("weather_data.csv")
FactSales["OrderDateKey"]=pd.to_datetime(FactSales["OrderDateKey"])
FactSales["ShipDateKey"]=pd.to_datetime(FactSales["ShipDateKey"])
# print(FactSales.groupby("ShipDateKey")["Profit"].agg("sum").reset_index())
#print(orders.groupby("Product")["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False))
#print(FactSales.groupby("CustomerKey")["SalesAmount"].sum().astype(int))
# print(orders["Sales"])
fc=FactSales["CustomerKey"].value_counts().reset_index(name="count")
print(fc[fc["count"]>1].count())

# print(FactSales["SalesAmount"])
jk=np.select(
        [FactSales["SalesAmount"]>1000,
         FactSales["SalesAmount"]>500] ,
         ["High","Medium"],
         default="Low"   
)
# print(pd.DataFrame({"Sales_cat":[np.select(
#         [FactSales["SalesAmount"]>1000,
#          FactSales["SalesAmount"]>500] ,
#          ["High","Medium"],
#          default="Low" ]  
# )}))
# df=pd.DataFrame({"Sales_cat":[
#                 np.select(
#                     [FactSales["SalesAmount"]>1000,
#                      FactSales["SalesAmount"]>500],
#                      ["High","Medium"],
#                      default="Low"
#                 )
# ]
# })
# print(df["Sales_cat"])
# rt=pd.DataFrame({"fidt":[np.where(
#     FactSales["SalesAmount"]>900,
#         "Expensive","Normal")
# ]
# }
# )
# print(rt.reset_index().columns)

# FactSales["sales_caat"]=pd.cut(
#     FactSales["SalesAmount"],
#     bins=[0,400,600,1200],
#     labels=["Average","Good","Excellent"]
# )
# print(FactSales["sales_caat"].dropna().isna().sum())

# print(
#     pd.DataFrame({
#         "pd1":
#     [np.select(
#         [FactSales["SalesAmount"]>1000,
#           FactSales["SalesAmount"]>500],
#         ["High","Medium"],
#         default="Low"
#     )]
#     }
# ).reset_index().columns)

print(
    pd.cut(
        FactSales["SalesAmount"],
        bins=[0,800,1500],
        labels=["High","Low"]
    )
)



