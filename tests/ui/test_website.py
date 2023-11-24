def test_title(py):
    py.visit('https://david-herrera.dev/')
    assert py.should().contain_title('David Herrera')
