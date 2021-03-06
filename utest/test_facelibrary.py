from pathlib import Path
from FaceLibrary import FaceLibrary
import pytest

testdata_directory = Path(__file__).parent.resolve() / "testdata"

def test_image_should_contain_a_face():
    face_detector = FaceLibrary()
    assert face_detector.is_face_in_image(str(testdata_directory /'faces.png')) == True
    face_detector.should_contain_a_face(str(testdata_directory /'faces.png'))

def test_image_should_not_contain_a_face():
    face_detector = FaceLibrary()
    assert face_detector.is_face_in_image(str(testdata_directory /'no_faces.jpg')) == False
    face_detector.should_not_contain_a_face(str(testdata_directory /'no_faces.jpg'))

def test_assertion_error_should_be_raised():
    face_detector = FaceLibrary()
    with pytest.raises(AssertionError):
        face_detector.should_contain_a_face(str(testdata_directory /'no_faces.jpg'))
    with pytest.raises(AssertionError):
        face_detector.should_not_contain_a_face(str(testdata_directory /'faces.png'))