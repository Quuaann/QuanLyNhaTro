from imgbeddings import imgbeddings
import psycopg2
from PIL import Image

# loading the face image path into file_name variable
file_name = "temp/temp.jpg"  # replace <INSERT YOUR FACE FILE NAME> with the path to your image
# opening the image
img = Image.open(file_name)
# loading the `imgbeddings`
ibed = imgbeddings()
# calculating the embeddings
embedding = ibed.to_embeddings(img)

conn = psycopg2.connect("postgres://avnadmin:AVNS_C3g-_WIL48h5-ugIW0R@pg-1e534733-facemmm.d.aivencloud.com:13503/defaultdb?sslmode=require")
cur = conn.cursor()
string_representation = "["+ ",".join(str(x) for x in embedding[0].tolist()) +"]"
cur.execute("SELECT * FROM pictures ORDER BY embedding <-> %s LIMIT 1;", (string_representation,))
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()