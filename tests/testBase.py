import unittest
from mymodule import BaseModel  # Replace 'mymodule' with the actual module name containing the BaseModel class

class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def test_init_with_kwargs(self):
        """Test initializing BaseModel with keyword arguments."""
        data = {
            'id': 'test_id',
            'created_at': '2023-08-03T12:34:56.789',
            'updated_at': '2023-08-03T12:34:56.789',
            'name': 'Test Model',
            'value': 42,
        }

        instance = BaseModel(**data)

        self.assertEqual(instance.id, data['id'])
        self.assertEqual(instance.created_at.isoformat(), data['created_at'])
        self.assertEqual(instance.updated_at.isoformat(), data['updated_at'])
        self.assertEqual(instance.name, data['name'])
        self.assertEqual(instance.value, data['value'])

    def test_init_without_kwargs(self):
        """Test initializing BaseModel without keyword arguments."""
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)
        self.assertIs(instance.created_at, instance.updated_at)

    def test_save_updates_updated_at(self):
        """Test that calling save() updates the updated_at attribute."""
        instance = BaseModel()
        old_updated_at = instance.updated_at

        instance.save()

        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test converting BaseModel instance to a dictionary."""
        instance = BaseModel()
        instance.name = 'Test Model'
        instance.value = 42

        expected_dict = {
            'id': instance.id,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
            'name': 'Test Model',
            'value': 42,
            '__class__': 'BaseModel',
        }

        self.assertDictEqual(instance.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()

