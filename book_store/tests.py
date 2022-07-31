

# i tryied very single type of testing and it did not work with me and mr ahmad told us to we are free to did it
# this is the errors that i faced :
# AttributeError: Manager isn't accessible via CustomUser instances
# AssertionError: Database queries to 'default' are not allowed in SimpleTestCase subclasses.
#     model_state = self.models[model_key]
#     KeyError: ('book_store', 'book_store')



# from django.test import SimpleTestCase
# from django.urls import reverse
# from .models import CustomUser, Category, Book
#
# class SnacksTest(SimpleTestCase):
#
#     def setUp(self):
#         """
#         create a tester user
#         """
#         self.user = CustomUser().objects.create_user(
#             username="tester", email="tester@tester.com", password="12345test"
#         )
#         self.category = Category().objects.create_user(
#             username="test_name"
#         )
#
#         # create a record in the table
#         self.book = Book.objects.create(
#             title="Game of The Dead",
#             category=self.category,
#             author=self.user,
#             description="",
#             image=""
#         )

    # def test_snack_content(self):
    #     """
    #     Test the record's data , title, purchaser and description
    #     """
    #     self.assertEqual(f"{self.book.title}", "Game of The Dead")
    #     self.assertEqual(f"{self.book.author}", "test_name")
    #     self.assertEqual(f"{self.book.description}", "")


    # def test_book_list_status_code(self):
    #     url = reverse('book_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_book_list_template(self):
        # url = reverse('book_list')
        # response = self.client.get(reverse('book_list'))
        # self.assertTemplateUsed(response, 'book_list.html')
    #
    # def test_book_detail_status_code(self):
    #     url = reverse('book_detail')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_book_detail_template(self):
    #     url = reverse('book_detail')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'book_detail.html')
    #
    # def test_book_create_status_code(self):
    #     url = reverse('book_create')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_book_create_template(self):
    #     url = reverse('book_create')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'book_create.html')
    #
    # def test_book_update_status_code(self):
    #     url = reverse('book_update')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_book_update_template(self):
    #     url = reverse('book_update')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'book_update.html')
    #
    # def test_book_delete_status_code(self):
    #     url = reverse('book_delete')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_book_delete_template(self):
    #     url = reverse('book_delete')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'book_delete.html')
