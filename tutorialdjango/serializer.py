from  rest_framework import selializers
from .models import Post

class PostSerializer(selializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','slug','author','body']