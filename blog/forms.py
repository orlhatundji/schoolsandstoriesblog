from django.forms import ModelForm
from blog.models import Post
from blog.models import Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']