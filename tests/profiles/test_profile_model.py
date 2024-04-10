from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from veggie_recipe_book.recipes.validators import validate_image_size


class ProfileModelTestCase(TestCase):
    def test_image_size_validator(self):
        valid_image = SimpleUploadedFile("pic.jpg", b"file_content", content_type="image/jpeg")
        try:
            validate_image_size(valid_image)
        except ValidationError as e:
            self.fail(f"Validation error raised for valid image size: {e}")

        invalid_image = SimpleUploadedFile("big_pic.jpg", b"file_content" * 1024 * 1024 * 6,
                                           content_type="image/jpeg")
        with self.assertRaises(ValidationError):
            validate_image_size(invalid_image)

        with self.assertRaises(ValidationError):
            validate_image_size(invalid_image)
