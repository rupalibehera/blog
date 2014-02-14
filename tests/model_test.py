import web
from blog import model
import unittest2 as unittest
from mock import patch


class ModelTest(unittest.TestCase):

  @patch.object(model,'get_db')
  def test_get_posts(self, mock_db):
    model.get_posts()
    self.assertTrue(mock_db.called)


if __name__ == "__main__":
  unittest.main()

