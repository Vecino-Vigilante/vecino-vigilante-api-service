import unittest
from unittest.mock import MagicMock
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.domain.models.complaint_comment_model import ComplaintCommentModel
from app.application.services.complaint_comment_service import ComplaintCommentService
from app.application.repositories.complaint_comment_repository import (
    ComplaintCommentRepository,
)
from app.application.repositories.files_repository import FilesRepository
from datetime import datetime


class TestComplaintCommentService(unittest.TestCase):
    def setUp(self):
        self.mock_complaint_comment_repository = MagicMock(
            spec=ComplaintCommentRepository
        )
        self.mock_files_repository = MagicMock(spec=FilesRepository)
        self.service = ComplaintCommentService(
            self.mock_complaint_comment_repository, self.mock_files_repository
        )

    def test_add_complaint_comment_with_image(self):
        complaint_comment = ComplaintCommentModel(
            id=1, incident_id=1, user_id=1, content="Test comment", date=datetime.now()
        )
        base64_image = "picture"
        expected_comment = complaint_comment
        expected_comment.image_url = "uploaded_picture_url"

        self.mock_files_repository.upload_base64.return_value = "uploaded_picture_url"
        self.mock_complaint_comment_repository.add_comment.return_value = (
            expected_comment
        )

        comment_data = self.service.add_complaint_comment(
            complaint_comment, base64_image
        )

        self.assertEqual(comment_data, expected_comment)
        self.mock_files_repository.upload_base64.assert_called_once_with(
            base64_image, str(complaint_comment.id).replace("-", "")
        )
        self.mock_complaint_comment_repository.add_comment.assert_called_once_with(
            complaint_comment
        )

    def test_add_complaint_comment_without_image(self):
        complaint_comment = ComplaintCommentModel(
            id=1, incident_id=1, user_id=1, content="Test comment", date=datetime.now()
        )
        expected_comment = complaint_comment

        self.mock_complaint_comment_repository.add_comment.return_value = (
            expected_comment
        )

        comment_data = self.service.add_complaint_comment(complaint_comment)

        self.assertEqual(comment_data, expected_comment)
        self.mock_files_repository.upload_base64.assert_not_called()
        self.mock_complaint_comment_repository.add_comment.assert_called_once_with(
            complaint_comment
        )

    def test_get_complaint_comments(self):
        incident_id = 1
        complaint_comment1 = ComplaintCommentModel(
            id=1,
            incident_id=incident_id,
            user_id=1,
            content="Test comment",
            date=datetime.now(),
        )
        complaint_comment2 = ComplaintCommentModel(
            id=2,
            incident_id=incident_id,
            user_id=2,
            content="Another Test comment",
            date=datetime.now(),
        )
        expected_comments = [complaint_comment1, complaint_comment2]

        self.mock_complaint_comment_repository.get_complaint_comments.return_value = (
            expected_comments
        )

        incident_data = self.service.get_complaint_comments(incident_id)

        self.assertEqual(incident_data, expected_comments)
        self.mock_complaint_comment_repository.get_complaint_comments.assert_called_once_with(
            incident_id
        )

    def test_get_comment_by_id_found(self):
        comment_id = 1
        complaint_comment = ComplaintCommentModel(
            id=comment_id,
            incident_id=1,
            user_id=1,
            content="Test comment",
            date=datetime.now(),
        )
        expected_comment = complaint_comment

        self.mock_complaint_comment_repository.get_comment.return_value = (
            expected_comment
        )

        comment_data = self.service.get_comment_by_id(comment_id)

        self.assertEqual(comment_data, expected_comment)
        self.mock_complaint_comment_repository.get_comment.assert_called_once_with(
            comment_id
        )

    def test_get_comment_by_id_not_found(self):
        comment_id = 1
        self.mock_complaint_comment_repository.get_comment.return_value = None

        with self.assertRaises(ResourceNotFoundException):
            self.service.get_comment_by_id(comment_id)

        self.mock_complaint_comment_repository.get_comment.assert_called_once_with(
            comment_id
        )

    def test_update_complaint_comment(self):
        comment_id = 1
        complaint_comment = ComplaintCommentModel(
            id=comment_id,
            incident_id=1,
            user_id=1,
            content="Updated comment",
            date=datetime.now(),
        )
        base64_image = "updated_picture"
        expected_comment = complaint_comment
        expected_comment.image_url = "updated_picture_url"

        self.mock_complaint_comment_repository.get_comment.return_value = (
            expected_comment
        )
        self.mock_files_repository.upload_base64.return_value = "updated_picture_url"
        self.mock_complaint_comment_repository.update_comment.return_value = (
            expected_comment
        )

        comment_data = self.service.update_complaint_comment(
            complaint_comment, base64_image
        )

        self.assertEqual(comment_data, expected_comment)
        self.mock_complaint_comment_repository.get_comment.assert_called_once_with(
            comment_id
        )
        self.mock_files_repository.upload_base64.assert_called_once_with(
            base64_image, str(comment_id).replace("-", "")
        )
        self.mock_complaint_comment_repository.update_comment.assert_called_once_with(
            complaint_comment
        )

    def test_update_complaint_comment_not_found(self):
        comment_id = 1
        complaint_comment = ComplaintCommentModel(
            id=comment_id,
            incident_id=1,
            user_id=1,
            content="Updated comment",
            date=datetime.now(),
        )

        self.mock_complaint_comment_repository.get_comment.return_value = None

        with self.assertRaises(ResourceNotFoundException):
            self.service.update_complaint_comment(complaint_comment)

        self.mock_complaint_comment_repository.get_comment.assert_called_once_with(
            comment_id
        )

    def test_delete_comment(self):
        comment_id = 1
        expected_comment = ComplaintCommentModel(
            id=comment_id,
            incident_id=1,
            user_id=1,
            content="Test comment",
            date=datetime.now(),
        )

        self.mock_complaint_comment_repository.get_comment.return_value = (
            expected_comment
        )

        self.service.delete_comment(comment_id)

        self.mock_complaint_comment_repository.get_comment.assert_called_once_with(
            comment_id
        )
        self.mock_complaint_comment_repository.delete_comment.assert_called_once_with(
            comment_id
        )

    def test_delete_comment_not_found(self):
        comment_id = 1
        self.mock_complaint_comment_repository.get_comment.return_value = None

        with self.assertRaises(ResourceNotFoundException):
            self.service.delete_comment(comment_id)

        self.mock_complaint_comment_repository.get_comment.assert_called_once_with(
            comment_id
        )


if __name__ == "__main__":
    unittest.main()
