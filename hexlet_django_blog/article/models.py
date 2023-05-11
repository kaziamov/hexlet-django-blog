from django.db import models as m


class ArticleModel(m.Model):
    title = m.CharField(max_length=200)
    body = m.TextField()
    created_at = m.DateTimeField(auto_now_add=True)
