from  rest_framework import selializers
from post.models import Post

class PostSerializer(selializers.ModelSerializer):
    class Meta:
        model = Post
        Fields = ['id','title','slug','author','body']