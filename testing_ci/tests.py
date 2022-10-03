from django.test import TestCase

from testing_ci.models import Person

class PersonModelTest(TestCase):
    def create_a_person(self, first_name="Julien"):
        return Person.objects.create(first_name=first_name)

    def test_person_creation(self):
        person = self.create_a_person()
        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person.__str__(), person.first_name)
        
