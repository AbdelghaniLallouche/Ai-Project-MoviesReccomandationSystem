from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .InferenceSystem import *
class MovieRec(APIView):

    def post(self, request, *args, **kwargs):

        #send the data in json format like this
        # data={
        #"language":value,
        #"type": value,
        #"time": value,
        #"genre": value,
        #"principalactor": value,
        # }
        # to send post request axios.post('http://localhost:8000/api/movie',data)
        data = request.data
        language = data.get('language')
        type = data.get('type')
        time = data.get('time')
        genre = data.get('genre')
        principalactor = data.get('principalactor')
        data_list =[ principalactor, language, type, genre, time]
        movies = final_Movie(data, data_list)
        return Response({"movies": movies , "data" : data_list #to check the data sent to the model
        })
