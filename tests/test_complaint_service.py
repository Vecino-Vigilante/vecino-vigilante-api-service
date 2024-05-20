import unittest
from unittest.mock import MagicMock
from datetime import datetime, timedelta
from app.domain.models.complaint_model import ComplaintModel
from app.domain.models.marker_model import MarkerModel
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.application.services.complaint_service import ComplaintsService
from app.application.repositories.complaint_repository import ComplaintRepository
from app.application.repositories.files_repository import FilesRepository


class TestComplaintsService(unittest.TestCase):
    def setUp(self):
        self.mock_complaint_repository = MagicMock(spec=ComplaintRepository)
        self.mock_files_repository = MagicMock(spec=FilesRepository)
        self.service = ComplaintsService(
            self.mock_complaint_repository, self.mock_files_repository
        )

    def test_create_complaint_with_image(self):
        location = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        complaint = ComplaintModel(
            id=1,
            type_id=1,
            user_id=1,
            description="Test complaint",
            date=datetime.now(),
            location=location,
        )
        base64_image = "picture"
        expected_complaint = complaint
        expected_complaint.image_url = "uploaded_picture_url"

        self.mock_files_repository.upload_base64.return_value = "uploaded_picture_url"
        self.mock_complaint_repository.add_complaint.return_value = expected_complaint

        complaint_data = self.service.create_complaint(complaint, base64_image)

        self.assertEqual(complaint_data, expected_complaint)
        self.mock_files_repository.upload_base64.assert_called_once_with(
            base64_image, str(complaint.id).replace("-", "")
        )
        self.mock_complaint_repository.add_complaint.assert_called_once_with(complaint)

    def test_create_complaint_without_image(self):
        location = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        complaint = ComplaintModel(
            id=1,
            type_id=1,
            user_id=1,
            description="Test complaint",
            date=datetime.now(),
            location=location,
        )
        expected_complaint = complaint

        self.mock_complaint_repository.add_complaint.return_value = expected_complaint

        complaint_data = self.service.create_complaint(complaint)

        self.assertEqual(complaint_data, expected_complaint)
        self.mock_files_repository.upload_base64.assert_not_called()
        self.mock_complaint_repository.add_complaint.assert_called_once_with(complaint)

    def test_get_complaints(self):
        start_date = datetime.now() - timedelta(days=3)
        end_date = datetime.now() + timedelta(days=3)
        type_id = 1
        location1 = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        location2 = MarkerModel(
            id=2,
            incident_id=2,
            latitude=2.0,
            longitude=2.0,
            direction="another location",
        )
        complaint1 = ComplaintModel(
            id=1,
            type_id=1,
            user_id=1,
            description="Test complaint",
            date=datetime.now(),
            location=location1,
        )
        complaint2 = ComplaintModel(
            id=2,
            type_id=1,
            user_id=2,
            description="Another Test complaint",
            date=datetime.now(),
            location=location2,
        )
        expected_complaints = [complaint1, complaint2]

        self.mock_complaint_repository.get_complaints.return_value = expected_complaints

        filter_data = self.service.get_complaints(start_date, end_date, type_id)

        self.assertEqual(filter_data, expected_complaints)
        self.mock_complaint_repository.get_complaints.assert_called_once_with(
            start_date, end_date, type_id
        )

    def test_get_complaint_by_id_found(self):
        complaint_id = 1
        location = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        complaint = ComplaintModel(
            id=complaint_id,
            type_id=1,
            user_id=1,
            description="Test complaint",
            date=datetime.now(),
            location=location,
        )

        expected_complaint = complaint

        self.mock_complaint_repository.get_complaint.return_value = expected_complaint

        complaint_data = self.service.get_complaint_by_id(complaint_id)

        self.assertEqual(complaint_data, expected_complaint)
        self.mock_complaint_repository.get_complaint.assert_called_once_with(
            complaint_id
        )

    def test_get_complaint_by_id_not_found(self):
        complaint_id = 1

        self.mock_complaint_repository.get_complaint.return_value = None

        with self.assertRaises(ResourceNotFoundException):
            self.service.get_complaint_by_id(complaint_id)

        self.mock_complaint_repository.get_complaint.assert_called_once_with(
            complaint_id
        )

    def test_update_complaint(self):
        complaint_id = 1
        location = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        complaint = ComplaintModel(
            id=complaint_id,
            type_id=1,
            user_id=1,
            description="Updated complaint",
            date=datetime.now(),
            location=location,
        )
        base64_image = "updated_picture"
        expected_complaint = complaint
        expected_complaint.image_url = "updated_picture_url"

        self.mock_complaint_repository.get_complaint.return_value = expected_complaint
        self.mock_files_repository.upload_base64.return_value = "updated_picture_url"
        self.mock_complaint_repository.update_complaint.return_value = (
            expected_complaint
        )

        complaint_data = self.service.update_complaint(complaint, base64_image)

        self.assertEqual(complaint_data, expected_complaint)
        self.mock_complaint_repository.get_complaint.assert_called_once_with(
            complaint_id
        )
        self.mock_files_repository.upload_base64.assert_called_once_with(
            base64_image, str(complaint_id).replace("-", "")
        )
        self.mock_complaint_repository.update_complaint.assert_called_once_with(
            complaint
        )

    def test_update_complaint_not_found(self):
        complaint_id = 1
        location = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        complaint = ComplaintModel(
            id=complaint_id,
            type_id=1,
            user_id=1,
            description="Test complaint",
            date=datetime.now(),
            location=location,
        )

        self.mock_complaint_repository.get_complaint.return_value = None

        with self.assertRaises(ResourceNotFoundException):
            self.service.update_complaint(complaint)

        self.mock_complaint_repository.get_complaint.assert_called_once_with(
            complaint_id
        )

    def test_delete_complaint(self):
        complaint_id = 1
        location = MarkerModel(
            id=1, incident_id=1, latitude=1.0, longitude=1.0, direction="location"
        )
        expected_complaint = ComplaintModel(
            id=complaint_id,
            type_id=1,
            user_id=1,
            description="Test complaint",
            date=datetime.now(),
            location=location,
        )
        self.mock_complaint_repository.get_complaint.return_value = expected_complaint

        self.service.delete_complaint(complaint_id)

        self.mock_complaint_repository.get_complaint.assert_called_once_with(
            complaint_id
        )
        self.mock_complaint_repository.delete_complaint.assert_called_once_with(
            complaint_id
        )

    def test_delete_complaint_not_found(self):
        complaint_id = 1

        self.mock_complaint_repository.get_complaint.return_value = None

        with self.assertRaises(ResourceNotFoundException):
            self.service.delete_complaint(complaint_id)

        self.mock_complaint_repository.get_complaint.assert_called_once_with(
            complaint_id
        )


if __name__ == "__main__":
    unittest.main()
