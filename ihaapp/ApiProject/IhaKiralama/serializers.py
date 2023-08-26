from rest_framework import serializers,fields
from IhaKiralama.models import IHA,Kiralama,User


class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model=IHA 
        fields=('iha_id','marka','model','agirlik','kategori','eklenme_zamani')

class KiralamaSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=Kiralama 
        fields=('kiralama_id','iha','kiralayan_uye','kiralama_tarihi','iade_tarihi','kiralama_zamani')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User 
        fields=('id','username','email','last_login')
