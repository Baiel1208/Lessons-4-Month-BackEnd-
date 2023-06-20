from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title="Test", content="Test")

# HW4
    def test_post_update(self): 
        url = reverse("post-update", kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/post_update.html')
        self.assertEqual(response.status_code, 200)


    def test_post_delete(self):
        url = reverse("post-delete", kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/post_delete.html')
        self.assertEqual(response.status_code, 200)


    # def test_index(self):
    #     response = self.client.get(reverse("index-page"))
    #     self.assertTemplateUsed(response, 'blog/index.html')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_contacts(self):
    #     response = self.client.get(reverse("contacts-page"))
    #     self.assertTemplateUsed(response, 'blog/contacts.html')
    #     self.assertEqual(response.status_code, 200)


    # def test_get_about(self):
    #     response = self.client.get(reverse("about-page"))
    #     self.assertTemplateUsed(response, 'blog/about.html')
    #     self.assertEqual(response.status_code, 200)