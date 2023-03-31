# Path: face/serializers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from retinaface import RetinaFace
from deepface import DeepFace


# from rest_framework.generics import GenericAPIView
# Create your views here.
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
        # image = request.data["image"]
        # detect all the faces present in the image
        # faces = RetinaFace.extract_faces(img_path=image)
        # for face in faces:
        #     # save the faces to a temporary directory
        #     plt.imsave(f"temp/{randint(0, 1000000)}.jpg", face)
        # # load each image in temporary directory
        # folder_dir = "/home/lox/finalyearproject/backend/temp"
        # listImg = list()
        # result = list()
        # for images in os.listdir(folder_dir):
        #     if images.endswith(".jpg"):
        #         listImg.append(f"temp/{images}")

        # for img in listImg:
        #     result = DeepFace.find(img_path=img, db_path="db_path", enforce_detection=False)
        #     print(result)
        image = request.data["image"]
        result = DeepFace.find(img_path=image, db_path="db_path")
        usnlist = list()
        for ins in result[0]["identity"]:
            # remove db_path from string ins
            usn = ins.strip("db_path/ .jpeg .jpg .png")
            usnlist.append(usn)
        return Response({"result": usnlist})
