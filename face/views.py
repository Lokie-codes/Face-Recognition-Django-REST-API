# Path: face/serializers.py
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from retinaface import RetinaFace
from deepface import DeepFace
from PIL import Image

@api_view(["GET"])
def faceOverview(request):
    """
    An overview of all the available API endpoints to work with the face detection and recognition.
    """
    api_urls = {
        "Face Count": "/count/",
        "Detect Faces": "/faces/",
        "Recognise Faces": "/recognise/",
        "Students Present": "/present/",
        "Students Absent": "/absent/",
        "Present Students Count": "/present/count/",
        "Absent Students Count": "/absent/count/",
    }
    return Response(api_urls)


class FaceCount(APIView):
    """
    Count the number of faces in an image.
    """
    def post(self, request, *args, **kwargs):
        image = request.data["image"]
        faces = RetinaFace.detect_faces(image)
        return Response({"count": len(faces)})


class FaceDetect(APIView):
    """
    Detect all the faces present in the image.
    """
    def post(self, request, *args, **kwargs):
        image = request.data["image"]
        faces = RetinaFace.detect_faces(image)
        return Response({"faces": faces})


class FaceRecognise(APIView):
    """
    Recognise the multiple faces present in the image and compare them to database
    """
    def post(self, request):      
        byteImage = request.data.get("image")
        image = Image.open(byteImage)
        image.save("image.jpeg")
        image = os.path.abspath("image.jpeg")
        result = DeepFace.find(img_path=image, db_path="db_path")
        # result is a list of dataframes
        # print(f"Result is type : {type(result)}")
        usns = list()
        print(f"result - {result}")
        try:
            # for multiple faces
            for rep in result:
                # rep is a set of dataframes
                if rep.empty:
                    # if dataframe is empty
                    continue
                row = rep.iloc[0]
                # print(row["identity"]) 
                # strip usn from row["identity"]
                usn = row["identity"].strip("/home/lox/finalyearproject/backend/db_path/ .jpeg .jpg .png")
                usns.append(usn)
        except:
            # print(f"Single Face Detected!")
            # for single face
            print(f"Some Exception has occured")
            
        # result = [*set(usns)]
        return Response({"result": usns})

