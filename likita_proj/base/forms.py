from django.forms import ModelForm
from .models import Post, User, CommentReply

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['id', 'owner', 'no_of_liked_post']
        
        
class ReplyForm(ModelForm):
    
    class Meta:
        model = CommentReply
        fields = ['body']
    