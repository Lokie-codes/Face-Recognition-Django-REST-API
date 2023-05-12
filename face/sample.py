from deepface import DeepFace

# result = DeepFace.verify(
#     img1_path="/home/lox/finalyearproject/backend/WhatsApp Image 2023-05-11 at 10.05.30.jpeg",
#     img2_path="/home/lox/finalyearproject/backend/24883120_375096919618520_1406499502_o.jpg",
#     distance_metric="euclidean_l2",
# )
# print(result)
image = "/home/lox/finalyearproject/backend/images/all.png"

result = DeepFace.find(
    img_path=image,
    db_path="/home/lox/finalyearproject/backend/db_path",
    model_name="Facenet512",
    detector_backend="retinaface"
)
print(result)
usns = list()
for ins in result[0]["identity"]:
    # remove db_path from string ins
        usn = ins.strip("db_path/ .jpeg .jpg .png")
        usns.append(usn)

print(usns)