import pytest 
from score_processor import ScoreProcessor 
 
 
@pytest.fixture 
def processor(): 
    return ScoreProcessor() 
 
 
def test_successful_score_processing(processor, tmp_path): 
 
    # Create temporary valid file 
    test_file = tmp_path / "score.txt" 
    test_file.write_text("5") 
 
    result = processor.process_score_file(str(test_file)) 
 
    assert result == 50 
 
 
def test_missing_file(processor): 
 
    with pytest.raises(FileNotFoundError): 
        processor.process_score_file("missing_file.txt") 
 
 
def test_invalid_number_format(processor, tmp_path): 
 
    # Create temporary invalid file 
    test_file = tmp_path / "invalid.txt" 
    test_file.write_text("abc") 
 
    with pytest.raises(ValueError): 
        processor.process_score_file(str(test_file))