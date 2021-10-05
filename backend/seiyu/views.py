from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, parsers

from django.core.files.storage import FileSystemStorage

from .models import Seiyu
from .serializers import SeiyuSerializer
from .services import SeiyuService

  

# Create your views here.
class SeiyuViewSet(viewsets.ViewSet):
  queryset = Seiyu.objects.all()
  serializer_class = SeiyuSerializer
  parser_classes = (parsers.FormParser, parsers.MultiPartParser)
  

      
  @action(methods=['put'], detail=False)
  def classify(self, request):
    """
        Classify Seiyu
        ---
        parameters:
            - seiyu: name
              image: files
        responseMessages:
            - code: 204
    """
    
    img = request.FILES['image']
    fss = FileSystemStorage()
    file = fss.save(img.name, img)
    file_ulr = fss.url(file)
    
    seiyu_name = SeiyuService.predict_seiyu(img_url=file_ulr)

    
    return Response({ 'seiyu': seiyu_name },status=204)


  def list(self, request):
    """return available seiyu list

    Args:
        request ([type]): [description]
    """
    return Response(['sakura ayane', 'unkown'], status=200)


  

