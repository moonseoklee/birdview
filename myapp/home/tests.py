from django.test import TestCase
from myapp.item.models import Item
import json
# Create your tests here.

class mainTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(id=1,imageId="a",name="b",price=111,gender="a",
            category="O",ingredients="X",monthlySales="O",forOily=3,forDry=2,forSensitive=1)
        Item.objects.create(id=2,imageId="a",name="b",price=11,gender="a",
            category="O",ingredients="X",monthlySales="O",forOily=3,forDry=2,forSensitive=1)
        Item.objects.create(id=3,imageId="a",name="b",price=11,gender="a",
            category="O",ingredients="X",monthlySales="O",forOily=3,forDry=2,forSensitive=1)
        Item.objects.create(id=4,imageId="a",name="b",price=11,gender="a",
            category="O",ingredients="X",monthlySales="O",forOily=5,forDry=2,forSensitive=1)


   
    def test_only_product(self):
        res = self.client.get('http://127.0.0.1:8000/product/1/')
        temp = json.dumps(res.content.decode('utf8'))
        temp = temp.replace("'",'\"')[1:-1]
        
        
        temp = eval(temp)              
        
        self.assertFalse(temp[0]['name']=="a")
        self.assertTrue(temp[0]['name']=="b")
       
    def test_product_with_skintype(self):
        res = self.client.get('http://127.0.0.1:8000/product/1/?skin_type=dry')
        temp = json.dumps(res.content.decode('utf8'))
        
        temp = temp.replace("'",'\"')[1:-1]      
        
        temp = eval(temp)              
        

        #####serched product(1) + recommended(3) == 4  ##################
        self.assertEqual(len(temp),4)    
    
    def test_product_with_detail(self):
        res = self.client.get('http://127.0.0.1:8000/products/?skin_type=oily&exclude_ingredient=X&include_ingredient=palace')
        temp = json.dumps(res.content.decode('utf8'))
        
        temp = temp.replace("'",'\"')[1:-1]      
        
        temp = eval(temp)              
        
        
        
        self.assertEqual(len(temp),0)