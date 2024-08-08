from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from greenhousebackend.models import User, Tag
from greenhousebackend.views import TagSerializer

class TagTests(APITestCase):
  
  fixtures = ['tags']
  
  def setUp(self):
    self.user = User.objects.first()
    
  def test_create_tag(self):
    """create tag test"""
    url = '/tags'
    
    tag = {
      "name": "test tag"
    }
    
    response = self.client.post(url, tag, format='json')
    new_tag = Tag.objects.last()
    expected = TagSerializer(new_tag)
    self.assertEqual(expected.data, response.data)
    
  def test_get_tag(self):
    """Get Tag Test"""
    tag = Tag.objects.first()
    url = f'/tags/{tag.id}'
    response = self.client.get(url)
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    expected = TagSerializer(tag)
    self.assertEqual(expected.data, response.data)
    
  def test_list_tags(self):
    """test list tags"""
    url = '/tags'
    response = self.client.get(url)
    all_tags = Tag.objects.all()
    expected = TagSerializer(all_tags, many=True)
    
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual(expected.data, response.data)
    
  def test_change_tag(self):
    """test update tag"""
    tag = Tag.objects.first()
    url = f'/tags/{tag.id}'
    
    updated_tag = {
      'name': f'{tag.name} updated'
    }
    
    response = self.client.put(url, updated_tag, format='json')
    self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    tag.refresh_from_db()
    self.assertEqual(updated_tag['name'], tag.name)
    
  def test_delete_tag(self):
    """test delete tag"""
    tag = Tag.objects.first()
    url = f'/tags/{tag.id}'
    response = self.client.delete(url)
    self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    
    response = self.client.get(url)
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)