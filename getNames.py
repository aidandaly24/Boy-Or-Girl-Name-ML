from google.cloud import bigquery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aidandaly/Desktop/PersonalCode/Unfinished/BoyOrGirl/boyorgirlnames-393a34edcf8d.json"

clientForNames = bigquery.Client()

sql = """
SELECT
  name,
  gender,
  COUNT(name) AS num_names
FROM
  `bigquery-public-data.usa_names.usa_1910_current`
GROUP BY
  name,
  gender
"""

namesDF = clientForNames.query(sql).to_dataframe()

print(namesDF.shape)
namesDF.head()
