# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os
import io

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ecommerce_transactions_with_ip_prepared = dataiku.Dataset("ecommerce_transactions_with_ip_prepared")
df = ecommerce_transactions_with_ip_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Filter to only US records
df_usa = df[df["MerchantIP_country"] == "United States"]

# Determine average purchase amount, per customer age and purchase hour
df_avg_purchase = df[["PurchaseHour", "CustomerAge", "OrderTotal"]].groupby(by=["PurchaseHour",
                                                                                "CustomerAge"], as_index=False).mean()

# Scatter plot of avg purchase amount, per customer age and purchase hour
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = df_avg_purchase["PurchaseHour"]
ys = df_avg_purchase["CustomerAge"]
zs = df_avg_purchase["OrderTotal"]

ax.set_xlabel('Purchase Hour')
ax.set_ylabel('Customer Age')
ax.set_zlabel('Avg Order Total')
ax.set_title("US Transactions Only")

ax.scatter(xs, ys, zs)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Save scatter plot to folder
folder_for_plots = dataiku.Folder("MIrujfBg")

buffer = io.BytesIO()
plt.savefig(buffer, format="png")
folder_for_plots.upload_stream("US Transactions Only.png", buffer.getvalue())