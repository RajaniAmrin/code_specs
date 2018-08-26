from tastypie.resources import ModelResource
from api_calls.models import Add_api,Provider,service_area
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class Add_api_Resource(ModelResource):
    class Meta:
        queryset = Add_api.objects.all()
        resource_name = 'Add_api'
        authorization = Authorization()
        
        
class Provider_Resource(ModelResource):
    class Meta:
        queryset = Provider.objects.all()
        resource_name = 'provider'
        authorization = Authorization()
        filtering = {
            'name': ALL,
            'Email': ALL_WITH_RELATIONS,
            'phone_number': ALL,
            'Language':ALL,
            'Currency':ALL
        }
    # def dispatch(self, request_type, request, **kwargs):
        # print ('request_type---',request.method)
class service_area_resource(ModelResource):
    class Meta:
        queryset = service_area.objects.all()
        resource_name = 'service_area'
        authorization = Authorization()
        filtering = {
            'name': ALL,
            'lat': ALL_WITH_RELATIONS,
            'lng': ALL
        }        
        