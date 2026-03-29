# Test for CNN model

def test_build_cnn():
    from src.models.cnn import build_cnn
    model = build_cnn((256, 256, 3), 10)
    assert model is not None
