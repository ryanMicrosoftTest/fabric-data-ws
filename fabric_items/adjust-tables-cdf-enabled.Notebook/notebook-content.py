# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fc2a7f71-e48c-4fc1-b6a6-90672c99a015",
# META       "default_lakehouse_name": "bronze_lh",
# META       "default_lakehouse_workspace_id": "d616705d-6d64-4f83-a586-051cc5ec8979",
# META       "known_lakehouses": [
# META         {
# META           "id": "fc2a7f71-e48c-4fc1-b6a6-90672c99a015"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from delta.tables import DeltaTable


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_address
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_customer
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_customerAddress
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_product
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_productCategory
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_productDescription
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_productModel
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_productModelProductDescription
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_salesOrderDetail
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

spark.sql("""
ALTER TABLE raw_salesOrderHeader
SET TBLPROPERTIES (
'delta.enableChangeDataFeed' = 'true'
)
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC DESCRIBE HISTORY raw_address

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
