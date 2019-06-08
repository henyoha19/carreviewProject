from django.test import TestCase
from django.urls import reverse
from .models import CarMake, CarModel, Review
import datetime
from .forms import CarMakeForm

from django.contrib.auth.models import User

# Create your tests here.
# test models

class CarMakeTest(TestCase):
    def test_string(self):
        make=CarMake(carmakename='nissan')
        self.assertEqual(str(make),make.carmakename)

class CarModelTest(TestCase):
    def test_string(self):
        model=CarModel(carmodelname='versa')
        self.assertEqual(str(model),model.carmodelname)

class ReviewTest(TestCase):
    def test_string(self):
        rev=Review(reviewtitle='Excellent')
        self.assertEqual(str(rev),rev.reviewtitle)

#test view
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetCarModelsTest(TestCase):
    def setUp(self):
        self.model=CarModel.objects.create(carmodelname='ford', carprice= 20000,
        manifacturingdate='2019-05-05', carmillage= 0, cardescription="durable car")

    
# test for forms
class CarMakeFormTest(TestCase):
    def setUp(self):
        self.userid2=User.objects.create(username='userid1', password='P@ssw0rd1')
        
    def test_carmodel_detail_sucess(self):
        response=self.client.get(reverse('carmodeldetails', args=(self.model.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_carmakeForm(self):
        data={
            'carmakename' : 'carmake1',
            'cardescription' : "car1",
        }
        form = CarMakeForm(data=data)
        self.assertTrue(form.is_valid)

    def test_carmakeFormInvalid(self):
        data={
            'carmakename' : 'carmake1',
            'cardescription' : "car1", 
        }
        form = CarmakeForm(data=data)
        self.assertFalse(form.is_valid())