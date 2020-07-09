from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="authors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('autor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to="posts/")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name="author", related_name="blog_author")
    tags = models.ManyToManyField(Tag, verbose_name="tags")
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
